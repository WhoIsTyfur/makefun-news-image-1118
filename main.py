"""make.fun news-image-20261118 entry: writes the committed front page to the output folder."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(HERE, "entry.png"), "rb") as f:
    data = f.read()

# The gate takes only a whole PNG or JPEG of at most 1 MiB.
if not (data.startswith(b"\x89PNG\r\n\x1a\n") or data.startswith(b"\xff\xd8")) or len(data) > 1048576:
    sys.exit("entry.png is not a PNG/JPEG within 1 MiB")

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.png"), "wb") as f:
    f.write(data)
