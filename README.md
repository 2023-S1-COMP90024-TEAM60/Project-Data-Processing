# Project-Data-Processing


## Utilities
1. upload_twitter_data_to_couchdb.py: Upload the twitter data to couchdb
Command: <br>
`python --twitter_data_in_file_path <twitter json file path> --batch_size 10000 --couchdb_endpoint http://<username>:<password>@<database ip>:<database port>/ --couchdb_database <database name>`