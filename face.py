import cv2
import numpy as np
import face_recognition
import math

imgAnar = face_recognition.load_image_file('images/anar1.jpeg')
imgAnar = cv2.cvtColor(imgAnar, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('images/anar2.jpeg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLocsAnar = face_recognition.face_locations(imgAnar)
for (top,right,bottom,left) in faceLocsAnar:
    cv2.rectangle(imgAnar, (left, top), (right, bottom), (255, 0, 255), 2)

encodeAnar = face_recognition.face_encodings(imgAnar)
if len(encodeAnar) == 0:
    print("No face")
    exit()
encodeAnar = encodeAnar[0]

faceLocsTest = face_recognition.face_locations(imgTest)
for (top, right, bottom, left) in faceLocsTest:
    cv2.rectangle(imgTest, (left, top), (right, bottom), (255, 0, 255), 2)

encodeTest = face_recognition.face_encodings(imgTest)
if len(encodeTest) == 0:
    print("No face")
    exit()
encodeTest = encodeTest[0]

results = face_recognition.compare_faces([encodeAnar], encodeTest)
face_distance = face_recognition.face_distance([encodeAnar], encodeTest)

print("Is it the same person? ", results[0])
print(f"Face distance: {face_distance[0]}")

cv2.imshow("Anar", imgAnar)
cv2.putText(imgTest, f'{results[0]} {round(face_distance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
cv2.imshow("Anar Test", imgTest)

cv2.waitKey(0)
cv2.destroyAllWindows()
