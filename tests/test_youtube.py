from rick_roll_detector import verify_youtube_video


def test_youtube_video():
    assert verify_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") is True
