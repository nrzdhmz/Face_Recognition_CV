import cv2
import face_recognition

base_image = face_recognition.load_image_file('images/hamza.jpeg')
base_encoding = face_recognition.face_encodings(base_image)[0]

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  if not ret:
    break

  small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
  rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

  face_locations = face_recognition.face_locations(rgb_small_frame)
  face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

  for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    top *= 4
    right *= 4
    bottom *= 4
    left *= 4

    matches = face_recognition.compare_faces([base_encoding], face_encoding)
    face_distance = face_recognition.face_distance([base_encoding], face_encoding)

    if matches[0]:
      label = "You are Hamza"
      color = (0, 255, 0)
    else:
      label = "You are Not Hamza"
      color = (0, 0, 255)

    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    cv2.putText(frame, f'{label} {round(face_distance[0], 2)}', (left, top - 10),
      cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

  cv2.imshow('Say my Name', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
