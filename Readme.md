VoterDB - Database of voterids
==============================

VoterDB is an application that mapping from voterid to a polling booth. 

There'll be huge number of voterids for each state. After couple of experiments it is found that **sqlite** works great for this particular use case. It is also easy to generate a database file for each state. 

USAGE
-----

To start development server:

	$ python voterdb.py

The program expects a SQLite database with name `voterids.db` in the current directory. A different database file can be specified using the environment variable `VOTERDB_DATABSE`.

	$ VOTERDB_DATABSE=a.db python voterdb.py

