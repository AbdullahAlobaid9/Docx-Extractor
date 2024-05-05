import os
import subprocess
from docx import Document
import logging
import time
from multiprocessing import Pool, cpu_count

input_directory = '/media/abdullah-alobaid/RIOTU/Serry Sibaee/files'
output_directory = '/media/abdullah-alobaid/RIOTU/Serry Sibaee/text_output'


def setup_logging():
    logging.basicConfig(level=logging.INFO, filename='doc_conversion.log',
                        format='%(asctime)s - %(levelname)s - %(message)s')

def convert_to_docx(doc_path, docx_path):
    try:
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'docx',
                        '--outdir', os.path.dirname(docx_path), doc_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except Exception as e:
        logging.error(f"Error converting {doc_path} to DOCX: {e}")
        raise

def extract_text_from_docx(docx_path):
    try:
        document = Document(docx_path)
        return '\n'.join([para.text for para in document.paragraphs])
    except Exception as e:
        logging.error(f"Error extracting text from {docx_path}: {e}")
        raise

def ensure_directory_exists(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        logging.error(f"Error ensuring directory {path} exists: {e}")
        raise

def process_file(file_path):
    try:
        file_base_name, file_extension = os.path.splitext(os.path.basename(file_path))
        output_file_path = os.path.join(output_directory, f'{file_base_name}.txt')
        ensure_directory_exists(os.path.dirname(output_file_path))
        
        if file_extension.lower() == '.doc':
            docx_path = os.path.join(output_directory, f'{file_base_name}.docx')
            convert_to_docx(file_path, docx_path)
            text = extract_text_from_docx(docx_path)
            os.remove(docx_path)
        elif file_extension.lower() == '.docx':
            text = extract_text_from_docx(file_path)

        if text:
            with open(output_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
            logging.info(f"Extracted text saved to {output_file_path}")
    except Exception as e:
        logging.error(f"Failed to process {file_path}: {e}")

def process_files():
    setup_logging()
    file_paths = []
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(('.doc', '.docx')):
                file_paths.append(os.path.join(root, file))
    
    num_processes = max(1, min(cpu_count() - 1, 4))  # Limit the number of processes
    with Pool(processes=num_processes) as pool:
        pool.map(process_file, file_paths)

if __name__ == "__main__":
    process_files()
