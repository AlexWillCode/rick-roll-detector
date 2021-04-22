from rick_roll_detector.image import verify_image
import cv2


# vid_cap has to be a cv2.VideoCapture()
def verify_video(vid_cap: cv2.VideoCapture) -> bool:
    success, image = vid_cap.read()
    while success:
        success, image = vid_cap.read()

        # If the video ended return false.
        if not success:
            vid_cap.release()
            return False

        # Return true if the frame contains Rick
        if verify_image(image):
            vid_cap.release()
            return True
