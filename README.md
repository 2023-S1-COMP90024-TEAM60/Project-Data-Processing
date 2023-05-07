# Project-Data-Processing


## Utilities
1. upload_twitter_data_to_couchdb.py: Upload the twitter data to couchdb
Command: <br>
`python --twitter_data_in_file_path <twitter json file path> --batch_size 10000 --couchdb_endpoint http://<username>:<password>@<database ip>:<database port>/ --couchdb_database <database name>`

2. upload_db.py: Upload the processed twitter data to couchdb
Command: <br>
`python3 upload_db.py --twitter_data_in_file_path <twitter json file path> --lga_data_in_file_path <lga json file path> --batch_size 10000 --couchdb_endpoint http://admin:comp90024-60@172.26.136.78:5984/ --couchdb_database <database name>`

3. upload_lga.py: Upload the processed lga data to couchdb
Command: <br>
`python3 upload_lga.py --lga_data_in_file_path <lga json file path> --couchdb_endpoint http://admin:comp90024-60@172.26.136.78:5984 --couchdb_database <database name>`

4.upload_sudo.py: Upload the processed sudo data to couchdb
Command: <br>
`python3 upload_sudo.py --pop_sudo_data_in_file_path "sudo/pop.json" --other_sudo_data_in_file_path "sudo/sudo_other.json" --couchdb_endpoint http://admin:comp90024-60@172.26.136.78:5984 --sudo_pop_db <database name1> --sudo_other_data_db <database name2> --sudo_other_data_raw_db <database name3> `
