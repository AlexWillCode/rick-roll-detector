# Youtube

You can scan a Youtube video with the [verify_youtube_video](api.md#rick_roll_detectorverify_youtube_videourl-str-bool) function.

First let's import the necessary package.
```python
from rick_roll_detector import verify_youtube_video
```

Then we should create a video_url variable.
```python
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Finally, let's use the [verify_youtube_video](api.md#rick_roll_detectorverify_youtube_videourl-str-bool) function.
```python
if verify_youtube_video(video_url):
    print("The video is a Rick Roll!")
else:
    print("The video isn't a Rick Roll.")
```

Your final product should be:
```python
from rick_roll_detector import verify_youtube_video

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

if verify_youtube_video(video_url):
    print("The video is a Rick Roll!")
else:
    print("The video isn't a Rick Roll.")
```