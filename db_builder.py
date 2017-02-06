from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')
#server = MongoClient('149.89.150.100')

db = server.g1mp5

c = db.students

p = open('peeps.csv','r')
peep = csv.DictReader(p)


for i in peep:
    doc = {}
    doc['name'] = i['name']
    doc['age'] = int(i['age'])
    doc['id'] = int(i['id'])
    g = open('courses.csv', 'r')
    grades = csv.DictReader(g)
    for j in grades:
        if i['id'] == j['id']:
            doc[j['code']] = j['mark']
    g.close()
    c.insert_one(doc)

p.close()
g.close()
