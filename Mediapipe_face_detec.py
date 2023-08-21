import cv2
import mediapipe as mp


class Mediapipe_face_detec:

    def __init__(self, videoCapture):
        self.videoCapture = videoCapture
        self.mp_face_detection = mp.solutions.face_detection
        # self.mp_drawing = mp.solutions.drawing_utils
        self.detect = False
        self.counter = 0

    # mp_face_detection = mp.solutions.face_detection
    # mp_drawing = mp.solutions.drawing_utils

    def detection(self):
        return self.detect

    def face_detec(self):
        # For webcam input:
        cap = cv2.VideoCapture(self.videoCapture)
        with self.mp_face_detection.FaceDetection(
                model_selection=0, min_detection_confidence=0.5) as face_detection:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    continue

                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = face_detection.process(image)
                if results.detections is not None:
                    self.counter = self.counter + 1
                else:
                    self.counter = 0
                if self.counter > 25:
                    self.detect = True
                else:
                    self.detect = False

                '''
              # Draw the face detection annotations on the image.
              image.flags.writeable = True
              image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
              if results.detections:
                  for detection in results.detections:
                      self.mp_drawing.draw_detection(image, detection)
                      
                '''
                # Flip the image horizontally for a selfie-view display.
                cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
                if cv2.waitKey(5) & 0xFF == 27:
                    break
        cap.release()


if __name__ == "__main__":
    object1 = Mediapipe_face_detec(0)
    object1.face_detec()
