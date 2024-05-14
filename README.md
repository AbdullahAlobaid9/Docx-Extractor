# DOCX to Text Converter

This script leverages Apache Tika to extract text from DOCX files and saves it as plain text files. The output maintains the organization by paragraphs, making it easier to read and process the text data programmatically.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python 3.6+**: The script is written in Python and requires a modern version of the interpreter.
- **pip**: Python's package manager, used to install dependencies.

## Installation

Follow these steps to set up your environment and run the script:

### 1. Clone the Repository

Clone the repository to your local machine and navigate to the cloned directory:

```bash
git clone https://github.com/AbdullahAlobaid9/DOCX-Extractor
cd DOCX-Extractor
```

### 2. Install Python Dependencies

Install the required Python packages using pip:
      pip install -r requirements.txt

### 3. Install Apache Tika

Download and install Apache Tika Server. You can download it from the Apache website:

(https://www.apache.org/dyn/closer.lua/tika/3.0.0-BETA/tika-server-standard-3.0.0-BETA.jar
)
After downloading, place the .jar file in a known directory.

## Usage

To use the DOCX to Text Converter, follow these steps:
### Start Apache Tika Server

First, start the Apache Tika server using the following command:
      java -jar /path/to/tika-server-standard-3.0.0-BETA.jar

Make sure to replace /path/to/ with the actual path where the Tika server .jar file is located.

## Run the Script

Execute the script to begin processing your DOCX files:

```bash

   python doc_extractor.py
```

## How It Works

The script communicates with the Apache Tika server to convert DOCX files into plain text. The text is extracted maintaining the paragraph structure and saved in separate .txt files corresponding to each DOCX file processed.