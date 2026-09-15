#!/usr/bin/env python3
"""Parallel range downloader for BACI_HS92_V202601.zip (CEPII).
Small 8MB segments + 24 workers: each HTTP connection yields ~10-20MB before
the server throttles, so many short-lived connections maximize throughput.
Resumable: existing segment files are kept. Final file verified by size."""
import os, sys, time, threading, queue, requests

URL = "https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS92_V202601.zip"
TOTAL = 2417732497
OUT = "/home/z/my-project/Russia-market/05-Data/raw/bac/BACI_HS92_V202601.zip"
PARTS = "/home/z/my-project/Russia-market/05-Data/raw/bac/parts"
SEG = 8 * 1024 * 1024            # 8MB segments
WORKERS = 24
N = (TOTAL + SEG - 1) // SEG

os.makedirs(PARTS, exist_ok=True)
q = queue.Queue()
for i in range(N):
    q.put(i)

lock = threading.Lock()
done_bytes = [0]
failed = []

def seg_path(i):
    return os.path.join(PARTS, f"p_{i:05d}")

def worker():
    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
    while True:
        try:
            i = q.get_nowait()
        except queue.Empty:
            return
        start = i * SEG
        end = min(start + SEG, TOTAL) - 1
        want = end - start + 1
        f = seg_path(i)
        have = os.path.getsize(f) if os.path.exists(f) else 0
        for attempt in range(12):
            if have >= want:
                break
            try:
                r = s.get(URL, headers={"Range": f"bytes={start+have}-{end}"}, timeout=(10, 60), stream=True)
                if r.status_code not in (200, 206):
                    r.close(); time.sleep(1 + attempt); continue
                with open(f, "ab") as fh:
                    for chunk in r.iter_content(1024 * 256):
                        fh.write(chunk)
                r.close()
                have = os.path.getsize(f)
            except Exception:
                time.sleep(1 + attempt)
                have = os.path.getsize(f) if os.path.exists(f) else 0
        if have < want:
            with lock:
                failed.append(i)
        with lock:
            done_bytes[0] += want
            print(f"seg {i}/{N} ok ({done_bytes[0]/1e6:.0f} MB placed)", flush=True)

threads = [threading.Thread(target=worker, daemon=True) for _ in range(WORKERS)]
for t in threads: t.start()
for t in threads: t.join()

if failed:
    print(f"FAILED segments: {failed[:20]} (total {len(failed)})", file=sys.stderr)
    sys.exit(1)

with open(OUT, "wb") as out:
    for i in range(N):
        with open(seg_path(i), "rb") as fh:
            while True:
                b = fh.read(4 * 1024 * 1024)
                if not b: break
                out.write(b)
got = os.path.getsize(OUT)
if got != TOTAL:
    print(f"SIZE MISMATCH got={got} want={TOTAL}", file=sys.stderr)
    sys.exit(1)
for i in range(N):
    os.remove(seg_path(i))
os.rmdir(PARTS)
print(f"OK: {OUT} ({got} bytes)")
