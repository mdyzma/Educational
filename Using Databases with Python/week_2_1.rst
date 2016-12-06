Instructions
------------

If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

.. code-block:: sqlite
        
    CREATE TABLE Ages ( 
    name VARCHAR(128), 
    age INTEGER
    )


Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:
::
    
    DELETE FROM Ages;
    INSERT INTO Ages (name, age) VALUES ('Atal', 21);
    INSERT INTO Ages (name, age) VALUES ('Arsalan', 32);
    INSERT INTO Ages (name, age) VALUES ('Raashi', 31);
    INSERT INTO Ages (name, age) VALUES ('Jorgie', 17);


Once the inserts are done, run the following SQL command::

    SELECT hex(name || age) AS X FROM Ages ORDER BY X


Find the first **row** in the resulting record set and enter the long string that looks like **53656C696E613333**.

**Note:** This assignment must be done using SQLite - in particular, the SELECT query above will not work in any other database. So you cannot use MySQL or Oracle for this assignment.


Answer
------

Alternative to SQLite Editor is simple SQLite library and command line tool taken from 

https://sqlite.org

In order to create SQlite  database type: ::
    
    sqlite3 mydata

In sqlite  environment (prompt changed to ``sqlite>``) input:

.. code-block:: sqlite
    
    CREATE TABLE Ages (name VARCHAR(128), age INTEGER);

    INSERT INTO Ages (name, age) VALUES ('Atal', 21);
    INSERT INTO Ages (name, age) VALUES ('Arsalan', 32);
    INSERT INTO Ages (name, age) VALUES ('Raashi', 31);
    INSERT INTO Ages (name, age) VALUES ('Jorgie', 17);

    SELECT hex(name || age) AS X FROM Ages ORDER BY X

You should get his in response: ::
    
    417273616C616E3332
    4174616C3231
    4A6F726769653137
    5261617368693331
    



