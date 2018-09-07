import insta.config as cfg
import requests
import json
from pprint import pprint as pp
import web

def requestPics(userID):
    response = requests.get('https://www.instagram.com/graphql/query/',
                            headers=cfg.headers, params=cfg.getParamsPics(userID), cookies=cfg.cookies)
    json_data = json.loads(response.text)
    edges = json_data["data"]["user"]["edge_owner_to_timeline_media"]["edges"]

    if(json_data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]):
        print("Pics: has next page")

        end_cursor = json_data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
        edgesToAdd = requestPicsRecursiv(userID, end_cursor)
        for data in edgesToAdd:
            edges.append(data)

    print("Media Count: {}".format(len(edges)))
    return edges


def requestPicsRecursiv(userID, end_cursor):
    response = requests.get('https://www.instagram.com/graphql/query/', headers=cfg.headers,
                            params=cfg.getParamsPicsSecond(userID, end_cursor), cookies=cfg.cookies)
    json_data = json.loads(response.text)

    edges = json_data["data"]["user"]["edge_owner_to_timeline_media"]["edges"]

    if(json_data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]):
        print("Pics: has next page(rec)")

        end_cursor = json_data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
        edgesToAdd = requestPicsRecursiv(userID, end_cursor)
        for data in edgesToAdd:
            edges.append(data)
    return edges


def requestLikes(shortcode):
    print("Requesting Likes for: {}".format(shortcode))
    response = requests.get(cfg.url, headers=cfg.headers, params=cfg.getParamsFirst(
        shortcode), cookies=cfg.cookies)
    json_data = json.loads(response.text)
    edges = json_data["data"]["shortcode_media"]["edge_liked_by"]["edges"]

    # check next_page and recall requestLikes
    if(json_data["data"]["shortcode_media"]["edge_liked_by"]["page_info"]["has_next_page"]):
        print("Yesssssss: has next page")
        end_cursor = json_data["data"]["shortcode_media"]["edge_liked_by"]["page_info"]["end_cursor"]
        edgesToAdd = requestLikesRecursiv(shortcode, end_cursor)
        for data in edgesToAdd:
            edges.append(data)
    return edges


def requestLikesRecursiv(shortcode, end_cursor):
    response = requests.get(cfg.url, headers=cfg.headers, params=cfg.getParamsSecond(
        shortcode, end_cursor), cookies=cfg.cookies)
    json_data = json.loads(response.text)
    edges = json_data["data"]["shortcode_media"]["edge_liked_by"]["edges"]

    if(json_data["data"]["shortcode_media"]["edge_liked_by"]["page_info"]["has_next_page"]):
        print("Yesssssss: has next page (rec)")
        end_cursor = json_data["data"]["shortcode_media"]["edge_liked_by"]["page_info"]["end_cursor"]
        edgesToAdd = requestLikesRecursiv(shortcode, end_cursor)
        for data in edgesToAdd:
            edges.append(data)
    return edges


def extractLikes(listOfEdges):
    json_data = json.loads(listOfEdges)
    # offline use
    #data = open("data.txt").read()
    #json_data = json.loads(data)
    print(type(json_data))
    edges = json_data["data"]["shortcode_media"]["edge_liked_by"]["edges"]

    return edges


def requestAllFollower(userID):
    response = requests.get('https://www.instagram.com/graphql/query/',
                            headers=cfg.headers, params=cfg.getParamsFollower(userID), cookies=cfg.cookies)
    json_data = json.loads(response.text)
    edges = json_data["data"]["user"]["edge_followed_by"]["edges"]

    if(json_data["data"]["user"]["edge_followed_by"]["page_info"]["has_next_page"]):
        print("Follower: has next page")

        end_cursor = json_data["data"]["user"]["edge_followed_by"]["page_info"]["end_cursor"]
        edgesToAdd = requestAllFollowerRecursiv(userID, end_cursor)
        for data in edgesToAdd:
            edges.append(data)

    print("Follower Count: {}".format(len(edges)))
    web.statusUpdate("Follower Count: {}".format(len(edges)))
    return edges


def requestAllFollowerRecursiv(userID, end_cursor):
    response = requests.get('https://www.instagram.com/graphql/query/', headers=cfg.headers,
                            params=cfg.getParamsFollowerSecond(userID, end_cursor), cookies=cfg.cookies)
    json_data = json.loads(response.text)

    edges = json_data["data"]["user"]["edge_followed_by"]["edges"]

    if(json_data["data"]["user"]["edge_followed_by"]["page_info"]["has_next_page"]):
        print("Follower: has next page(rec)")

        end_cursor = json_data["data"]["user"]["edge_followed_by"]["page_info"]["end_cursor"]
        edgesToAdd = requestAllFollowerRecursiv(userID, end_cursor)
        for data in edgesToAdd:
            edges.append(data)

    return edges


def extractAllFollower(followerData):
    allFollower = {}
    for value in followerData:
        username = value["node"]["username"]
        allFollower[username] = 0
    return allFollower


def extractShortcodes(allPicData):
    shortcodeList = []
    for node in allPicData:
        shortcode = node["node"]["shortcode"]
        shortcodeList.append(shortcode)

    return shortcodeList


def addLikesToDict(dataDict, imageID):
    listOfEdges = requestLikes(imageID)
    dataDict[imageID] = listOfEdges
    return dataDict