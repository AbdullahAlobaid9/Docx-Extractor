import os
import subprocess
from docx import Document

input_directory = 'docs/input'
output_directory = 'docs/output'

def convert_to_docx(doc_path, docx_path):
    """Convert .doc files to .docx using LibreOffice."""
    print(f"Converting {doc_path} to {docx_path}...")
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'docx',
                    '--outdir', os.path.dirname(docx_path), doc_path],
                   stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def extract_text_from_docx(docx_path):
    """Extract text from a .docx file using python-docx."""
    print(f"Extracting text from {docx_path}...")
    document = Document(docx_path)
    return '\n'.join([para.text for para in document.paragraphs])

def ensure_directory_exists(path):
    """Ensure that a directory exists, and if not, create it."""
    print(f"Ensuring directory exists: {path}")
    os.makedirs(path, exist_ok=True)

def process_files():
    """Process all .doc and .docx files within the input_directory recursively."""
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_base_name, file_extension = os.path.splitext(file)
            output_rel_path = os.path.relpath(root, input_directory)
            output_folder = os.path.join(output_directory, output_rel_path)
            ensure_directory_exists(output_folder)
            output_file_path = os.path.join(output_folder, f'{file_base_name}.txt')

            if file_extension.lower() == '.doc':
                docx_path = os.path.join(root, f'{file_base_name}.docx')
                convert_to_docx(file_path, docx_path)
                text = extract_text_from_docx(docx_path)
            elif file_extension.lower() == '.docx':
                text = extract_text_from_docx(file_path)

            # Save the extracted text to a text file
            if text:
                with open(output_file_path, 'w', encoding='utf-8') as text_file:
                    text_file.write(text)
                print(f"Extracted text saved to {output_file_path}")

if __name__ == "__main__":
    process_files()
