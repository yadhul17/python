import pymongo
from urllib.parse import quote_plus

username='yadhul'
password='yadhul@2005'

q_password=quote_plus(password)
uri=f'mongodb+srv://{username}:{q_password}@cluster0.uvmgcab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
myclient=pymongo.MongoClient(uri)
print(myclient)

mydb=myclient['newdb']
mycol=mydb['new']     
data={'name':'yadhul','address':'trissur'}
x=mycol.insert_one(data)


# mongodb+srv://yadhul:yadhul@2005@cluster0.uvmgcab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0