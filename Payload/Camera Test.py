import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

picam2 = Picamera2(0)    #change to 0 or 1 based on which port the camera is connected to
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder(10000000)

picam2.start_recording(encoder, '/home/ARC/Desktop/test.h264')
time.sleep(10)
picam2.stop_recording()