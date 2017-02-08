from pymongo import MongoClient

def compute(x):
    i = 0.0
    ans = 0.0
    for a in x:
        i += 1.0
        ans += int(a[1])
    return ans/i

    
def computeAverage():
    server = MongoClient('127.0.0.1')
    col = server.g1mp5.students
    c = col.find()
    averages = []
    ids = []
    names = []
    for a in c:
        averages.append( compute(a["courses"]) )
        ids.append([a["id"]])
        names.append([a["name"]])
    for i in range(len(averages)):
        print "Name: " + str(names[i][0])
        print  "ID: " + str(ids[i][0])
        print  "Average: "+str(averages[i])
        print "\n"

computeAverage()
