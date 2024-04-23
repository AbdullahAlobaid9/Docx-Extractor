import os
import subprocess
from docx import Document
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

input_directory = 'docs/input'
output_directory = 'docs/output'

def ensure_directory_exists(path):
    """Ensure that a directory exists, and if not, create it."""
    os.makedirs(path, exist_ok=True)

def convert_to_docx(doc_path, docx_path):
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'docx',
                    '--outdir', os.path.dirname(docx_path), doc_path],
                   stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def extract_text_from_docx(docx_path):
    try:
        document = Document(docx_path)
        text = '\n'.join([para.text for para in document.paragraphs])
        return text
    except Exception as e:
        print(f"Failed to read {docx_path}: {str(e)}")
        return None

def process_file(file):
    root, file = file
    file_path = os.path.join(root, file)
    file_base_name, file_extension = os.path.splitext(file)
    output_file_path = os.path.join(output_directory, f'{file_base_name}.txt')

    if file_extension.lower() == '.doc':
        docx_path = os.path.join(root, f'{file_base_name}.docx')
        convert_to_docx(file_path, docx_path)
        text = extract_text_from_docx(docx_path)
    elif file_extension.lower() == '.docx':
        text = extract_text_from_docx(file_path)

    if text:
        with open(output_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        print(f"Extracted text saved to {output_file_path}")
    else:
        print(f"No text extracted from {file_path}")

def process_files():
    files_to_process = [(root, file) for root, _, files in os.walk(input_directory) for file in files if file.lower().endswith(('.doc', '.docx'))]
    cpu_count = multiprocessing.cpu_count()
    workers = max(1, int(cpu_count * 0.6))  # Use up to 90% of CPU cores

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(process_file, file) for file in files_to_process]
        for future in as_completed(futures):
            future.result()  # Collect result or re-raise exception

if __name__ == "__main__":
    process_files()
