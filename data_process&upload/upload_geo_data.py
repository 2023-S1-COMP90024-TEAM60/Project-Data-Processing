import ijson
import time
import argparse
from couchdb import Server, Document

def upload_lga_data(lga_path: str, couchdb_endpoint: str, lga_database: str)-> None:
    couch = Server(couchdb_endpoint)
    db = couch[lga_database]
    records=[]
    with open(lga_path, 'r') as f:
        data = ijson.items(f, 'item',use_float=True)
        for obj in data:
            doc = {
                    'coordinates': obj["geo_point_2d"],
                    'geo_shape': obj["geo_shape"],
                    'ste_code':obj["ste_code"][0],
                    'ste_name':obj["ste_name"][0],
                    'lga_code':obj["lga_code"][0],
                    'lga_name':obj["lga_name_long"][0]
                }
            records.append(Document(doc))
        db.update(records)


def upload_state_data(state_path: str, couchdb_endpoint: str, state_database: str)-> None:
    couch = Server(couchdb_endpoint)
    db = couch[state_database]
    records=[]
    with open(state_path, 'r') as f:
        data = ijson.items(f,'item',use_float=True)
        for obj in data:
            doc = {
                "_id":obj["ste_code"][0],
                "data":{
                    "type": "Feature",
                    "properties":{"state_code": obj["ste_code"][0],"state_name": obj["ste_name"][0],"sentiment":0},
                    "geometry": obj["geo_shape"]["geometry"]  
                }
                }
            records.append(Document(doc))
        db.update(records)
        
def main(): 
    """
    Main method of the program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lga_data_in_file_path", type=str, help="LGA data input file path"
    )
    parser.add_argument(
        "--state_data_in_file_path", type=str, help="state data input file path"
    )
    parser.add_argument(
        "--couchdb_endpoint", type=str, help="CouchDB endpoint"
    )
    parser.add_argument(
        "--couchdb_database_lga", type=str, help="CouchDB database to store data"
    )
    parser.add_argument(
        "--couchdb_database_state", type=str, help="CouchDB database to store data"
    )
    args = parser.parse_args()

    print(f"Starting upload data to {args.couchdb_endpoint}/{args.couchdb_database_lga}")
    start_time=time.time()
    upload_lga_data(args.lga_data_in_file_path,args.couchdb_endpoint, args.couchdb_database_lga)
    end_time=time.time()
    time_used=(end_time-start_time)/60
    print(f"Time used: {time_used} mins")
    
    print(f"Starting upload data to {args.couchdb_endpoint}/{args.couchdb_database_state}")
    upload_state_data(args.state_data_in_file_path,args.couchdb_endpoint,args.couchdb_database_state)
    end_time2=time.time()
    time_used2=(end_time2-start_time)/60
    print(f"Time used: {time_used2} mins")

if __name__ == "__main__":
    main()
    