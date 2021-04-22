from setuptools import setup

__version__ = "1.0.0"
__license__ = "MIT"

DESCRIPTION = "A Python package that detects if an image, video, or Youtube video is a Rick Roll."
CLASSIFIERS = [
    "Programming Language :: Python :: 3"
]


setup(
    name="rick_roll_detector",
    version=__version__,
    description=DESCRIPTION,
    url="https://github.com/alexwillcode/rick-roll-detector/",
    author="AlexWillCode",
    author_email="alexwillcode@gmail.com",
    license=__license__,
    classifiers=CLASSIFIERS,
    packages=["rick_roll_detector"],
    include_package_data=True,
    install_requires=[
        "face-recognition",
        "opencv-python",
        "youtube-dl",
        "pafy",
        "pillow",
        "numpy"
    ]
)
