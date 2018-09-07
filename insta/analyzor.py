from pprint import pprint as pp
from operator import itemgetter


def likesPerPerson(dataDict, allFollower):
    for key in dataDict:
        for value in dataDict[key]:
            username = value["node"]["username"]
            if(username in allFollower):
                allFollower[username] = allFollower[username] + 1
            else:
                allFollower[username] = 1
    return allFollower


def zeroLikes(allFollower):
    zeroLikes = []
    print()
    print("People that do not like you! (Accounts that haven't liked a single picture)")
    i = 0
    for key in allFollower:
        if(allFollower[key] == 0):
            print(key)
            zeroLikes.append(key)
            i += 1
    return zeroLikes


def printSorted(allFollower):
    for k, v in sorted(allFollower.items(), key=itemgetter(1)):
        print (k, v)


def totalLikes(allFollower):
    i = 0
    for key in allFollower:
        i = i + allFollower[key]
    return i
