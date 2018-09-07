# instagram-insights

The first part of a small instagram analytics tool.

At the moment just the "Fake Friends Finder" application. Which will display accounts that follow your account but have not liked a single picture of yours.
Great for finding "Fake Friends", "Fake Accounts" and "Follow to get attention Accounts".




## Setup
1. git clone 'https://github.com/SirBenedick/instagram-insights.git'
2. cd instagram-insights
3. virtualenv env (make sure you are using python > 3.4)
4. source env/bin/activate
5. pip install -r requirements.txt
6. retrive instagram cookie data and add to insta/config.py
7. python web.py
8. http://127.0.0.1:5000
9. enjoy


### To-Do
* add login function to extract cookie automatically
* "is private" error message
* data export of the results
* do analytic stuff


## Why
Project based learning seems to be the most efficent way of grasping a new topic.
During this Project I learned alot about the following:

* HTTP Requests
* AJAX
* Cookies
* Flask
* Websockets
* Javascript
* Data manipulation in python
