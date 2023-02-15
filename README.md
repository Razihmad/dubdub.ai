# dubdub.ai
# Data fields name should be same as
# 1. work, 2. dateTime, 3. status
# dateTime format should be like "30-May-2023-15:59:02" 


This is a to do list API. where you can get post update and delete any item by using the methods given below.
All these methods here are given using python requests library to access API.
There are total 7 urls to communicate with this api.


In Order To Run this project on your computer. Follow the given instruction given below.
# git clone https://github.com/Razihmad/dubdub.ai.git
# cd dubdub.ai
# install all dependencies using pip install -r requirements.txt
# now runserver using command python manage.py runserver
server on your local machine has been run now.
you can test the api as instructed below.


/incomplete/ => This is to get all the reminders that has not been completed yet.
/incomplete/<id>/ => In order to get any specific incomplete reminder just put the id of that in the url.
/complete/ =>    This is to get all the reminders that has  been completed so far.
/complete/<id>/ => In order to get any specific completed reminder just put the id of that in the url



/post/reminder/ => To post the reminder
# this is an example to post data.
    import requests
    import json
    from datetime import datetime
    my_date = "30-May-2023-15:59:02" 
    url = "<base url>/post/reminder/"
    data = {"work":"this is nothing work","status":"Incomplete","dateTime":my_date}
    data = json.dumps(data)
    headers = {"content-type":"application/json"}
    res = requests.post(url=url,data=data,headers=headers)
###### 

/update/reminder/<int:pk>/ => To update a particular reminder use this link by passing the primary key in the link


/delete/reminder/<int:pk>/ => To delete any reminder.

# example for delete .
    import requests
    import json
    url = "<base url>/delete/reminder/1/"
    res = requests.post(url=url)
######
