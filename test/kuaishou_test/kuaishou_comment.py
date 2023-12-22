import requests

cookies = {
    'did': 'web_50a6d089a9d08c2e42ed768f997af787',
}

headers = {
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/short-video/3xfnpdmbyunumge',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

json_data = {
    'operationName': 'commentListQuery',
    'variables': {
        'photoId': '3xfnpdmbyunumge',
        'pcursor': '',
    },
    'query': 'query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      authorLiked\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        authorLiked\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
}

response = requests.post('https://www.kuaishou.com/graphql', cookies=cookies, headers=headers, json=json_data).text
print(response)