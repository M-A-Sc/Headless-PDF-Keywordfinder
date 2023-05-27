#M-A-SC
#https://github.com/M-A-Sc/Headless-PDF-Keywordfinder

import os
import PyPDF2
from datetime import datetime

def search_pdf_folder(folder_path, sentences):
    try:
        # List of all pdfs in the dir
        pdf_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.pdf')]

        if len(pdf_files) == 0:
            print('Error: No .pdf found')
            return

        # For each .pdf in the dir
        for pdf_file in pdf_files:
            pdf_path = os.path.join(folder_path, pdf_file)

            # Open .pdf
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                total_occurrences = 0
                max_occurrences = 0
                max_occurrences_page = None

                # Show name
                print(f"Name of PDF File: {pdf_file}")

                # Show Size and date of Creation
                file_size = os.path.getsize(pdf_path) / (1024 * 1024)  # in MB
                creation_time = os.path.getctime(pdf_path)
                formatted_creation_time = datetime.fromtimestamp(creation_time).strftime('%d/%m/%Y')
                print(f"PDF Size: {file_size:.2f} MB")
                print(f"File Creation: {formatted_creation_time}")

                # For each .pdf 
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()

                    # Search Keywords and show count
                    occurrences = 0
                    for sentence in sentences:
                        occurrences += text.lower().count(sentence.lower())
                        total_occurrences += occurrences

                        if occurrences > max_occurrences:
                            max_occurrences = occurrences
                            max_occurrences_page = page_num + 1

                if total_occurrences == 0:
                    print('Nothing was found')
                else:
                    print(f'How often I found the keywords/sentences: {total_occurrences}')
                    print(f'Most found on page {max_occurrences_page} with {max_occurrences} matches')
                print()

    except FileNotFoundError:
        print('Error: No folder found')

# Userinput
folder_path = input("Enter path: ")
sentences = ['Sentence/Keywords', 'Another Sentence/Keyword']

search_pdf_folder(folder_path, sentences)
