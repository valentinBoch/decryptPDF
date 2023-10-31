import os
import yaml
from PyPDF2 import PdfReader, PdfWriter

# Importing the configuration file
config = yaml.safe_load(open("config.yml"))

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
    file = open(input_file, mode='rb')
    reader = PdfReader(file)

    # Check that the PDF contains a password
    if reader.is_encrypted:
        reader.decrypt(password)

        writer = PdfWriter()
        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])

        pdf = list(pdf)
        pdf = ''.join(pdf)
        output = open(path_dest+'/'+str(pdf), 'wb')
        writer.write(output)
        print(f'The file {str(pdf)} is saved without password in {path_dest}')
        file.close()
    else:
        print(f"The file {str(pdf)} does not contain a password")
