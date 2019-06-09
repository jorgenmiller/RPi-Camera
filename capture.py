from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)

camera.start_preview()
camera.annotate_text = "Taken by RPi Camera Module V2"
sleep(2)
camera.capture('image.jpg')
camera.stop_preview()
