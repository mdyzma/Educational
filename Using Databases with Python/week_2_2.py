'''You do not need to export or convert the database - simply upload the .sqlite file that your program creates. See the example code for the use of the connect() statement.

Counting Organizations
======================

This application will read the mailbox data (``mbox.txt``) count up the number email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts. ::

    CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading. If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.pythonlearn.com/code/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.pythonlearn.com/code/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.'''

# Imports
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)

def get_email(fhandler):
    for line in fhandler:
        if not line.startswith('From: ') : continue
        pieces = line.split()
        return pieces[1]

emails = [get_email(fh)for line in fh]
# There is annooying "None" element at last position of the array
emails.pop()

orgs =[i.split('@')[1] for i in emails]
# Create dictionary counting elements on the way
d = {x:orgs.count(x) for x in orgs}

# switch to list of tuples, which is much easier to handle for sqlite
rows = [(key, value) for key, value in d.items()]
	
for row in rows:
    conn.execute("INSERT INTO Counts VALUES (?,?)", row)

conn.commit()

# Check data correctnes
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
