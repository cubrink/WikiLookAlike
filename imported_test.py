from PIL import Image
import face_recognition


image = face_recognition.load_image_file("family.jpeg")



# Find all the faces in the image using the default HOG-based model.

# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.

# See also: find_faces_in_picture_cnn.py

face_locations = face_recognition.face_locations(image)

faces = []
isize = []



print("I found {} face(s) in this photograph.".format(len(face_locations)))



for face_location in face_locations:



    # Print the location of each face in this image





    top, right, bottom, left = face_location

    print(

        "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(

            top, left, bottom, right

        )

    )



    face_size = (bottom - top) * (right - left)

    isize.append(face_size)




    # You can access the actual face itself like this:

    face_image = image[top:bottom, left:right]

    pil_image = Image.fromarray(face_image)

    faces.append(pil_image)
  
largest = 0
i = 0

for item in isize:
  if item > largest:
    largest = item
    indexing_num = i
  i += 1

print(str(largest))

faces[i-1].save("tmp.jpg")

prelim = face_recognition.load_image_file("tmp.jpg")
my_face_encoding = face_recognition.face_encodings(prelim)[0]


pil_image.show(faces[i-1])

print("The size of the face is: " + str(largest) + " pixels")

print("The encoding is: " + str(my_face_encoding))




