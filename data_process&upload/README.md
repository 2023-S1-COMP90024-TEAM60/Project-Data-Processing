## Utilities

1. upload_db.py: Upload the processed twitter data to couchdb
Command: <br>
`python3 upload_db.py --twitter_data_in_file_path <twitter json file path> --lga_data_in_file_path <lga json file path> --batch_size 10000 --couchdb_endpoint http://admin:comp90024-60@172.26.136.78:5984/ --couchdb_database <database name>`

2. upload_lga.py: Upload the processed lga data to couchdb
Command: <br>
`python3 upload_lga.py --lga_data_in_file_path <lga json file path> --couchdb_endpoint http://admin:comp90024-60@172.26.136.78:5984 --couchdb_database <database name>`

3. upload_geo_data.py: Upload the processed lga/state data to couchdb
Command: <br>
`python3 upload_geo_data.py --lga_data_in_file_path <lga json file path> --state_data_in_file_path <state json file path> --couchdb_endpoint http://admin:comp90024-60@172.26.136.78:5984 --couchdb_database_lga <lga database name> --couchdb_database_state <state database name>`

4. upload_sudo.py: Upload the processed sudo data to couchdb
Command: <br>
`python3 upload_sudo.py --pop_sudo_data_in_file_path "sudo/pop.json" --other_sudo_data_in_file_path "sudo/sudo_other.json" --couchdb_endpoint http://admin:comp90024-60@172.26.136.78:5984 --sudo_pop_db <database name1> --sudo_other_data_db <database name2> --sudo_other_data_raw_db <database name3> `
