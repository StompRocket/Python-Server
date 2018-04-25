# Python Server

A test of using Python and MongoDB as a backend.

**Usage**

MongoDB must be running in the background in order for PyMongo to be able to write to the database. 
Launch MongoDB with `mongod`, then launch `python3 server.py`.

**Reading from the databse**

Reading from the database can be done by accessing `localhost:8080/db/UID` (via a browser or curl is the easiest way) where UID is an `owneruid` added to the databse in the Python code. 

**Writing to the databse**

*because I still haven't implemented POST requests, adding entries to the database is done in much the same way as retrieving from it*

To write an entry to the databse, simply access `localhost:8080/push/t/TITLE/c/CONTENT/u/UID` where TITLE, CONTENT, and UID are specified by the user. UID will be used to look up databse entries, and must be unique. 