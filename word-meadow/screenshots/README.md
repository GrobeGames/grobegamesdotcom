# Word Meadow screenshots

The ten App Store screenshots (the `export/iPhone-6.9` set), named `01.png`
through `10.png`.

Ordering matters — `01`, `02` and `03` are the three phones featured in the hero.
The hero renders them `02 · 01 · 03` left to right, so **`01` is the centre phone**
and gets the strongest shot. The remaining seven fill the "Peek Into the Meadow"
gallery further down the page.

## Current mapping

| File     | Source (`export/iPhone-6.9`) | Where |
|----------|------------------------------|-------|
| `01.png` | `02-gameplay.jpg`            | Hero, centre — the honeycomb word-trace board |
| `02.png` | `03-campaign.jpg`            | Hero, left — the meadow path, twenty zones |
| `03.png` | `04-restore-meadows.jpg`     | Hero, right — the restored-meadow beauty shot |
| `04.png` | `01-hero.jpg`                | Gallery — title screen |
| `05.png` | `05-my-meadows.jpg`          | Gallery |
| `06.png` | `06-daily-puzzle.jpg`        | Gallery |
| `07.png` | `07-endless.jpg`             | Gallery |
| `08.png` | `08-closet.jpg`              | Gallery |
| `09.png` | `09-holiday-closets.jpg`     | Gallery |
| `10.png` | `10-awards.jpg`              | Gallery |

The sources are 1290×2796 JPEGs. They are resampled to 860px wide and saved as
256-colour PNGs (~380 KB each, ~3.8 MB for the set). The page never renders a
phone wider than about 320 CSS px, so shipping the full-resolution originals
would cost ~26 MB for no visible gain. If you re-export, keep the same treatment:

```bash
python3 - <<'PY'
from PIL import Image
SRC = 'export/iPhone-6.9'
order = ['02-gameplay','03-campaign','04-restore-meadows','01-hero','05-my-meadows',
         '06-daily-puzzle','07-endless','08-closet','09-holiday-closets','10-awards']
for i, name in enumerate(order, 1):
    im = Image.open(f'{SRC}/{name}.jpg').convert('RGB')
    im = im.resize((860, round(im.size[1] * 860 / im.size[0])), Image.LANCZOS)
    im.quantize(colors=256, dither=Image.FLOYDSTEINBERG).save(
        f'word-meadow/screenshots/{i:02d}.png', optimize=True)
PY
```

The page degrades gracefully: any screenshot that isn't present is dropped from
the layout at load time rather than rendering as a broken image, and a group that
ends up empty hides itself. So the page is safe to deploy before the images land.

## App icon

The Word Meadow app icon lives at `word-meadow/app-icon.png` (1024×1024 PNG,
sourced from `Word Meadow App Logo.png`). It feeds the Word Meadow hero, the
"Meet Word Meadow" box on the homepage, and the favicon. If it goes missing the
hero falls back to `../word-meadows-screenshot.png`.
