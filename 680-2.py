import os, time
from datetime import datetime

while 1>0:

    now = datetime.now()

    #result = os.popen('ls -al').read()

    result = os.popen('/Users/wansookim/PycharmProjects/680-twamp/twampy.py controller 192.168.30.253 | grep Round').read()

    result = result.split(":")[1]

    #print ("1st", result)

    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")
    result = result.replace ("  ", " ")

    #print ("2nd", result)

    result = result.split(" ")

    #print (result[0])
    #print ( now, result[1], result[2], result[3], result[4], result[5].strip("\n") )
    data = str(now) + " " + result[1] + " " +  result[2] +  " " + result[3] + " " + result[4] + " " + result[5]
    print (data)

    f = open ("result.txt", 'a')
    f.write (data)
    f.close()

    time.sleep(10)