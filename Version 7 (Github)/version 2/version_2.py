########################## Hafiz Abdulmanan ############################

########################## Github Api Scraping Task (Programming langueges version)####################

from github import Github
import json

g = Github("access token")


data = {
    'user name':str,
    'full name':str,
    'email':str,
    'languages':list
}
all_data = list()

for users in g.search_users(query="repos:>=600 location:pakistan"):
    #print(users.name , " " , users.email, " ")
    data['user name'] = users.login
    data['full name'] = users.name
    data['email'] = users.email

    #languages are not directly be present at the user data but can be accessed by repos data
    repo = g.get_user(users.login).get_repos() # to get programminng langueges we have to get info of repos
    list_prog = list()
    for r in repo:
        if(r.language != None): # some repos dont have languages
            if(r.language not in list_prog): # making sure to eliminate duplicate entries
                list_prog.append(r.language)
                #print(r.language)

    data['languages'] = list_prog
    print(data)
    all_data.append(data.copy())

json_string = json.dumps(all_data,indent = 4)
with open('version_2.json', 'w') as out:
    out.write(json_string)