import os
import logging
from pathlib import Path

from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline
from docling.datamodel.pipeline_options import PdfPipelineOptions

# Suppress RapidOCR empty-result warnings — expected on diagram/image-only pages
logging.getLogger("docling").setLevel(logging.ERROR)

basepath = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
docs_folder = basepath / "docs"
processed_base = basepath / "processed_docs"


class PROCESSDOCS:

    def __init__(self):
        # Disable OCR — AB manuals are text-layer PDFs, not scanned.
        # OCR only needed if you have actual scanned/image PDFs.
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = False
        pipeline_options.do_table_structure = True   # keep table extraction

        self.doc_converter = DocumentConverter(
            allowed_formats=[InputFormat.PDF],
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_cls=StandardPdfPipeline,
                    backend=PyPdfiumDocumentBackend,
                    pipeline_options=pipeline_options,
                ),
            },
        )

    def process_documents(self):
        processed_base.mkdir(exist_ok=True)

        # Collect all PDFs preserving family subfolder for naming
        pdf_paths = []
        for family_dir in docs_folder.iterdir():
            if family_dir.is_dir():
                for pdf_file in family_dir.glob("*.pdf"):
                    pdf_paths.append((family_dir.name, pdf_file))

        if not pdf_paths:
            print("No PDFs found in docs/")
            return

        print(f"Converting {len(pdf_paths)} PDFs...")

        for family, pdf_path in pdf_paths:
            # Output: processed_docs/controllogix/1756-um001-en-p.md
            out_dir = processed_base / family
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / (pdf_path.stem + ".md")

            if out_path.exists():
                print(f"  SKIP  {family}/{pdf_path.name}")
                continue

            try:
                result = self.doc_converter.convert(str(pdf_path))
                markdown = result.document.export_to_markdown()
                out_path.write_text(markdown, encoding="utf-8")
                print(f"  OK    {family}/{pdf_path.name} -> {out_path.name}")
            except Exception as e:
                print(f"  ERR   {family}/{pdf_path.name}: {e}")


if __name__ == "__main__":
    processor = PROCESSDOCS()
    processor.process_documents()
