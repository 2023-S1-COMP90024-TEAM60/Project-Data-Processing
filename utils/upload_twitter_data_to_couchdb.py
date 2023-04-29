"""
    This program process the JSON file.
"""
import argparse
import logging
from couchdb import Server, Document
import ijson

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)


def upload_twitter_data(file_path: str, batch_size: int, couchdb_endpoint: str, database: str) -> None:
    """
    Upload twitter data to couch DB.

        Parameters:
            file_path (str): Original twitter JSON file path
            batch_size (int): Number of records to be inserted to DB at once
            couchdb_endpoint (str): CouchDB endpoint
            database (str): Database name

    """
    couch = Server(couchdb_endpoint)
    db = couch[database]
    records = []
    i = 0
    with open(file_path, "rb") as original_f:
        for record in ijson.items(original_f, "rows.item", use_float=True):
            try:
                if len(records)!=0 and len(records) % batch_size == 0:
                    logging.info(f"processed {i} records")
                    db.update(records)
                    records = []
                else:
                    if "place_id" in record["doc"]["data"]["geo"]:
                        records.append(Document(record))
                    elif "includes" in record["doc"]:
                        records.append(Document(record))
            except:
                logging.error(f"exception occurs of records...skipping records: ")
                records = []
            i += 1
        if len(records) > 0:
            db.update(records)

def main(): 
    """
    Main method of the program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--twitter_data_in_file_path", type=str, help="Twitter data input file path"
    )
    parser.add_argument(
        "--batch_size", type=int, help="Upload batch size"
    )
    parser.add_argument(
        "--couchdb_endpoint", type=str, help="CouchDB endpoint"
    )
    parser.add_argument(
        "--couchdb_database", type=str, help="CouchDB database to store data"
    )
    args = parser.parse_args()

    logging.info(f"Starting upload twitter data to {args.couchdb_endpoint}/{args.couchdb_database}")
    upload_twitter_data(args.twitter_data_in_file_path, args.batch_size,
                        args.couchdb_endpoint, args.couchdb_database)


if __name__ == "__main__":
    main()
