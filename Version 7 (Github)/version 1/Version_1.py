########################## Hafiz Abdulmanan ############################

########################## Github Api Scraping Task ####################

########################### Pygithub API ###############################

from github import Github
import json

g = Github("Acess_Token") # I am hiding my access token


data = {
    'user name':str,
    'full name':str,
    'email':str
}
all_data = list()

count=0

for users in g.search_users(query="repos:>=50 location:pakistan"):
    #print(users.name , " " , users.email, " ")
    data['user name'] = users.login # getting user name and storing to dictionary
    data['full name'] = users.name # name
    data['email'] = users.email # email
    print(data)
    all_data.append(data.copy())
    count+=1

### saving my data to a json file : it is a format used across internet to share data
json_string = json.dumps(all_data,indent = 4)
with open('version_1.json', 'w') as out:
    out.write(json_string)


print("Total users :", count)
