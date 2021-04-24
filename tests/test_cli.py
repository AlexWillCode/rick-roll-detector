from click.testing import CliRunner
from rick_roll_detector.cli import cli
from os import path

runner = CliRunner()

youtube_video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
image_path = f"{path.dirname(__file__)}/assets/test_image.jpg"
video_path = f"{path.dirname(__file__)}/assets/test_video.mov"


def test_youtube():
    response = runner.invoke(cli, ["--youtube", youtube_video_url])

    assert response.exit_code == 0
    assert "True" in response.output


def test_image():
    response = runner.invoke(cli, ["--image", image_path])

    assert response.exit_code == 0
    assert "True" in response.output


def test_video():
    response = runner.invoke(cli, ["--video", video_path])

    assert response.exit_code == 0
    assert "True" in response.output
