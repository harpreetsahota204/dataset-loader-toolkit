
from datasets import Dataset
import base64
from io import BytesIO
from PIL import Image
import os

def process_image(example):
    base64_string = example['image_base64_str']
    
    # Decode the base64 string
    image_data = base64.b64decode(base64_string)
    
    # Create a BytesIO object from the decoded data
    image_buffer = BytesIO(image_data)
    
    # Open the image using PIL
    image = Image.open(image_buffer)
    
    # Add the PIL image as a new feature
    example['image'] = image
    
    return example

# Assuming your dataset is named 'dataset'
dataset = dataset.map(process_image, num_proc=os.cpu_count())