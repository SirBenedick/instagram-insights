import insta.config as cfg
import insta.extractor as ex
import insta.analyzor as ana
import insta.login as login
from pprint import pprint as pp
import numpy as np
from operator import itemgetter
import web

dataDict = {}


def addLikesToDict(imageID):
    listOfEdges = ex.requestLikes(imageID)

    dataDict[imageID] = listOfEdges


# MAIN
# get User ID
def fakeFriends(username):
    username = username
    userID = login.retriveUserID(username)
    print("{}: {}".format(username, userID))
    web.statusUpdate("UserID: ".format(userID))
    print("ff")
    web.statusUpdate("Extracting Data")

    # extract data
    web.statusUpdate("Retriving Follower Data ")
    followerData = ex.requestAllFollower(userID)

    web.statusUpdate("Extracting all Follower ")
    allFollower = ex.extractAllFollower(followerData)

    web.statusUpdate("Retriving Picture  Data ")
    allPicData = ex.requestPics(userID)

    web.statusUpdate("Extracting all Pictures ")
    shortcodeList = ex.extractShortcodes(allPicData)
    web.statusUpdate("Pictures found: {}".format(len(shortcodeList)))

    for count, imageID in enumerate(shortcodeList):
        print("{}/{}: ".format(count, len(shortcodeList)))
        web.statusUpdate(
            "{}/{} Images scanned ".format(count+1, len(shortcodeList)))
        addLikesToDict(imageID)

    # ANALYZING
    web.statusUpdate("Analyzing data")
    print("\n\nAnalyzing Data")
    allFollower = ana.likesPerPerson(dataDict, allFollower)
    zeroLikes = ana.zeroLikes(allFollower)
    web.statusUpdate("Done")
    return zeroLikes
