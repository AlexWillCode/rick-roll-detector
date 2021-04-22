from rick_roll_detector import verify_image
from numpy import array
from PIL import Image
from os import path


def test_image():
    image_path = f"{path.dirname(__file__)}/assets/test_image.jpg"
    image = Image.open(image_path)
    image_array = array(image)

    assert verify_image(image_array) is True
