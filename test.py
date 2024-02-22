import pymongo
import datetime
import time

myclient = pymongo.MongoClient('mongodb+srv://nisamanee:passw0rd!@ct-pj-iot.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000')
mydb = myclient["Project"]
mycol = mydb["TEST"]

def toggle_temp():
    global temp_status
    if temp_status == 0:
        temp_status = 1
    else:
        temp_status = 0
    return temp_status

temp_status = 0

for i in range(1000):
    time_now = datetime.datetime.now()
    if i % 6 < 3:
        temp_status = 0
    else:
        temp_status = 1
        
    database_list = [
        {"Date_time": time_now, "Status": temp_status}
    ]
    x = mycol.insert_many(database_list)
    time.sleep(60)
