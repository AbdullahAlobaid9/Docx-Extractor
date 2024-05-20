import os
import json

def combine_text_files(input_directory, output_json_path):
    text_data = {}
    
    # Walk through the input directory
    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read the content of the file
                    content = file.read().strip()
                    # Use filename as key or modify as needed
                    text_data[filename] = content
    
    # Write the dictionary to a JSON file
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(text_data, json_file, indent=4, ensure_ascii=False)

    print(f"JSON file created at {output_json_path}")

# Define the input and output paths
input_directory = '/media/abdullah-alobaid/RIOTU/Serry Sibaee/files'
output_json = '/media/abdullah-alobaid/RIOTU/Serry Sibaee/combined_text.json'


combine_text_files(input_directory, output_json)
