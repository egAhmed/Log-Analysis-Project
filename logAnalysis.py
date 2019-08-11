#!/usr/bin/env python

import psycopg2

def connect():
    """Connect to the PostgreSQL database and returns a database connection."""
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        return db, c
    except:
        print("Error in connecting to database")



def popular_article():
    """Prints most popular three articles of all time"""
    db, c = connect()
    query = "select * from articles limit 3"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print ("\nPopular Articles:\n")
    for i in range(0, len(result), 1):
        #print ("\"" + result[i][0] + "\" - " + str(result[i][1]) + " views")
        print("'{}' - '{}' views.".format(str(result[i][1]),result[i][0])))




def popular_authors():
    """Prints most popular article authors of all time"""
    db, c = connect()
    query = "select * from authors"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print ("\nPopular Authors:\n")
    for i in range(0, len(result), 1):
        #print ("\"" + result[i][0] + "\" - " + str(result[i][1]) + " views")
        print("'{}' - '{}' views.".format(str(result[i][1]),result[i][0]))




def log_status():
    """Print days on which more than 1% of requests lead to errors"""
    db, c = connect()
    query = "select * from log"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print ("\nDays with more than 1% of errors:\n")
    for i in range(0, len(result), 1):
        #print (str(result[i][0])+ " - "+str(round(result[i][3], 2))+"% errors")
        print("'{}' - '{}' % errors.".format(result[i][0], str(result[i][3])))


def view_popular_article():
    try:
        db, c = connect()
        query = "create or replace view popular_articles as\
        select title,count(title) as views from articles,log\
        where log.path = concat('/article/',articles.slug)\
        group by title order by views desc"
        c.execute(query)
        db.commit()
        db.close()
    except:
        print("Error in creating view popular_articles")


def view_popular_authors():
    try:
        db, c = connect()
        query= "create or replace view popular_authors as select authors.name,\
        count(articles.author) as views from articles, log, authors where\
        log.path = concat('/article/',articles.slug) and\
        articles.author = authors.id group by authors.name order by views desc"
        c.execute(query)
        db.commit()
        db.close()
    except:
        print("Error in creating view popular_authors")


def view_log_status():
    try:
        db, c = connect()
        query = "create or replace view log_status as select Date,Total,Error,\
        (Error::float*100)/Total::float as Percent from\
        (select time::timestamp::date as Date, count(status) as Total,\
        sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error\
        from log group by time::timestamp::date) as result\
        where (Error::float*100)/Total::float > 1.0 order by Percent desc;"
        c.execute(query)
        db.commit()
        db.close()
    except:
        print("Error in creating view log_status")



if __name__ == '__main__':
    #code to make views

    view_popular_article()
    view_popular_authors()
    view_log_status()

    popular_article()
    popular_authors()
    log_status()
    print ("\nSuccess!\n")
