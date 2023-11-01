import os
import yaml
from PyPDF2 import PdfReader, PdfWriter

# Importing the configuration file
with open("config.yml", 'rb') as file:
    config = yaml.safe_load(file)

# variable
path_source = config['data']['path_source']
path_dest = config['data']['path_dest']
password = config['data']['password']
pdfs = []

# Retrieving *.pdf files
for files in os.listdir(path_source):
    if files.endswith(".pdf"):
        pdfs += [files]

for pdf in pdfs:
    input_file = os.path.join(path_source, pdf)
    with open(input_file, mode='rb') as file:
        reader = PdfReader(file)

        # Check that the PDF contains a password
        if reader.is_encrypted:
            reader.decrypt(password)

            writer = PdfWriter()
            for i, item in enumerate(reader.pages):
                writer.add_page(reader.pages[i])

            pdf = list(pdf)
            pdf = ''.join(pdf)
            with open(path_dest+'/'+str(pdf), 'wb') as output:
                writer.write(output)

            print(
                f'The file {str(pdf)} is saved without password in {path_dest}')
        else:
            print(f"The file {str(pdf)} does not contain a password")
