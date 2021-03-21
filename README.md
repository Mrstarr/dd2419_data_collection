# dd2419_data_collection
Simple GUI to record camera data:
<p align="left">
  <img src="./dd2419_coco2/demo.jpg" width="450">
</p>

## Prerequisites

- Rospy
- Tkinter

## Installing
Under `~\dd2419_ws\src`
```
$ git clone https://github.com/Mrstarr/dd2419_data_collection.git
$ mkdir build
```

## Running
After base launching and power up the drone, run:
```
$ rosrun data_collection gui.py
```
Once click `save`, the current record of camera data will be saved.
