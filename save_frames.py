import cv2
import os

file = '/local/mnt/workspace/chris/projects/udacity/CarND-Vehicle-Detection/project_video.mp4'
assert os.path.isfile(file)
vidcap = cv2.VideoCapture(file)
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  if count %10 == 0:
	  print('Read a new frame: ', success)
	  if success:
	  	cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1