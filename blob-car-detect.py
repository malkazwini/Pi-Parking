from SimpleCV import *

import sys

if len(sys.argv) > 1:
  image_string = sys.argv[1]
else:
  image_string = "positive_images/screenshot_11-23_17:00"

car = Image(image_string)
no_car = Image("negative_images/screenshot_11-24_17:00")

# crop with full car & no back wall:
car = car.crop(170, 170, 230, 300)
no_car = no_car.crop(170, 170, 230, 300)

blobs = car.findBlobs(minsize=400, maxsize=100000)
for blob in blobs:
  blob.drawMinRect(color = Color.RED, width = 2)

car.show()

raw_input()

blobs = no_car.findBlobs(minsize=400, maxsize=100000)
for blob in blobs:
  blob.drawMinRect(color = Color.RED, width = 2)

no_car.show() 

raw_input()

#biggestArea = 0
#for blob in blobs:
#  if blob.area() > biggestArea:
#    biggestArea = blob.area()
#    biggestBlob = blob
#
#lowestPoint = 0
#for points in biggestBlob.minRect():
#  if points[1] > lowestPoint:
#    lowestPoint = points[1]
#
#print "Image " + image_string + " has " + str(lowestPoint) + " lowest point"

#raw_input()
