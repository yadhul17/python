import pymongo
from urllib.parse import quote_plus
username='yadhul'
password='yadhul@2005'
q_password=quote_plus(password)
uri=f'mongodb+srv://{username}:{q_password}@cluster0.uvmgcab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
myclient=pymongo.MongoClient(uri)
mydb=myclient['tata']
mycol=mydb['emp']
# data=[{'anme':'athul','age':42},{'name':'arjun','age':34},{'name':'anay','age':54}]
# result=mycol.insert_many(data)
# result=mycol.find()
# for i in result:
#     print(i)

mydata = mycol.find({'age': {'$lt': 18}})
for j in mydata:
    print(j)
    

