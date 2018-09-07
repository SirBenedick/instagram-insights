import requests
import insta.config as cfg
import json


def retriveUserID(username):
    import requests
    url = 'https://www.instagram.com/{}/'.format(username)
    response = requests.get(url, headers=cfg.headers,
                            params=cfg.paramsUserID, cookies=cfg.cookies)
    try:
        json_data = json.loads(response.text)
    except ValueError:
        print("Username '{}' not found!".format(username))
        exit()

    userID = json_data["graphql"]["user"]["id"]
    return userID
