# Getting db version
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","password","TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()

# Drop existing table and creating new
mport MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","password","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20),
         LAST_NAME  CHAR(20),
         AGE INT,
         INCOME FLOAT )"""

cursor.execute(sql)


# disconnect from server
db.close()

# Inserting data to table
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","password","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, INCOME)
         VALUES ('Mac', 'Mohan', 20, 2000)"""

#....................OR.......................................		 
# Dynamically adding values
"""
# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
"""
#...........................................................

#.......................OR....................................
user_id = "test123"
password = "password"

con.execute('insert into Login values("%s", "%s")' % \
             (user_id, password))
.............................................................
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

#......... Read data from database
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","password","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      income = row[3]
      # Now print fetched result
      print "fname=%s,lname=%s,age=%d,income=%d" % \
             (fname, lname, age, income )
except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()

#......... Update data from database
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","password","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = '21' WHERE INCOME = '%f'" % (2000)

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
