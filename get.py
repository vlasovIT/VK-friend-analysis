from settings import *
import json

class DataShow:
    def __init__(self):
        self.users = []

    def open_data(self):
        with open(LOCATION+"data.json") as file:
            self.users = json.load(file)

    def get_user_by_id(self, userid):
        userid = int(userid)
        for user in self.users:
            if user['id'] == userid:
                return user

    def print_likes(self, likesDict):
        likesList = list(likesDict.items())
        likesList.sort(key=lambda i: i[1], reverse=True)
        for i in range(len(likesList)):
            likeId = likesList[i][0]
            like = self.get_user_by_id(likeId)
            print(f'{i + 1}. {like["first_name"]} {like["last_name"]}')

    def print_fans(self, fansDict):
        fansList = list(fansDict.items())
        fansList.sort(key=lambda i: i[1], reverse=True)
        for i in range(len(fansList)):
            fanId = fansList[i][0]
            fan = self.get_user_by_id(fanId)
            print(f'{i + 1}. {fan["first_name"]} {fan["last_name"]}')

    def get_users_info(self, username):
        for user in self.users:
            if username in (user["first_name"]+" "+user["last_name"]) or username in (user["last_name"]+" "+user["first_name"]):
                print(user["first_name"]+" "+user["last_name"])

                print("\nFans:")
                self.print_fans(user["fans"])

                print("\nLikes:")
                self.print_likes(user["likes"])

                print("\n============================\n")


if __name__ == "__main__":
    dataShow = DataShow()
    dataShow.open_data()
    dataShow.get_users_info(input("Input user name: "))
    #print(dataShow.users)