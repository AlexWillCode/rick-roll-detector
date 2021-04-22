import face_recognition
import numpy
import rick_roll_detector
import os

# Get training image.
rick_image_path = f"{os.path.dirname(rick_roll_detector.__file__)}/assets/training.jpg"
rick_image = face_recognition.load_image_file(rick_image_path)

# Import training image and get face encoding.
rick_encoding = face_recognition.face_encodings(numpy.array(rick_image))[0]


# Image has to be a numpy array.
def verify_image(image: numpy.array) -> bool:
    # Get image face encodings.
    unknown_encoding = face_recognition.face_encodings(image)

    try:
        # Loop through the faces found in the image. If one or more matches Rick's encoding return true.
        for face in unknown_encoding:
            if face_recognition.compare_faces([rick_encoding], face)[0]:
                return True

    except IndexError:
        # If there aren't any faces pass.
        pass

    return False
