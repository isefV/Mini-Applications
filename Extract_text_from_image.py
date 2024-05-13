from PIL import Image
import pytesseract
import os 
# import textract
# from google.cloud import vision

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
def extract_text_from_image_pytesseract(image_path):
    try:
        # Open an image using PIL
        with Image.open(image_path) as img:
            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        return f"An error occurred: {e}"


# def extract_text_from_image_textract(image,path):
#     try:
#         # Use textract to extract text from the image
#         extracted_text = textract.process(f"{path}\\{image}")
#         # extracted_text = textract.process(image, method='tesseract',method='tesseract', encoding='utf-8',path=f'{path}')
#         return extracted_text.decode('utf-8')  # Decode bytes to string
#     except Exception as e:
#         return f"An error occurred: {e}"



# Set up credentials and authenticate with Google Cloud Vision API
# def extract_text_from_image_google(image_path):
#     client = vision.ImageAnnotatorClient()
#     # Load image file
#     with open(f'{image_path}.jpg', 'rb') as image_file:
#         content = image_file.read()
#     image = vision.Image(content=content)
#     # Perform OCR on the image
#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     paragraph = ""
#     for text in texts:
#         paragraph += text.description + '\n'
#     return paragraph


file_path = "F:\\WT-App\\Desktop.P\\1\\Designs Projects\\Code Proj\\Web Scraping\\Mangas\\Part-0"
file_name = ""
path = f"{file_path}\\{file_name}"
with open(f"{path}.txt",'w',encoding="utf-8") as file:
    counter = 1
    for image in os.listdir(path):
        if image.endswith('.jpg'):
            file.write(f"\n{image.upper()[:-8]} {counter}: \n")
            counter += 1
            # image_text = extract_text_from_image_google(f"{path}\\{image}")
            # image_text = extract_text_from_image_textract(image,path)
            image_text = extract_text_from_image_pytesseract(f"{path}\\{image}")
            image_text = image_text.split()
            image_text = ' '.join(image_text)
            # temp_text = ""
            # for token in image_text:
            #     temp_text += f" {token}"
            file.write(f'{image_text.lower()}\n')

print("SUC")
























# import easyocr

# def extract_text_from_image(image_path):
#     reader = easyocr.Reader(['en'])  # Specify the language(s) you want to detect

#     try:
#         result = reader.readtext(image_path)
#         extracted_text = '\n'.join([text[1] for text in result])
#         return extracted_text
#     except Exception as e:
#         return f"An error occurred: {e}"

# # Replace 'image_path' with the path to your image file
# image_text = extract_text_from_image('image_path.jpg')
# print(image_text)
