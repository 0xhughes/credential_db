# credential_db
These scripts were written in Python to create, populate, massage, and discover (via rainbow table'esque attack) dumped account credential information.

## General
Each script provides a certain function, first you may consider running the createDB.py script to create a database containing the table structure used by the rest of the scripts.

### createDB.py
This script's usage is simple, run it, tell it where you want your DB+table to be created, and you should be good to go.

### basic_Input.py
This script will read in dump files you have prepared. Ensure the dump files reside by themselves in a single directory, and that they all sure a format in their lines of " identifierDELIMITERpassword " For example, bob:password, or, billy+++drowssap, etc. It will ask for the type of dump (identifier + hash, identifier + clear text, etc), the delimiter, and the path of the input. It will then populate the database with entries from the files. Some care must be taken to massage the data within your dump files, removing characters that may interrupt SQL queries (such as *, or |, etc), and that each line within the dump files are the same (who know's what fun could end up in your DB if you read in some hacker's banner message into your cred. DB).

### generate_rain.py
This script will ask for your DB path, and then populate the DB with MD5's/SHA1's for each credential that has a cleartext password but no hashes with it. These hashes can later be leveraged to try and populate other credential's cleartext passwords by matching hashes.

### rain_to_clear.py
This script takes hashes generated from generate_rain.py, and compares them to credentials that have no cleartext passwords, but hashed passwords. Any matches will populate the cleartext password entry for that credential.

### rain_to_clear_threading.py
Same as above, but I am attempting to efficiently thread it to increase speed. When you leverage the above with millions of credentials, it takes a LONG time. This is a work in progress (as is most of this project).

### MD5colSHA1stoSHA1col.py
One time I brought in a big pile of SHA1 hashes in as MD5s, so I made this script to check the MD5 column and move SHA1s (40 characters) from the MD5 column into the SHA1 column.

## More General
This project has been slow and on-going for me. The scripts will vary in styling/format, and your results may vary. They were written using Python 2.7.11 within Windows 7. Some of the scripts utilize potential third party modules, so check the imports to prevent errors at run-time. Please reach out to me with any thoughts, comments, concerns, etc.
