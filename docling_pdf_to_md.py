#!/usr/bin/env python3
"""
Convert a PDF document to Markdown
Based on the [Simple conversion](https://docling-project.github.io/docling/examples/minimal/) example.

Usage:
  ./docling_pdf_to_md.py {/path/to/file or URL}
  ./docling_pdf_to_md.py /Users/thomas/Downloads/Release-notes-35-GA-24-07.pdf

"""

from docling.document_converter import DocumentConverter
import sys
import time

start_time = time.time()

source = sys.argv[1]  # document per local path or URL
print(f"Converting {sys.argv[1]} ...")

converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())
# output: ## Docling Technical Report [...]"

print(f"⏲ {'{0:.3f}'.format(time.time() - start_time)} seconds", file=sys.stderr)
