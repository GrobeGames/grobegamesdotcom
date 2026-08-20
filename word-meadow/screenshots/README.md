# Word Meadow screenshots

Drop the ten App Store screenshots (the `export/iPhone-6.9` set) in this folder,
named `01.png` through `10.png`:

```
word-meadow/screenshots/01.png
word-meadow/screenshots/02.png
...
word-meadow/screenshots/10.png
```

From the machine that has them, that's:

```bash
cd ~/Downloads/export/iPhone-6.9
i=1; for f in $(ls -1 | sort); do
  cp "$f" "/path/to/grobegamesdotcom/word-meadow/screenshots/$(printf '%02d' $i).png"
  i=$((i+1))
done
```

Ordering matters — `01`, `02` and `03` are the three phones featured in the hero,
so put the most eye-catching shots first. The remaining seven fill the
"Peek Into the Meadow" gallery further down the page.

The page degrades gracefully: any screenshot that isn't present is dropped from
the layout at load time rather than rendering as a broken image, and a group that
ends up empty hides itself. So the page is safe to deploy before the images land.

## App icon

The Word Meadow app icon belongs at `word-meadow/app-icon.png` (1024×1024 PNG).
Until it's added, the hero falls back to `../word-meadows-screenshot.png`.
