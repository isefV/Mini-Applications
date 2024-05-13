import pathlib
# from PyPDF2 import PdfFileWriter, PdfFileReader
# import PyPDF2
# from PIL import Image
# import img2pdf
# import os
# import glob
# from fpdf import FPDF
import img2pdf
from PIL import Image
import os

def rename(image_folder):
    for file in os.listdir(image_folder):
        if file.endswith('.jpg'):
            name = file[:file.index('(')]
            counter = file [file.index('(')+1:-5]
            exten = file[-4:]
            if len(counter) != 3:
                counter = '0' * (3 - len(counter)) + counter
            os.rename(f"{image_folder}\\{file}", f"{image_folder}\\{name}-{counter}{exten}")

def convert_images_to_pdf(image_folder, output_pdf):
    image_name = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    image_file_name = []
    for filename in image_name:
        image_file_name.append(os.path.join(image_folder._str, filename))
    
    pdf_bytes = img2pdf.convert(image_file_name)
    with open(f"{output_pdf}.pdf",'wb') as file:
        file.write(pdf_bytes)

# dir_path = f"{pathlib.Path().resolve()}\\UnSeen\\"
dir_path = pathlib.Path("")
# rename(dir_path)

convert_images_to_pdf(dir_path, "")

# for folder in pathlib.Path(dir_path).iterdir():
#     # print(folder)
#     if folder.is_dir():
#         print(f"{folder._str.split(dir_path)[1][:20]}\t",end="")
#         try:
#             convert_images_to_pdf(folder, folder)
#         except:
#             print(f"|Faild|")
#         else:
#             print(f"|Done|")


