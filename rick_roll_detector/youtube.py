import cv2
import pafy
from rick_roll_detector.video import verify_video


def verify_youtube_video(url: str) -> bool:
    pafy_video = pafy.new(url)
    play = pafy_video.getbest(preftype="mp4")

    cap = cv2.VideoCapture(play.url)
    return verify_video(cap)
