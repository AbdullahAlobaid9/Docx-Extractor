import os
import subprocess
from docx import Document

# Specify directories
input_directory = 'docs/input/'; 
output_directory = 'docs/output/'; 

def convert_to_docx(doc_path, docx_path):
    # Convert .doc to .docx using LibreOffice
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'docx',
                    '--outdir', os.path.dirname(docx_path), doc_path],
                   stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def extract_text_from_docx(docx_path):
    # Open and read a .docx file
    document = Document(docx_path)
    return '\n'.join([para.text for para in document.paragraphs])

for filename in os.listdir(input_directory):
    filepath = os.path.join(input_directory, filename)
    fileBaseName, fileExtension = os.path.splitext(filename)
    output_text_path = os.path.join(output_directory, f'{fileBaseName}.txt')
    
    if fileExtension.lower() == '.doc':
        # Convert .doc to .docx
        docx_path = os.path.join(input_directory, f'{fileBaseName}.docx')
        convert_to_docx(filepath, docx_path)
        text = extract_text_from_docx(docx_path)
    elif fileExtension.lower() == '.docx':
        # Directly extract text from .docx
        text = extract_text_from_docx(filepath)
    else:
        continue  # Skip non-doc and non-docx files

    # Save the extracted text to a text file
    with open(output_text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

    print(f"Extracted text saved to {output_text_path}")
