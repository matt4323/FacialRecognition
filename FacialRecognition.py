import os
import face_recognition
from PIL import Image


known_faces = []

# assign directory
knownDirectory = '/Users/matt/Desktop/Portfolio/FacialRecognitionProject/img/known'
 
# iterate over files in
# that directory
for filename in os.scandir(knownDirectory):
    img = face_recognition.load_image_file(filename.path)
    face_encoding = face_recognition.face_encodings(img)[0]
    known_faces.append((face_encoding, filename.name.split(".")[0], []))

unknownDirectory = "/Users/matt/Desktop/Portfolio/FacialRecognitionProject/img/Unkown"

for filename in os.scandir(unknownDirectory):
    img = face_recognition.load_image_file(filename.path)
    face_encodings = face_recognition.face_encodings(img)
    for face_encoding in face_encodings:
        for known_face in known_faces:
            results = face_recognition.compare_faces([known_face[0]], face_encoding)
            if results[0]:
                known_face[2].append(img)
                
parent_dir = "/Users/matt/Desktop/Portfolio/FacialRecognitionProject/results/"

for known_face in known_faces:
    path = os.path.join(parent_dir, known_face[1])
    os.mkdir(path)
    count = 0
    for image in known_face[2]:
        im = Image.fromarray(image)
        updatedPath = path + "/" + str(count) + ".jpg"
        im.save(updatedPath)
        count += 1
    
    
