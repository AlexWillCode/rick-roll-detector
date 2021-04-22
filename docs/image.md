# Image

You can scan an image file using the [verify_image](/api/#rick_roll_detectorverify_imageimage-numpyarray-true-or-none) function.

First let's import the necessary packages.
```python
import numpy
import PIL
from rick_roll_detector import verify_image
```

Now let's import your image and turn it into a numpy array.
```python
image = PIL.Image.open("YOUR_IMAGE_PATH")
image_array = numpy.array(image)
```

Now let's use the [verify_image](/api/#rick_roll_detectorverify_imageimage-numpyarray-true-or-none) function.
```python
if verify_image(image_array):
    print("The image is a Rick Roll!")
else:
    print("The image isn't a Rick Roll.")
```

Your final product should be:
```python
import numpy
import PIL
from rick_roll_detector import verify_image

image = PIL.Image.open("YOUR_IMAGE_PATH")
image_array = numpy.array(image)

if verify_image(image_array):
    print("The image is a Rick Roll!")
else:
    print("The image isn't a Rick Roll.")
```