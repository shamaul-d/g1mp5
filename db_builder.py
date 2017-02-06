from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')
#server = MongoClient('149.89.150.100')

db = server.g1mp5

c = db.students

p = open('peeps.csv','r')
peep = csv.DictReader(p)

g = open('courses.csv', 'r')
grades = csv.DictReader(g)

for i in peep:
    doc = {}
    doc['name'] = i['name']
    doc['age'] = int(i['age'])
    doc['id'] = int(i['id'])
    for j in grades:
        if doc['id'] == int(j['id']):
            doc[j['code']] = j['mark']
    c.insert_one(doc)

peep.close()
grades.close()
