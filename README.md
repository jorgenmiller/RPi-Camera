# RPi-Camera  
How I use my [raspberry pi camera module V2](https://www.raspberrypi.org/products/camera-module-v2/)  
The docs are available  on [readthedocs.io](https://picamera.readthedocs.io/en/release-1.13/install.html)  

## Installation of Drivers  
Distribution of Raspbian come with this already installed. If you do not have the package, install it for python.  
`sudo apt-get update`  
`sudo apt-get install python-picamera python3-picamera`  

## Usage  
`from picamera import PiCamera`  
The typical instance of a camera is:  
`camera = PiCamera()`  
The PiCamera class has many attributes and methods 

## Attributes  
- `framerate`
- `resolution`
- ``

## Preview  
The preview function overlays the feed from the camera to an HDMI screen. This is useful to quickly test that the camera works and later can be used to line up shots or stream video.  



## Capture Images  


## Record Video  
