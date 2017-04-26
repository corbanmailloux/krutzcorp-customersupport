import os
import secrets

if('ENV' in os.environ and os.environ['ENV'] == 'production'):
	print('Using Mysql database')
	DATABASE_URI = 'mysql+pymysql://customersupport:'+secrets.MYSQL_PASS+'@localhost/customer-support'
else:
	print('Using SQLite database')
	DATABASE_URI = 'sqlite:///customer-support.db'

HR_URL = 'http://vm343a.se.rit.edu:8080'
# SALES_URL = 'http://sales.krutz.site'
SALES_URL = 'http://vm343c.se.rit.edu/api'
