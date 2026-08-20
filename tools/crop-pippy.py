#!/usr/bin/env python3
"""
Turn the green-screen Pippy sprite sheets into tightly-cropped transparent PNGs.

Usage:
    python3 tools/crop-pippy.py FLYING_SHEET.png STANDING_SHEET.png

Each sheet holds four poses side by side on a green background. This keys out
the green, splits the sheet on the empty columns between poses, trims each pose
to its own bounding box, and writes:

    pippy/fly-1.png   … fly-4.png
    pippy/stand-1.png … stand-4.png

Requires Pillow:  pip install Pillow
"""
import sys, os
from PIL import Image

OUT_DIR = "pippy"
MAX_H = 900          # cap output height; keeps files light for the web
FEATHER_TOL = 0.55   # edge pixels this green get partial alpha instead of a hard cut


def greenness(r, g, b):
    """How much this pixel reads as chroma-key green, 0..1."""
    if g <= r or g <= b:
        return 0.0
    # distance of green above the stronger of the other two channels,
    # normalised so a vivid key returns ~1 and skin/fur returns ~0
    dom = g - max(r, b)
    return min(1.0, dom / 90.0)


def key_out_green(im):
    """Return an RGBA copy with the green background removed and despilled."""
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            k = greenness(r, g, b)
            if k >= FEATHER_TOL:
                px[x, y] = (r, g, b, 0)
            elif k > 0:
                # Partial edge pixel: soften alpha and pull the green spill out
                # so the halo doesn't glow against a light page.
                new_a = int(a * (1.0 - k / FEATHER_TOL))
                avg = (r + b) // 2
                px[x, y] = (r, min(g, avg + 12), b, new_a)
    return im


def column_segments(im, min_width=20):
    """Column ranges that contain visible (non-transparent) pixels."""
    w, h = im.size
    px = im.load()
    occupied = []
    for x in range(w):
        hit = False
        for y in range(0, h, 2):          # every other row is plenty
            if px[x, y][3] > 12:
                hit = True
                break
        occupied.append(hit)

    segments, start = [], None
    for x, on in enumerate(occupied):
        if on and start is None:
            start = x
        elif not on and start is not None:
            if x - start >= min_width:
                segments.append((start, x))
            start = None
    if start is not None and w - start >= min_width:
        segments.append((start, w))
    return segments


def process(path, prefix):
    if not os.path.exists(path):
        print(f"  !! missing: {path}")
        return 0
    sheet = key_out_green(Image.open(path))
    segments = column_segments(sheet)

    # Keep the four biggest blobs — drops stray sparkles/watermarks.
    frames = []
    for x0, x1 in segments:
        piece = sheet.crop((x0, 0, x1, sheet.size[1]))
        bbox = piece.getbbox()
        if not bbox:
            continue
        piece = piece.crop(bbox)
        frames.append(piece)
    frames.sort(key=lambda i: i.size[0] * i.size[1], reverse=True)
    frames = frames[:4]

    if not frames:
        print(f"  !! no poses found in {path} — is it really a green-screen sheet?")
        return 0

    # Restore left-to-right order among the kept frames
    order = {id(f): i for i, f in enumerate(frames)}
    frames.sort(key=lambda f: order[id(f)])

    os.makedirs(OUT_DIR, exist_ok=True)
    for i, frame in enumerate(frames, 1):
        if frame.size[1] > MAX_H:
            ratio = MAX_H / frame.size[1]
            frame = frame.resize(
                (max(1, round(frame.size[0] * ratio)), MAX_H), Image.LANCZOS
            )
        out = os.path.join(OUT_DIR, f"{prefix}-{i}.png")
        frame.save(out, optimize=True)
        print(f"  {out}  {frame.size[0]}x{frame.size[1]}")
    return len(frames)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    total = 0
    print("Flying poses:")
    total += process(sys.argv[1], "fly")
    print("Standing poses:")
    total += process(sys.argv[2], "stand")
    print(f"\nDone — {total} pose(s) written to {OUT_DIR}/")
    if total < 8:
        print("Expected 8. Check the sheets if that looks wrong.")


if __name__ == "__main__":
    main()
