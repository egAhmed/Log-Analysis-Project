# Log-Analysis-Project
An internal reporting tool that uses information of large database of a web server and draw business conclusions from that information.
(Project from [Full Stack Web Development Nanodegree]


#### The project drives following conclusions:
* Most popular three articles of all time.
* Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

### Functions in logAnalysis.py:
* **connect():** Connects to the PostgreSQL database and returns a database connection.
* **popular_article():** Prints most popular three articles of all time.
* **popular_authors():** Prints most popular article authors of all time.
* **log_status():** Print days on which more than 1% of requests lead to errors.
* **view_popular_articles():** Creates view popular_articles that drives first conclusion.
* **view_popular_authors():** Creates view popular_authors that drives second conclusion.
* **view_log_status():** Creates view log_status that drives third conclusion.


**Some of the codes are taken from visheshbanga/Log-Analysis-Udacity-Project