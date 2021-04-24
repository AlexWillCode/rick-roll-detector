import click
import rick_roll_detector
import os
import PIL
import numpy
import imghdr
import cv2


@click.command()
@click.option("--image", "-i", required=False, type=str, help="Scans an image for a Rick Roll.")
@click.option("--video", "-v", required=False, type=str, help="Scans a video file for a Rick Roll.")
@click.option("--youtube", "-y", required=False, type=str, help="Scans a Youtube video for a Rick Roll.")
def cli(image, video, youtube):
    # If no options are given
    if all(v is None for v in [image, video, youtube]):
        click.echo("No options were given.")
        return

    # Youtube video scanning
    if youtube:
        result = rick_roll_detector.verify_youtube_video(youtube)
        click.echo(f"{youtube} = {result}")

    # Video file scanning
    if video:
        # If the file doesn't exist
        if not os.path.exists(video):
            click.echo(f"'{video}' does not exist!")
            return

        video_capture = cv2.VideoCapture(video)
        result = rick_roll_detector.verify_video(video_capture)

        click.echo(f"{video} = {result}")

    # Image file scanning
    if image:
        # If the file doesn't exist
        if not os.path.exists(image):
            click.echo(f"'{image}' does not exist!")
            return

        # If the file is not an image
        if not imghdr.what(image):
            click.echo(f"'{image}' is not an image.")
            return

        image_object = PIL.Image.open(image)
        image_array = numpy.array(image_object)
        result = rick_roll_detector.verify_image(image_array)

        click.echo(f"{image} = {result}")
