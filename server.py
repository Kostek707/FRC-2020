from cscore import CameraServer, MjpegServer


# Import OpenCV and NumPy
import cv2
import numpy as np

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()
    
    MServer = MjpegServer(name='server', port=8000)

    # Capture from the first USB Camera on the system
    camera = cs.startAutomaticCapture(dev=0, return_server=True)
    camera.setResolution(320, 240)

    # Get a CvSink. This will capture images from the camera
    cvSink = cs.getVideo()

    # (optional) Setup a CvSource. This will send images back to the Dashboard
    outputStream = cs.putVideo("Name", 320, 240)

    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(240, 320, 3), dtype=np.uint8)
    cs.addServer(name='server', port=8000, server=MServer)

    while True:
        # Tell the CvSink to grab a frame from the camera and put it
        # in the source image.  If there is an error notify the output.
        time, img = cvSink.grabFrame(img)
        if time == 0:
            # Send the output the error.
            outputStream.notifyError(cvSink.getError());
            # skip the rest of the current iteration
            continue

        #
        # Insert your image processing logic here!
        #

        # (optional) send some image back to the dashboard
        server
        outputStream.putFrame(img)
