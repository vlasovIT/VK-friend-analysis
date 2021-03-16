import json
from data import *


class VkParser:
    def __init__(self):
        self.users = []
        self.friends = []

    def main(self):
        self.save_friends_list()
        self.parse_users()
        self.friends_analysis()
        self.save_data()
        log_action("Done...")

    def save_data(self):
        log_action("Saving data...")

        data_json = json.dumps(self.users)
        with open(LOCATION+"data.json", "w") as file:
            file.write(data_json)

    def friends_analysis(self):
        log_action("Analysis of users...")

        for i, user in enumerate(self.users):
            log_user(f'{i+1}. {user["first_name"]} {user["last_name"]}')
            user["likes"] = user_analysis(self.users, user["id"])

    def parse_users(self):
        log_action("Getting users posts...")

        for i, user in enumerate(self.users):
            log_user(f'{i+1}. {user["first_name"]} {user["last_name"]}')

            user_data = get_data("wall.get", {"owner_id": user["id"], "filter": "owner"}, "5.21")
            for post in user_data["items"]:
                user["fans"] = get_likes(post, user["fans"])
                user["fans"] = get_comments(post, user["fans"], self.friends)

    def save_friends_list(self):
        log_action("Getting friends list...")

        friends_items = get_data("friends.get", {}, "5.21")["items"]
        for friend_id in friends_items:
            friend_data = get_data("users.get", {"user_ids": friend_id}, "5.21")
            self.users.append({
                "id": friend_data[0]["id"],
                "first_name": friend_data[0]["first_name"],
                "last_name": friend_data[0]["last_name"],
                "likes": {},
                "fans": {}
            })
            self.friends.append(friend_data[0]["id"])


if __name__ == "__main__":
    parser = VkParser()
    parser.main()
