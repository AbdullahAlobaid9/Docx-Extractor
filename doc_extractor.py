import os
from tika import parser
import logging
from multiprocessing import Pool, cpu_count

input_directory = '/media/abdullah-alobaid/RIOTU/Serry Sibaee/files'
output_directory = '/media/abdullah-alobaid/RIOTU/Serry Sibaee/text_output'

def setup_logging():
    logging.basicConfig(level=logging.INFO, filename='doc_conversion.log',
                        format='%(asctime)s - %(levelname)s - %(message)s')

def process_file(file_path):
    logging.info(f"Starting processing for {file_path}")
    try:
        # Use Apache Tika to parse the file
        parsed = parser.from_file(file_path, serverEndpoint='http://localhost:9998')
        text = parsed.get('content')
        if text:
            file_base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_file_path = os.path.join(output_directory, f'{file_base_name}.txt')
            with open(output_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text.strip())
            logging.info(f"Extracted text saved to {output_file_path}")
        else:
            logging.info(f"No text extracted from {file_path}")
    except Exception as e:
        logging.error(f"Failed to process {file_path}: {e}")

def process_files():
    setup_logging()
    file_paths = []
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith('.doc'):
                file_paths.append(os.path.join(root, file))
    
    num_processes = max(1, min(cpu_count() - 1, 4))  # Limit the number of processes
    with Pool(processes=num_processes) as pool:
        pool.map(process_file, file_paths)

if __name__ == "__main__":
    process_files()
