
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello and welcome to my <u>Django App</u> project!</h1>")

import pymongo

client = pymongo.MongoClient('mongodb+srv://username:password@HOSTNAME/DATABASE_NAME?authSource=admin&tls=true&tlsCAFile=<PATH_TO_CA_FILE>')

#Define Db Name
dbname = client['first_db']

#Define Collection
collection = dbname['person']

person_1={
    "name": "Jonas Jones",
    "age" : 35
}

collection.insert_one(person_1)

person_details = collection.find({})

for r in person_details:
    print(r['name'])