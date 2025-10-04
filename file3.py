import pymongo
from urllib.parse import quote_plus
username='yadhul'
password='yadhul@2005'
q_password=quote_plus(password)
uri=f'mongodb+srv://{username}:{q_password}@cluster0.uvmgcab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
myclient=pymongo.MongoClient(uri)
# print(myclient)
mydb=myclient['company']
mycol=mydb['employe']
# data=[{'name':'athul','address':'thrissur','age':12,'class':4},{'name':'alan','address':'aalapy','age':20,'class':5},{'name':'achu','address':'ekm','age':23,'class':8}]
# result = mycol.insert_many(data)
# x=mycol.find_one() used to 
# print(x)
# for i in mycol.find():
#     print(i)
# mydata=mycol.find({'class':{'$gt':18}}) 
# doc=list(mydata)
# if  not doc:
#     print("no curosponding data")
# else:
#     for i in mydata:
#         print(i)
# mydata=mycol.find().sort('name',-1)  #print in sorted order
# for i in mydata:
#     print(i)
# myqry={'address':'aalapy'}
# newvalue={'$set':{'name':'anadhu'}}
# mycol.update_one(myqry,newvalue)

# myq={'address':'thrissur'}
# nvalue={'$set':{'age':65,'class':12}}
# for x in mycol.find():
#     print(x)

# myqry={'address':'thrissur'}
# mycol.delete_one(myqry)
# for i in mycol.find():
#     print(i)

myqry={'age':23}
mycol.delete_many(myqry)
for i in mycol.find():
    print(i)

