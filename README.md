## ⚠️ Attention: Deprecated
This repository is no longer maintained. The original README is below.

<p align="center"><a href="https://github.com/alexwillcode/rick-roll-detector"><img src="logo/triangle/logo_triangle_256.png" height="150"/></a></p>

<h1 align="center">rick-roll-detector</h1>

<p align="center">Rick Roll Detection using Facial Recognition</p>

<p align="center">
    <img src="https://github.com/alexwillcode/rick-roll-detector/workflows/Deploy%20Docs/badge.svg"/>
    <img src="https://github.com/alexwillcode/rick-roll-detector/workflows/Upload%20Python%20Package/badge.svg"/>
    <img src="https://github.com/alexwillcode/rick-roll-detector/workflows/Python%20package/badge.svg"/>
</p>

## 💭 What is it?
[rick-roll-detector](https://alexwillcode.github.io/rick-roll-detector/) is a Python package that uses facial recognition to detect if an image, video, or Youtube video is a Rick Roll.

## ⚡️ Fast implementation
**Step 1**: Install rick-roll-detector with PIP:
```
pip3 install rick-roll-detector
```

**Step 2**: Use of all of the CLI and Python commands are explained here https://alexwillcode.github.io/rick-roll-detector/.

## 🎉 Examples

### Python
```python
from rick_roll_detector import verify_youtube_video

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

if verify_youtube_video(video_url):
    print("The video is a Rick Roll!")
else:
    print("The video isn't a Rick Roll.")
```

### Command Line
```
rick-roll-detector --youtube "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```
