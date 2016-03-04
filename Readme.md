Voter Lookup
============

Voter Lookup is an application that finds the state, assembly constituency and polling booth, given an voter id.

This works by maintaining the all the voterids in a sqlite database table.

USAGE
-----

To start development server:

	$ python webapp.py

The program expects a SQLite database with name `voter.db` in the current directory. A different database file can be specified using the environment variable `VOTER_LOOKUP_DATABSE`.

	$ VOTER_LOOKUP_DATABSE=a.db python webapp.py

Running in production:

	$ gunicorn webapp:application -b 127.0.0.1:8080

Running using Docker
--------------------

Build the docker image:

	$ docker build anandology/voter-lookup:devel .

Run the application:

	$ docker run -p 8080:80 -v /opt/voter-lookup/voter.db:/voter.db anandology/voter-lookup:devel

This assumes the voterids database is available at /opt/voter-lookup/voter.db.

Use option `--restart=always` if you want docker to auto-restart your application and auto start it on boot.

API
---

	$ curl 'http://voter-lookup/search?voterid=ABC1234567'
	[
	 {
	  "voterid": "ABC1234567",
	  "state": "DL",
	  "ac": 56
	  "pb": 130,
	 }
	]

Optionally, two-letter state code can be specified to limit the search to one particular state.


	$ curl 'http://voter-lookup/search?voterid=ABC1234567&state=DL'
	[
	 {
	  "voterid": "ABC1234567",
	  "state": "DL",
	  "ac": 56
	  "pb": 130,
	 }
	]

Please note that the `voter-lookup` in the URL should be replaced with the hostname.
