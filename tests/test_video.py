from rick_roll_detector import verify_video
from cv2 import VideoCapture
from os import path


def test_video():
    video_path = f"{path.dirname(__file__)}/assets/test_video.mov"
    video_capture = VideoCapture(video_path)

    assert verify_video(video_capture) is True
