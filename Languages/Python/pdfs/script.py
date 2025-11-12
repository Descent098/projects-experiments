import fitz  # PyMuPDF
import os
import pypub
import re
import sys
import html


def extract_text_from_pdf(pdf_path):
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")
    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError("The file must be a PDF.")

    doc = fitz.open(pdf_path)
    pages = [page.get_text("text").strip() for page in doc]
    doc.close()
    return pages


def extract_toc(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        toc = doc.get_toc() or []
        doc.close()
        return toc
    except Exception:
        return []


def safe_html(text: str) -> str:
    """Escape any angle brackets etc. so pypub's XML parser won't choke."""
    return "<pre>" + html.escape(text) + "</pre>"


def make_epub_from_text(title, text_pages, toc=None, start_page=7, max_pages_per_chapter=20):
    epub = pypub.Epub(title)

    total_pages = len(text_pages)
    start_page = max(1, start_page)

    def add_chapter(epub_obj, title_text, full_text):
        if not full_text.strip():
            return
        # escape possible pseudo-HTML and wrap in <pre> so formatting is preserved
        safe_content = safe_html(full_text)
        # pypub expects bytes, so encode
        content_bytes = safe_content.encode("utf-8", "replace")
        epub_obj.add_chapter(pypub.Chapter(title=title_text, content=content_bytes))

    # ---- Use TOC if available ----
    if toc:
        print(f"Using Table of Contents with {len(toc)} entries.")
        usable = [entry for entry in toc if entry[2] >= start_page]
        if usable:
            for idx, (level, t, pnum) in enumerate(usable):
                start_idx = pnum - 1
                end_idx = usable[idx + 1][2] - 1 if idx + 1 < len(usable) else total_pages
                chunk = "\n\n".join(text_pages[start_idx:end_idx])
                add_chapter(epub, t, chunk)
            return epub

    # ---- Otherwise, fallback to regex-based chapter detection ----
    print("No TOC found; splitting by detected chapter headings or page count...")
    chapter_pattern = re.compile(
        r'^(?:\s*(?:book|part|chapter|section|volume)\b[\s\.\-:]*[IVXLCDM\d]+)',
        re.IGNORECASE | re.MULTILINE
    )

    current = []
    chapter_counter = 0
    pages_since_last = 0

    for idx, page_text in enumerate(text_pages[start_page - 1:], start=start_page):
        pages_since_last += 1
        if chapter_pattern.search(page_text) or pages_since_last >= max_pages_per_chapter:
            if current:
                chapter_counter += 1
                joined = "\n\n".join(current)
                add_chapter(epub, f"Chapter {chapter_counter}", joined)
                print(f"Added Chapter {chapter_counter} at page {idx}")
                current = []
                pages_since_last = 0
        current.append(page_text)

    if current:
        chapter_counter += 1
        add_chapter(epub, f"Chapter {chapter_counter}", "\n\n".join(current))
        print(f"Added final Chapter {chapter_counter}")

    return epub


if __name__ == "__main__":
    filename = "heretics of dune.pdf"

    try:
        pages = extract_text_from_pdf(filename)
        print(f"Extracted {len(pages)} pages.")
    except Exception as e:
        print(f"Error extracting text: {e}")
        sys.exit(1)

    toc = extract_toc(filename)

    epub = make_epub_from_text("Heretics of Dune", pages, toc=toc, start_page=7)
    out = "heretics_of_dune.epub"

    try:
        epub.create(out)
        print(f"✅ EPUB created successfully: {out}")
    except Exception as e:
        print(f"❌ EPUB creation failed: {e}")
        raise
