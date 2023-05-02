import json
import time
import argparse
from couchdb import Server, Document


def get_lga_code(lga_path):
    """
    This function loads lga.json and returns two dictionaries: lga_dict and state_dict.

        Parameters: 
            lga_path (string): A file path of the JSON file containing the LGA data.
        
        Returns:
            lga_dict (dict): A dictionary in the form of {lga_name:[lga_code,state_code]} 
            state_dict (dict): A dictionary in the form of {state_code: state_code}.
    """
    lga = json.load(open(lga_path,"r")) 
    lga_dict = dict()
    state_dict = dict()

    for i in lga:
        name = i['lga_name_long'][0]
        code = i['lga_code'][0]
        state_code = str(i['ste_code'][0])
        state_name = i['ste_name'][0]
        lga_dict[name] = [code,state_code]
        if state_name not in state_dict:
            state_dict[state_name] = state_code
    return(lga_dict,state_dict)


def extract_lga_info(item,lga_dict,state_dict):
    """
    This function matches the full_name field in the twitter data to the LGA location
    
        Parameters: 
            item(object): A json object in twitter file
            lga_dict (dict): A dictionary in the form of {lga_name:[lga_code,state_code]} 
            state_dict (dict): A dictionary in the form of {state_code: state_code}.
            
        Return:
            A tuple including the lag_name (string), lga_code (string), and state_code (string).
    """
    name = item['doc']['includes']['places'][0]['full_name']
    name = name.split(', ')
    lga_name = '0'
    state_code = '0'
    lga_code = '0'
    
    for each in name:
        if each in lga_dict:
            lga_name=each
            lga_code=lga_dict[each][0]
            state_code=lga_dict[each][1]
            break
            
    # for the special case: Victoria, Australia  
    for each in name:
        if each in state_dict:
            state_code=state_dict[each]
    
    return lga_name,lga_code,state_code


def upload_twitter_data(file_path: str, lga_path: str, batch_size: int, couchdb_endpoint: str, database: str)-> None:
    """
    Extract useful fields and upload twitter data to couch DB.
        Parameters:
            file_path (str): Original twitter JSON file path
            batch_size (int): Number of records to be inserted to DB at once
            couchdb_endpoint (str): CouchDB endpoint
            database (str): Database name
    """
    
    couch = Server(couchdb_endpoint)
    if database not in couch:
        couch.create(database)
    db = couch[database]
    lga_dict,state_dict=get_lga_code(lga_path)
    records=[]
    i=0
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip().endswith(","):
                line = line[:len(line)-2]
            obj = None
            try:
                obj = json.loads(line)
                # check if the tweet have location
                obj["doc"]["includes"]["places"][0]["full_name"]
            except:
                # skip if it's not a proper json or doesn't have have location
                continue
            
            try:
                # use the twitter id as doc_id
                doc_id = obj['id']
                # Extract the fields needed from the JSON object
                author_id = obj['doc']['data']['author_id']
                created_at=obj['doc']['data']['created_at']
                # content info
                tags=obj['value']['tags']
                tokens=obj['value']['tokens']
                text=obj['doc']['data']['text']
                lang=obj['doc']['data']['lang']
                sentiment=obj['doc']['data']['sentiment']
                # geo
                geo_full_name=obj['doc']['includes']['places'][0]['full_name']
                geo_coord=obj['doc']['includes']['places'][0]['geo']['bbox'] # [longitude of the southwest corner, latitude of the southwest corner, longitude of the northeast corner, latitude of the northeast corner]
                lga_name,lga_code,state_code=extract_lga_info(obj,lga_dict,state_dict)
                # others 
                n_retweet=int(obj['doc']['data']['public_metrics']['retweet_count'])
                n_reply=int(obj['doc']['data']['public_metrics']['reply_count'])
                n_like=int(obj['doc']['data']['public_metrics']['like_count'])
                n_quote=int(obj['doc']['data']['public_metrics']['quote_count'])
                
                    # Create the document with the selected fields
                doc = {
                    '_id': doc_id,
                    'author_id':author_id,
                    'created_at':created_at,

                    # content info
                    'tags':tags,
                    'tokens':tokens,
                    'text':text,
                    'lang':lang,
                    'sentiment':sentiment,
                    
                    # location info
                    'geo_full_name':geo_full_name,
                    'geo_coord': geo_coord,
                    'lga_name':lga_name,
                    'lga_code':lga_code,
                    'state_code':state_code,
                    
                    # others 
                    'n_retweet':n_retweet,
                    'n_reply':n_reply,
                    'n_like':n_like,
                    'n_quote':n_quote
                    }
                    
                records.append(Document(doc))
                    
                # upload docs as batch
                if len(records)!=0 and len(records) % batch_size == 0:
                    db.update(records)
                    print(f"processed {i} records")
                    records = []
            except:
                print(f"exception occurs of object...skipping records: {0}")
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
        "--lga_data_in_file_path", type=str, help="LGA data input file path"
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

    print(f"Starting upload twitter data to {args.couchdb_endpoint}/{args.couchdb_database}")
    start_time=time.time()
    upload_twitter_data(args.twitter_data_in_file_path, args.lga_data_in_file_path,args.batch_size,
                        args.couchdb_endpoint, args.couchdb_database)
    end_time=time.time()
    time_used=(end_time-start_time)/60
    print(f"Time used: {time_used} mins")
    
if __name__ == "__main__":
    main()
    
#python3 upload_db.py --twitter_data_in_file_path sample_data_with_geo_loc.json --lga_data_in_file_path lga_list.json --batch_size 50000 --couchdb_endpoint http://admin:comp90024-60@172.26.136.78:5984 --couchdb_database test