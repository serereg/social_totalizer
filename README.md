# Social Totalizer

A simple webserver for obtaining data and static about posts on a user's wall or community in social network, i.e. VK.

Features
* For given id of page/person get information about posts via csv file with:
  | post id
  | text
  | amount of applications (?)
  | amount of Likes
  | amount of reposts
  | amount of comments
* For given id of page/person get aggregation of average amount of Likes, reposts, comments:
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
...
|__ tests
```

## Instructions
For manual deploying on Linux (Ubuntu) machine and run locally:
1. Install python3.9 ```apt-get install python3.9```
1. Install virtualenv ```pip3 install virtualenv```
1. Create virtual environment ```virtualenv venv```
1. Activate vevn ```source venv/bin/activate```
1. Install dependencies ```pip3 install -r requirements.txt```
1. Run webserver ```python3.9 -m totalizer```
1. Check working via browser ```http://localhost/```
