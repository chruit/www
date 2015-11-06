# script to remove columns from a table in sqlite

# /usr/bin/python

# sql commands
# pragma table_info("chru_pubs_person")


import sqlite3

conn = sqlite3.connect('chru.sqlite')

c = conn.cursor()

c.execute("pragma table_info('chru_pubs_person')")
for c in c.fetchall():
	print c

"""
(0, u'interests', u'varchar(600)', 1, None, 0)
(1, u'about', u'varchar(2200)', 1, None, 0)
(2, u'urls', u'varchar(1000)', 1, None, 0)
(3, u'title', u'varchar(350)', 1, None, 0)
(4, u'employment_type', u'integer', 1, None, 0)
(5, u'uwnetid', u'varchar(12)', 1, None, 0)
(6, u'honors', u'varchar(700)', 1, None, 0)
(7, u'full_name', u'varchar(50)', 1, None, 0)
(8, u'id', u'integer', 0, None, 1)
(9, u'education', u'varchar(600)', 1, None, 0)
(10, u'order', u'INTEGER', 0, None, 0)
"""

""" 

`rename table

ALTER TABLE chru_pubs_person
	RENAME to chru_pubs_person_old

`create new pubs table without columns for about and urls

CREATE TABLE chru_pubs_person
(
interests, varchar(600), 
title varchar(350),
employment_type integer,
uwnetid varchar(12), 
honors varchar(700), 
full_name varchar(50),
id integer, 
education varchar(600),
order INTEGER,
);


"""