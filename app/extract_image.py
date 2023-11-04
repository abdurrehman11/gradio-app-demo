from PIL import Image
from io import BytesIO
import fitz


def extract_images_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    images = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        img_list = page.get_images(full=True)

        for img_index, img in enumerate(img_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]
            pil_image = Image.open(BytesIO(image_data))
            images.append(pil_image)

    return images
