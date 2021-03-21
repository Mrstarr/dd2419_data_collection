# dd2419_data_collection
Simple GUI to record camera data

# Prerequisites

- Rospy
- Tkinter

# Installing
### Install ros package
```

$ git clone -b detection https://github.com/tjr16/dd2419_detector_baseline.git
```
Extract all the files from `dd2419_detector_baseline` to `perception`
```
$ mkdir build
```

### Install opencv <for feature detection, not implemented yet>
```
$ To be filled
```
# Running
### Increase functionality of CPU
You can type the following line to check current CPU Running frequency:
```
grep MHz /proc/cpuinfo
```
If it's largely below the standard frequency the product is said to be, probably check if you PC is on powersave mode:
https://askubuntu.com/questions/929884/how-to-set-performance-instead-of-powersave-as-default
```
sudo systemctl restart cpufrequtils
```
Above line is just for convenience for me.
### Get ros node started
```
$ rosrun perception yolo_detector.py
```

### Check message information
```
$ rosmsg info perception/Sign
$ rosmsg info perception/SignArray
```
### Check rostopic 
```
$ rostopic echo sign/detected
```
The echoing information should be of type SignArray which refers to an array of the signs it is detected currently, empty if no detection found
