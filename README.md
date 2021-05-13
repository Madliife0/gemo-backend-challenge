# gemo-backend-challenge
## _this repo is an answer to gemography back end challenge   (using python-flask)_
## Functional specs

- Develop a REST microservice that list the languages used by the 100 trending public repos on GitHub.
- For every language, you need to calculate the attributes below 👇:
    - Number of repos using this language
    - The list of repos using the language
## The Code 
- i started with a GET request to the GitHub API. from the challenge i knew that we only need the first 100 row so i put the page and number of records, but i used the datetime in order to call for todays date and delete 30 days as requested.
- there is 3 endpoints uses GET Request:
- 1 : an api data dump at : /github-api 
- 2 : classification of the languages from the most populat to the least at : /github-trendy
- 3 : each language and the url repos using it at : /github-repos

## notice : it uses port 5000
