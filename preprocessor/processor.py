import os
from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption, WordFormatOption
from docling.datamodel.base_models import InputFormat
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.pipeline.simple_pipeline import SimplePipeline
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline


import os
import certifi

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['SSL_CERT_FILE'] = certifi.where()

class ProcessDocs:
    def __init__(self):
        # Initialize converter once in __init__
        self.doc_converter = DocumentConverter(
            allowed_formats=[InputFormat.PDF, InputFormat.DOCX, InputFormat.IMAGE], 
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_cls=StandardPdfPipeline, backend=PyPdfiumDocumentBackend
                ),
                InputFormat.DOCX: WordFormatOption(pipeline_cls=SimplePipeline)
            },
        )

    def run(self, source_dir, output_dir):
        source_path = Path(source_dir)
        output_base = Path(output_dir)
        output_base.mkdir(parents=True, exist_ok=True)

        # 1. Collect all file paths (the "Scouting" phase)
        input_files = []
        for root, dirs, files in os.walk(source_path):
            category = Path(root).name # e.g., 'compactlogix'
            
            for i, f_name in enumerate(files):
                full_input_path = Path(root) / f_name
                
                # We store a tuple: (source_path, target_filename)
                # target: processed_docs/compactlogix_f0.md
                target_name = f"{category}_f{i}.md"
                input_files.append((full_input_path, target_name))

        # 2. Convert everything in bulk (The "Action" phase)
        # We only pass the actual file paths to Docling
        file_paths_only = [item[0] for item in input_files]
        conv_results = self.doc_converter.convert_all(file_paths_only)

        # 3. Save results using the names we generated
        for result, (original_path, target_name) in zip(conv_results, input_files):
            if result.document:
                final_output_path = output_base / target_name
                with final_output_path.open("w", encoding="utf-8") as f:
                    f.write(result.document.export_to_markdown())
                print(f" Processed: {original_path.name} -> {target_name}")

# --- Execution ---
basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
docs_folder = Path(basepath) / "docs"
processed_folder = Path(basepath) / "processed_docs"

processor = ProcessDocs()
processor.run(docs_folder, processed_folder)
            
if __name__ == "__main__":
    processor = ProcessDocs()
    processor.run(docs_folder, processed_folder)
    