# Pippy

Pippy is the bee who stars in Word Meadow. These are the cropped, transparent
poses the website uses.

## Adding the art

The source files are the two green-screen sprite sheets (four poses each —
one sheet flying, one standing). They are kept in `raw-art/`:

```
raw-art/Pippy - Flying - Green.png
raw-art/Pippy-4 poses - Green.png
```

To regenerate the crops from them:

```bash
python3 tools/crop-pippy.py "raw-art/Pippy - Flying - Green.png" "raw-art/Pippy-4 poses - Green.png"
```

That keys out the green, splits each sheet on the gaps between poses, trims
every pose to its own bounding box, and writes this folder:

```
pippy/fly-1.png    pippy/stand-1.png
pippy/fly-2.png    pippy/stand-2.png
pippy/fly-3.png    pippy/stand-3.png
pippy/fly-4.png    pippy/stand-4.png
```

Requires Pillow (`pip install Pillow`). The script drops the little sparkle
in the sheet corner automatically — it keeps only the four largest shapes.

## Where each pose is used

| File           | Used on                                              |
|----------------|------------------------------------------------------|
| `fly-1.png`    | Homepage Word Meadow spotlight; Word Meadow hero      |
| `fly-2.png`    | Homepage "Explore" card row; games page hero           |
| `fly-3.png`    | Word Meadow "How To Play"                             |
| `fly-4.png`    | Games page, Word Meadow block                         |
| `stand-1.png`  | Homepage "Who We Are"; Word Meadow "Your Mission" — the "Hi, I'm Pippy!" portrait |
| `stand-2.png`  | Word Meadow closing call-to-action (mirrored to face left) |
| `stand-3.png`, `stand-4.png` | Spare — swap in anywhere               |

Every Pippy `<img>` carries `class="pippy"`. If a file is missing the page
hides that image instead of showing a broken icon, so the site is safe to
deploy before the art lands.
