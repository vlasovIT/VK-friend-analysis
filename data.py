from settings import *
from log import *
from api_request import ApiMethodRequest


def user_analysis(users, userId):
    likes = {}
    for user in users:
        if userId in user["fans"]:
            likes[user["id"]] = user["fans"][userId]

    return likes


def get_likes(post, user_fans):
    error = check_is_error("likes.getList", {
        "type": "post",
        "owner_id": post["owner_id"],
        "item_id": post["id"],
        "friends_only": 1,
        "skip_own": 1
    }, "5.21")

    if not error:
        post_likes = get_data("likes.getList", {
            "type": "post",
            "owner_id": post["owner_id"],
            "item_id": post["id"],
            "friends_only": 1,
            "skip_own": 1
        }, "5.21")

        for user_like in post_likes["items"]:
            if user_like in user_fans:
                user_fans[user_like] += 1
            else:
                user_fans[user_like] = 1

    return user_fans


def get_comments(post, user_fans, friends):
    error = check_is_error("wall.getComments", {
        "owner_id": post["owner_id"],
        "post_id": post["id"]
    }, "5.21")

    if not error:
        post_comments = get_data("wall.getComments", {
            "owner_id": post["owner_id"],
            "post_id": post["id"]
        }, "5.21")

        for comment in post_comments["items"]:
            if comment["from_id"] in friends and comment["from_id"] != post["owner_id"]:
                if comment["from_id"] in user_fans:
                    user_fans[comment["from_id"]] += 1
                else:
                    user_fans[comment["from_id"]] = 1

    return user_fans


def get_data(method, parameters, api_version):
    new_method_request = ApiMethodRequest(method, parameters, api_version)
    return new_method_request.do_request()["response"]


def check_is_error(method, parameters, api_version):
    new_method_request = ApiMethodRequest(method, parameters, api_version)
    return new_method_request.is_error()
