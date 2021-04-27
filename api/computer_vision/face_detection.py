import cv2
from base64 import b64decode, b64encode
import io



from PIL import Image



def face_detection(p):
   # initialize front face classifier
   cascade = cv2.CascadeClassifier("api/computer_vision/assets/haarcascade_frontalface_default.xml")

   bytes = bytearray(b64decode(p))
   image = Image.open(io.BytesIO(bytes))
   image.save('api/computer_vision/assets/photo.png')
   frame = cv2.imread("api/computer_vision/assets/photo.png")
   #frame = cv2.img(Image.open(io.BytesIO(bytes)))

   # Convert to black-and-white
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   blackwhite = cv2.equalizeHist(gray)
   rects = cascade.detectMultiScale(
      blackwhite, scaleFactor=1.1, minNeighbors=3, minSize=(1, 1),
      flags=cv2.CASCADE_SCALE_IMAGE)
   for x, y, w, h in rects:
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

   cv2.imwrite('api/computer_vision/outputs/faces.png', frame)

   with open(str('api/computer_vision/outputs/faces.png'), 'rb') as open_file:
      byte_content = open_file.read()
   base64_bytes = b64encode(byte_content)

   return {"photo_b64": base64_bytes}






