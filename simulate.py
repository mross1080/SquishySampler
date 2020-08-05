import os
import time

def sendPd(message=''):
    print(message)
    # os.system(str("echo '" + message + "' | /Applications/Pd-0.50-2.app/Contents/Resources/bin/pdsend 3001"))

    os.system(str("echo '" + message + "' | /Applications/Pd-0.50-2.app/Contents/Resources/bin/pdsend 3003"))
count = 0
while True:
    for x in range(13):
        sendPd("{} {};".format(x, count))
        count+=1
        time.sleep(.5)

    time.sleep(1)
