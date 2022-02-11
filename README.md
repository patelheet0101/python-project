# Project Introduction

I am going to demonstrate a machine learning project of gesture movement 
detection using opencv library 

Aim :  To perform any task when it detects any kind of movement of hands

Input : We clap our hands in froont of webcam

Output : Any song is played


# Project Description 

Step 1 :

Install necessary libraries :

pip install cv2
pip install pyaudio
pip install cvzone


Step 2 :

Capturing an webcam in your device using VideoCapture()


Step 3 :

Allow no of hands that it can capture in  a webcam 

Display the attributes of Hands like Landmarks, centrepoints, width and height and handtype


Step 4 :

This is a most important step where we have to map the distance between 2 centre points of Hands 

Decide any value 'k' of a certain distance upto which it can detect centrepoints

if centrepoints < k
  play any music from your folder
else
  continue the loop


Step 5 :

Compile and Run the program . 

Clap your hands in front of webcam and you will be able to listen any song from your device 
