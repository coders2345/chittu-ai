import cv2
import dlib
import numpy as np
import pyttsx3
import pickle
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Load pre-trained face detection model from dlib
detector = dlib.get_frontal_face_detector()

# Load pre-trained face landmark model from dlib
predictor_path = r"E:\PycharmProjects\chittu\shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

# Load pre-trained face recognition model from dlib
facerec_path = r"E:\PycharmProjects\chittu\dlib_face_recognition_resnet_model_v1.dat"
facerec = dlib.face_recognition_model_v1(facerec_path)

# File to load known face data
face_data_file = "known_faces_data.pkl"

def recognize_face():
    # Load known_faces_data from the file
    try:
        with open(face_data_file, 'rb') as file:
            known_faces_data = pickle.load(file)
    except FileNotFoundError:
        print("No face data found. Capture face data first.")
        return

    # Create a VideoCapture object (0 for default camera)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = detector(gray)

        for face in faces:
            # Get face landmarks
            shape = predictor(gray, face)

            # Get the face descriptor
            face_descriptor = facerec.compute_face_descriptor(frame, shape)

            # Compare with known faces
            for name, known_descriptor in known_faces_data.items():
                distance = np.linalg.norm(np.array(face_descriptor) - np.array(known_descriptor))

                # Set a threshold for face recognition (you may need to fine-tune this)
                if distance < 0.6:
                    if name.lower() == "basha":
                        # Use speak() here, not inside cv2.putText
                        speak("Hi Basha! Welcome, Chittu, your AI assistant.")
                        cv2.putText(frame, "Hi Basha! Welcome, Chittu, your AI assistant.", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    else:
                        cv2.putText(frame, f"Welcome, {name}!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                else:
                    # Use speak() here, not inside cv2.putText
                    speak("Unknown Person")
                    cv2.putText(frame, "Unknown Person", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            # Draw a rectangle around the face
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Recognition', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Uncomment the following line to recognize faces based on stored data
recognize_face()
