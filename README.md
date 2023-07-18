# TeslaFanController
A simple script that sets does fancontrolling based on nvidia cards.  
You need the following:  
-An NVIDIA driver that supports nvidia-smi  
-Case fans that are connected to a PWM port.  
  
The code main.py copy it to a folder that the systemd can read later (or clone this git there).  
Following make sure there are pwm file in any of the /sys/class/hwmon/ folders. For me they were in hwmon3  
Test the software first by running python main.py, make sure to install hddcontroller.  
Then copy the service (make sure to match the paths to the main.py and python script correctly):  
```sudo cp ./teslafans.service /lib/systemd/system/teslafans.service```  
Then reload the daemon and enable:
```sudo systemctl daemon-reload```  
```sudo systemctl enable teslafans.service```  
```sudo systemctl start teslafans.service```  

Thats it! Now to change the curves dig into the simple code of main.py and change things.

If you have suggestions or edits please create pull reqs. I am not planning on updating this frequently, but from time to time I will check.

For my current server rig I use very simple things in an sff case (I live in a small apt):
-Intel i3-10305
-Asrock H510M-ITX/AC
-32GB Corsair Vengence DDR4 3200
-NVIDIA Tesla K80 w/ 2 Corsair fans in the bottom of the case controlled by the Fan controller
-Coolermaster nr200p