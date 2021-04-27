# VK friend analysis app

This app can collect data on the number of likes and comments in VK. That is, for a friend, the app counts how many likes and comments it has for each of the other friends.
##### !!! It uses only the information that is available to you. !!!

# Installation
1. Go to https://vk.com/apps?act=manage. Click "Create", type title and select platform - "Standalone app".
2. Go to section "Settings", and find <b>App ID</b> (for example, 1234567).</br>
Using the address bar go to link https://oauth.vk.com/authorize?client_id=1234567&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,offline&response_type=token&v=5.52, replacing 1234567 on your <b>App ID</b>. Than click "Allow".
The access_token value is your token. It may look like:
>51eff86578a3bbbcb5c7043a122a69fd04dca057ac821dd7afd7c2d8e35b60172d45a26599c08034cc40a

The token is your access key. If certain conditions are met, the person who received your token can cause significant damage to your data and the data of other people. Therefore, it is very important not to transfer your token to third parties.

3. Clone this GitHub repository. Open "setting.py" file and replace the "TOKEN" with your token.
4. Install python modules (using cmd or terminal)
```
pip install requests
pip install simplejson
```
5. Run "main.py" using python. For example using cmd or terminal (you can use any other ide):
```
python main.py
```
6. Now you can find out about the user. Run "get.py" using python. For example using cmd or terminal (you can use any other ide):
```
python get.py
```
Type user name or surname. App will show you the result.

# Project settings:
The application settings are located in the file "settings.py".
+ LOCATION - path where the data will be saved
+ SHOW_PROGRESS - app will show progress of getting data
+ SHOW_PARSING_USER - app will show the name of the user whose data it receives
