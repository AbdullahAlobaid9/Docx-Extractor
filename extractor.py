import os
from docx import Document

def docx_to_text(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith('.docx'):
            filepath = os.path.join(input_directory, filename)
            try:
                document = Document(filepath)
                text = [para.text for para in document.paragraphs]

                output_filepath = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.txt")
                with open(output_filepath, 'w', encoding='utf-8') as text_file:
                    text_file.write('\n'.join(text))
                
                print(f"Text extracted and saved to {output_filepath}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

# Specify directories
input_directory = 'docs/input/'; 
output_directory = 'docs/output/'; 

# Run the function
docx_to_text(input_directory, output_directory)
