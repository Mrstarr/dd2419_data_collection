#!/usr/bin/env python

import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import rospy
import math
import os
import cv2
import PIL
from PIL import ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

class Data_GUI():

    def __init__(self,master):
        
        # set ros
        self.bridge = CvBridge()
        self.img_sub = rospy.Subscriber("/cf1/camera/image_raw", Image, self.feedback)

        # set gui
        self.master = master
        self.layout()

        # set path
        dir = os.path.dirname(os.path.dirname(__file__))
        self.path = os.path.join(dir,'dd2419_coco2')

    def layout(self):
        
        self.master.title("Data Collection GUI")
        
        self.panel = tk.Label(self.master)
        self.panel.pack()
        self.frame1 = tk.Frame(self.master, width=200, height=100, bg="white")
        self.frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frame2 = tk.Frame(self.master, width=100, bg="white")
        self.frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.label = tk.Label(master=self.frame1,text ='please enter file name :')
        self.label.pack()
        self.entry = tk.Entry(master=self.frame1)
        self.entry.pack()
        self.button = tk.Button(master = self.frame2,text='Save',width = 10,height = 2,bg='white',fg='black',command=self.save)
        self.button.pack()
        

    def feedback(self,data):
        """
        Feedback function for Image topic
        """

        try:
            self.img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        
        # convert te images to PIL format...
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(img)
        tkimg = ImageTk.PhotoImage(img)
        self.panel.config(image=tkimg)
        self.panel.tkimg = tkimg
        
        return None


    def save(self):
        filename = self.entry.get()
        suffix = '.jpg'
        file_path = os.path.join(self.path, filename + suffix)
        cv2.imwrite(file_path, self.img)
        '''
        '''

def main():
    rospy.init_node('yolo_detector', anonymous=True)
    rospy.loginfo("Data Collection Staring Working")

    root = tk.Tk()
    data_gui = Data_GUI(root)
    root.mainloop()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")


if __name__ == "__main__":
    main()

    
