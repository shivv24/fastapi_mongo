from pymongo import MongoClient

client=MongoClient("mongodb+srv://<username>:<password>@cluster0.1sd4pyy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client.todo_db

collection_name=db["todo_collection"]
