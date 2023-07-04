import os, sys, glob
from hddfancontrol import Fan
import time as t

def check_curves(temp):
    if temp >= 30 and temp < 50:
        return 32
    elif temp >= 50 and temp < 60:
        return 124
    elif temp >= 65 and temp < 70:
        return 255

fan = [Fan(id=id, pwm_filepath=path.replace("_start",""), start_value=0, stop_value=255) for id, path in enumerate(glob.glob("/sys/class/hwmon/hwmon3/pwm*_start")) if 'pwm7' in path][0] # Get all the fans
# Fan pwm2 = cpu, pwm7 = Right Fan GPU (cuda 1), pwm1 = Left Fan GPU (cuda 0)

while True:
    temps = [int(line.split(":")[-1].split(" ")[1]) for line in os.popen('nvidia-smi -q -d temperature').read().split("\n") if 'GPU Current Temp' in line]
    print(temps, fan.getPwmValue(), end="\r")
    sys.stdout.flush()
    fan.setPwmValue(check_curves(max(temps)))
    t.sleep(0.25)

    
# for fan in fans:
#     fan.setPwmValue(124)