import os
from cleaner import clean_text
from tqdm import tqdm

def stream_to_json_and_text(input_directory, output_json_path, output_text_path):
    # Ensure the output directories exist
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_text_path), exist_ok=True)

    total_files = sum(len(files) for _, _, files in os.walk(input_directory) if files)

    with open(output_json_path, 'w', encoding='utf-8') as json_file, \
         open(output_text_path, 'w', encoding='utf-8') as text_file:
        json_file.write('[\n')
        first = True
        counter = 1  # Initialize a counter for the keys

        for root, dirs, files in os.walk(input_directory):
            for filename in tqdm(files, total=total_files, desc="Processing files"):
                if filename.endswith('.txt'):
                    if not first:
                        json_file.write(',\n')
                    first = False
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read().strip()
                        cleaned_content = clean_text(content)
                        cleaned_content_json = cleaned_content.replace('"', '\\"')
                        
                        # Write to JSON
                        json_file.write('{')
                        json_file.write(f'"file_{counter}": "{cleaned_content_json}"')
                        json_file.write('}')

                        # Write to text file
                        text_file.write(cleaned_content + "\n")  # Optional: add newline for each document
                        
                        counter += 1  # Increment the counter
        json_file.write('\n]')

    print("Finished writing to JSON and text file.")

# Define the input and output paths
input_dir = '/home/riotu/Abdullah-Projects/Docx-Extractor/docs/input/'  # Make sure to update this path to your actual input directory
output_json = '/home/riotu/Abdullah-Projects/Docx-Extractor/docs/output/all_texts.json'  # Update this path to your desired output directory
output_text = '/home/riotu/Abdullah-Projects/Docx-Extractor/docs/output/all_texts.txt'  # Update this path to your desired output directory

stream_to_json_and_text(input_dir, output_json, output_text)