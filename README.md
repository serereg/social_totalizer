# Social Totalizer

A simple webserver for obtaining data and statistics about posts on a user's wall or a community in some social network, i.e. VK.

Features
* For given id of person or a social group get information about posts via csv file with format:

post id
  | text
  | amount of applications (?)
  | amount of likes
  | amount of reposts
  | amount of comments
* For given id of person or a social group get an aggregation of average amount of likes, reposts, comments:
  This functional is realised by jupyter notebook script that is sended on request.
    * by years
    * by months
    * by days
    * by hours

## Structure of repository
```buildoutcfg
.
|__ totalizer         : a project
|     |__ web         :   views, routes
|     |__ fetcher     :   classes for fetching data from VK
|     |__ static      :   static *.html
|
...
|__ tests             : tests for the project
```

## Instructions
For manual deploying on Linux (Ubuntu) machine and run locally:
1. Install python3.9 ```apt-get install python3.9```
1. Install virtualenv ```pip3 install virtualenv```
1. Create virtual environment ```virtualenv venv```
1. Activate vevn ```source venv/bin/activate```
1. Install dependencies ```pip3 install -e ./```
1. Run webserver ```python3.9 -m totalizer```
1. Check working via browser ```http://localhost/```

## Future improvements
1. Replace aiohttp to JupyterHub server with preconfigured scripts for getching data.
1. Add pyproject.toml file for installing project dependencies.
1. Use async library for fetching from VK (but, aiovk doesn't work properly).
   vk_api may be used just for generating list of tokens.
1. Use secure GET for sending user login and password.
