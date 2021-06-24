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
    * by years
    * by months
    * by days
    * by hours

## Structure
```buildoutcfg
.
|__ totalizer
|     |__ web
|     |__ routes
|     |__ views
|__ fetcher
|__ static
|
...
|__ tests
```

## Instructions
For manual deploying on Linux (Ubuntu) machine and run locally:
1. Install python3.9 ```apt-get install python3.9```
1. Install virtualenv ```pip3 install virtualenv```
1. Create virtual environment ```virtualenv venv```
1. If you need administrative privileges, get it ```sudo -s```
1. Activate vevn ```source venv/bin/activate```
1. Install dependencies ```pip3 install -r requirements.txt```
1. Run webserver ```python3.9 -m totalizer```
1. Check working via browser ```http://localhost/```
