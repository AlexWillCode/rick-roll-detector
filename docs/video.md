# Video

You can scan a video file with the [verify_video](api.md#rick_roll_detectorverify_videocap-cv2videocapture-bool/) function.

First let's import the necessary packages.
```python
from rick_roll_detector import verify_video
import cv2
```

Now let's create a VideoCapture of your video file.
```python
video = cv2.VideoCapture("YOUR_VIDEO_PATH")
```

Lastly, let's use the [verify_video](api.md#rick_roll_detectorverify_videocap-cv2videocapture-bool/) function.
```python
if verify_video(video):
    print("The video is a Rick Roll!")
else:
    print("The video isn't a Rick Roll.")
```

Your final product should be:
```python
from rick_roll_detector import verify_video
import cv2

video = cv2.VideoCapture("YOUR_VIDEO_PATH")

if verify_video(video):
    print("The video is a Rick Roll!")
else:
    print("The video isn't a Rick Roll.")
```