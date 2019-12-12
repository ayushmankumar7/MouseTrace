#1366 * 768
import cv2 
import numpy as np
import time
from pynput.mouse import Listener, Controller
import argparse 
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--t', type=int, default=10, help="Time the Program has to Run. Default 10")  # Argument accepted here

arg = parser.parse_args()
t = arg.t
print("Time Given = ",t)


m = Controller()
def scaleDown(x, y):
    
    return((x/1366 * 640), (y/768*480))

img = np.zeros((480, 640, 3))
def on_move(x,y):
    print(f"Position : {scaleDown(x,y)}")
    global img
    m,n = scaleDown(x,y)
    img = cv2.circle(img,(int(m),int(n)) , 2, (0,255,0), 2)     
    cv2.imshow('img', img)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()



def on_click(x,y,button, pressed):
    if pressed:
        Listener.stop()

m.position = (1366/2 , 768/2)

print(scaleDown(1366, 768))


l = Listener(on_move = on_move)
l.start()
time.sleep(t)  # Argument is used here
l.stop()
l.join()

if not l.isAlive():
    print("Monitoring Stopped")