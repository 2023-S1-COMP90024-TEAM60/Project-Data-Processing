import ijson
import time
import argparse
from couchdb import Server, Document

def upload_lga_data(lga_path: str, couchdb_endpoint: str, database: str)-> None:
    couch = Server(couchdb_endpoint)
    db = couch[database]
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

def main(): 
    """
    Main method of the program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lga_data_in_file_path", type=str, help="LGA data input file path"
    )
    parser.add_argument(
        "--couchdb_endpoint", type=str, help="CouchDB endpoint"
    )
    parser.add_argument(
        "--couchdb_database", type=str, help="CouchDB database to store data"
    )
    args = parser.parse_args()

    print(f"Starting upload twitter data to {args.couchdb_endpoint}/{args.couchdb_database}")
    start_time=time.time()
    upload_lga_data(args.lga_data_in_file_path,args.couchdb_endpoint, args.couchdb_database)
    end_time=time.time()
    time_used=(end_time-start_time)/60
    print(f"Time used: {time_used} mins")
    
if __name__ == "__main__":
    main()
    