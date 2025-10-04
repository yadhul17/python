import pymongo
from urllib.parse import quote_plus
username='yadhul'
password='yadhul@2005'
q_password=quote_plus(password)
uri=f'mongodb+srv://{username}:{q_password}@cluster0.uvmgcab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
myclient=pymongo.MongoClient(uri)
print(myclient)
mydb=myclient['company']
mycol=mydb['student']
data=[{'name':'yadhu','address':'thrissur','age':12,'class':4},{'name':'arun','address':'aalapy','age':20,'class':5},{'name':'arjun','address':'ekm','age':23,'class':8}]
result = mycol.insert_many(data)  # This will insert all
print(result)



