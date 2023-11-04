from transformers import CLIPModel, CLIPProcessor
from math import ceil
from PIL import Image
from extract_image import extract_images_from_pdf


# first run this file with just model and processor (line # 8 & 9) to download the data
# Or download the pretraind model and processor from huggingface and put them in 
# appropriate directory and then read from that directory
model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 430
IMG_TEXT_SIM_THRESH = 0.75


def get_image_grid(images):
    num_images = len(images)
    cols = ceil(num_images / 2)
    rows = (num_images + cols - 1) // cols

    # Create a new grid image with the desired size
    grid_width = cols * IMAGE_WIDTH
    grid_height = rows * IMAGE_HEIGHT
    grid = Image.new('RGB', size=(grid_width, grid_height), color='white')
    print(grid_width, grid_height)

    for i, img in enumerate(images):
        x = (i % cols) * IMAGE_WIDTH
        y = (i // cols) * IMAGE_HEIGHT
        img_resized = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.LANCZOS)
        grid.paste(img_resized, (x, y))

    return grid


def image_search(pdf_file, search_text):
    output_imgs, text = [], []

    search_text = search_text.strip().lower()
    images = extract_images_from_pdf(pdf_file)
    text.append(search_text)
    text.append("no " + search_text)

    inputs = processor(
        text=text,
        images=images,
        return_tensors="pt",
        padding=True
    )

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)
    print(probs)

    for i in range(probs.shape[0]):
        if probs[i, 0] > IMG_TEXT_SIM_THRESH:
            output_imgs.append(images[i])
            print(images[i].size)

    num_images = len(output_imgs)

    # if no image match to text
    if num_images == 0:
        num_images = 1
        output_imgs.append(Image.open("../data/no_image_available.png"))

    grid = get_image_grid(output_imgs)

    return grid
