url = 'https://www.instagram.com/graphql/query/'

cookies = {
    'ig_cb': '',
    'rur': '',
    'mcd': '',
    'mid': '',
    'csrftoken': '',
    'ds_user_id': '',
    'sessionid': '',
    'urlgen': '',
}


headers = {
    'Cache-Control': '',
    'Postman-Token': '',
    'accept': '',
    'accept-encoding': '',
    'accept-language': '',
    'authority': 'www.instagram.com',
    'cookie': '',
    'referer': '',
    'user-agent': '',
    'x-instagram-gis': '',
    'x-requested-with': '',
}


def getParamsFirst(shortcode):
    params = [
        ['query_hash', 'e0f59e4a1c8d78d0161873bc2ee7ec44'],
        ['variables', '{{"shortcode":"{}","include_reel":true,"first":30}}'.format(
            shortcode)],
    ]
    return params


def getParamsSecond(shortcode, end_cursor):
    params = [
        ['query_hash', 'e0f59e4a1c8d78d0161873bc2ee7ec44'],
        ['variables', '{{"shortcode":"{}","include_reel":true,"first":30,"after":"{}"}}'.format(
            shortcode, end_cursor)],
    ]
    return params


def getParamsPics(userID):
    params = [
        ['query_hash', 'a5164aed103f24b03e7b7747a2d94e3c'],
        ['variables', '{{"id":"{}","first":24}}'.format(
            userID)],
    ]
    return params


def getParamsPicsSecond(userID, end_cursor):
    params = [
        ['query_hash', 'a5164aed103f24b03e7b7747a2d94e3c'],
        ['variables', '{{"id":"{}","first":24,"after":"{}"}}'.format(
            userID, end_cursor)],
    ]
    return params


def getParamsFollower(userID):
    params = [
        ['query_hash', '56066f031e6239f35a904ac20c9f37d9'],
        ['variables', '{{"id":"{}","include_reel":false,"fetch_mutual":false,"first":24}}'.format(
            userID)],
    ]
    return params


def getParamsFollowerSecond(userID, end_cursor):
    params = [
        ['query_hash', '56066f031e6239f35a904ac20c9f37d9'],
        ['variables', '{{"id":"{}","include_reel":false,"fetch_mutual":false,"first":24,"after":"{}"}}'.format(
            userID, end_cursor)],
    ]
    return params


paramsUserID = (
    ('__a', '1'),
)
