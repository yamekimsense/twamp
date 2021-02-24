import os, time, datetime
from elasticsearch import Elasticsearch

es = Elasticsearch('192.168.235.196:9200')

while 1>0:

    result = os.popen('/Users/wansookim/PycharmProjects/680-twamp/twampy.py controller 192.168.30.253 | grep Round').read()
    print (result)
    result = result.split(":")[1]

    for i in range (0,11):
        result = result.replace ("  ", " ")

    result = result.split(" ")
    print (result)

    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    data = str(now) + " " + result[1] + " " +  result[2] +  " " + result[3] + " " + result[4] + " " + result[5]
    print (data)

    avg = float ( result[3].replace("ms","") )

    jit = result[4]


    if "us" in jit:
        jit = float(result[4].replace("us", "")) / 1000
        print (jit, type (jit))
    elif "ms" in jit:
        jit = float ( result[4].replace("ms","") )
        print (jit)

    los = float ( result[5].replace("%","").replace("\n","") )

    print (type (avg), avg)
    print (type (jit), jit)
    print (type (los), los)

    doc = {
     "latency_avg": avg,
     "jitter": jit,
     "loss": los,
     "time": now
    }

    es.index(index="twamp", doc_type="_doc", body=doc)

    time.sleep(10)
