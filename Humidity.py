import pymongo
import datetime
import time
import random
myclient = pymongo.MongoClient('mongodb+srv://nisamanee:passw0rd!@ct-pj-iot.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000')
mydb = myclient["Project"]
mycol = mydb["Humidity"]
 
def random_temp_int():
    random_num = random.randint(40, 60)
    return random_num
 
for i in range(1000):
   
    # time_now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    time_now = datetime.datetime.now()
    # print(time_now)
 
 
    database_list = [
    {"Date_time": time_now,"Status": random_temp_int()}
    ]
   
    x = mycol.insert_many(database_list)
    time.sleep(60)
 
    if i == 10:
        break
 
 
 
