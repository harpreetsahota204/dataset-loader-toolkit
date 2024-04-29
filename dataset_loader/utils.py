from datasets import Dataset
import base64
from io import BytesIO
from PIL import Image
import os

def convert_base_64_to_image(example):
    """
    Process an image example by decoding the base64 string and creating a PIL image.

    Args:
        example (dict): A dictionary containing the image example data.
            - 'image_base64_str' (str): The base64-encoded string of the image.

    Returns:
        dict: The updated example dictionary with the decoded PIL image added as a new feature.
            - 'image' (PIL.Image): The decoded PIL image.
    """
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
