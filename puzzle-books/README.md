# Puzzle Books page

`index.html` is grobegames.com/puzzle-books/: the Clear Page Puzzles books (large-print puzzle books on Amazon).
The bookshelf at the top opens each book; the word search further down is playable.

- **Images** in `img/` are rendered from the books' own print PDFs by `tools/web_images.py` in the
  GrobeGames/puzzle-books repo: `uv run python tools/web_images.py <this folder>/img`. Rerun it if a cover changes.
- **Book facts** (puzzle counts, print sizes, page counts, back-cover text) come from that repo's `books/bookN.toml`
  and build output. Change them there first, then here.
- **Amazon links**: each book's button is a placeholder `<span class="btn-amazon is-soon">` marked with an
  `<!-- AMAZON bookN -->` comment. When a book goes live, swap the span for the link in the comment, with the
  book's ASIN, and change its "Coming soon to Amazon" tag.
- Direct links open one book: `puzzle-books/#word-search`, `#number-puzzles`, `#cat-word-search`.
- Book 2 is called "number puzzles" everywhere, on the page as in the book.
