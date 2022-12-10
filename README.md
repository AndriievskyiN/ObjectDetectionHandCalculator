# Object Detection Finger Calculator

The goal of this project is to make and deploy an object detection model that can recognize different amount of fingers on a hand. Moreover, it can recognize + and - signs demonstrated using fingers. It will write the expression that you showed (e.g. 5 + 3 + 2 - 1), and then you will be able to calculate the result.

The detection part will be done in two steps:
1. Hand localization - find the hand in the frame, add a box aroudn it, crop the image to just the box with the hand.

2. Classification - based on the cropped image classify what number or sign is shown.
