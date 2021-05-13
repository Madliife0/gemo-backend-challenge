import flask
from flask import jsonify
import requests
from collections import Counter
import datetime
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# importing json data from the api for the back 30 days :
today = datetime.date.today()
lastMonth = today - datetime.timedelta(days=30)
lastMonth_string=str(lastMonth.strftime("%Y-%m-%d"))
url="https://api.github.com/search/repositories?q=created:%3E"+lastMonth_string+"&sort=stars&order=desc&page=1&per_page=100"
json_data = requests.get(url).json()

# geting the items and retrieving all languages in the 100 repo :
items_json=json_data["items"]
languages_list=[]
for i in range(100):
    languages_list.append(items_json[i]["language"])
# now finding the 10 best occurences as the 10 trendiest languages    
common_languages=Counter(languages_list).most_common()
# finding the repos using the most trendy languages
repos_dict=dict()
for j in range(len(items_json)):
    for i in range(len(common_languages)):
        if common_languages[i][0]==items_json[j]["language"]:
            repos_dict[j]={common_languages[i][0]:items_json[j]["html_url"]}

@app.route('/', methods=['GET'])
def home():
    return '''
    <h2>
    try calling this 3 endpoints : </h2>
    <b> for github-api dump , to the last 30 days. call route <a href='http://localhost:5000/github-api'> 
    (/github-api) <a/> using the method : HTTP/GET</b> <br>
    <b> the trendiest languages in the popular 100 repos in the previous 30 days . call route <a href='http://localhost:5000/github-trendy'> 
    (/github-trendy) <a/> using the method : HTTP/GET </b><br>
    <b> the repos using the the trendiest languages in the popular 100 repos in the previous 30 days . call route <a href='http://localhost:5000/github-repos'> 
    (/github-repos) <a/> using the method : HTTP/GET </b>
    '''
# A route that return the Github Api - resopnse ** basically the only important subtree is items.
@app.route('/github-api', methods=['GET'])
def api_all():
    return jsonify(items_json)

# a route that gives the most trendy languages in the most popular 100 languages for the previous 30 days
@app.route('/github-trendy', methods=['GET'])
def api_trendy():
    return jsonify(common_languages)
@app.route('/github-repos', methods=['GET'])
def api_repos():
    return jsonify(repos_dict)
      


app.run()
