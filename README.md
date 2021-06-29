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
  This functional is realised by jupyter notebook script that is sent on request.
    * by years
    * by months
    * by days
    * by hours

## Structure of repository
```buildoutcfg
|__ totalizer         : a project
|     |__ web         :   views, routes
|     |__ fetcher     :   classes for fetching data from VK
|     |__ static      :   static *.html
|
...
|__ tests             : tests for the project
```

## Instructions
For manual deploying on Linux (Ubuntu) machine and running locally:
1. Install python3.9 ```apt-get install python3.9```
1. Install virtualenv ```pip3 install virtualenv```
1. Create virtual environment ```virtualenv venv```
1. Activate vevn ```source venv/bin/activate```
1. Install dependencies ```pip3 install -e ./```
1. Run webserver ```python3.9 -m totalizer```
1. Check working via browser ```http://localhost/```

For running with docker:
1. `ssh user@xxx.xxx.xxx.xxx`
1. `apt install git`
1. `git clone https://github.com/serereg/social_totalizer.git`
1. `apt install docker.io`
1. `cd social_totalizer`
1. `./run_docker.sh`
* useful command: `docker stop $(sudo docker ps -a -q)`

## Future improvements
1. Replace aiohttp to JupyterHub server with preconfigured scripts for getting data.
1. Add pyproject.toml file for installing project dependencies.
1. Use async library for fetching from VK (but, aiovk doesn't work properly).
   vk_api may be used just for generating list of tokens.
1. Use generator with receiving info from users wall by parts.
1. Use secure GET for sending user login and password.

1. Also, for getting simple statistic simple sql-serve could be used.
1. Also, any service for getting statistic could be run with another docker container.

# Useful links
* https://youtu.be/fP8oGx6ZA5o
* https://youtu.be/0fSi7o-tRzo
* https://pohmelie.github.io/presentation-base-docker/#slide1
