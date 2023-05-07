import ijson
import time
import argparse
from couchdb import Server, Document

def upload_pop_data(file_path: str, couchdb_endpoint: str, database: str)-> None:
    """
    Extract useful fields in sudo population file and upload data to couch DB.
        Parameters:
            file_path (str): Original sudo population JSON file path
            couchdb_endpoint (str): CouchDB endpoint
            database (str): Database name
    """
    couch = Server(couchdb_endpoint)
    if database not in couch:
        couch.create(database)
    db = couch[database]
    records=[]
    with open(file_path, 'r') as f:
        data = ijson.items(f,'item',use_float=True)
        for obj in data:
            doc = {
                    'lga_code':obj[" lga_code_2021"],
                    'lga_popul':obj[" erp_2021"],
                    'lga_density':obj["pop_density_2021_people_per_km2"]
                }
            records.append(Document(doc))
        db.update(records)

def upload_lga_percentage(file_path: str, couchdb_endpoint: str, database: str)-> None:
    """
    - Extract fields related to gender/age/language used at home/education level in sudo file
    - calculate percentage of each category
    - upload data to couch DB.
        Parameters:
            file_path (str): pre-processed sudo JSON file path
            couchdb_endpoint (str): CouchDB endpoint
            database (str): Database name
    """
    couch = Server(couchdb_endpoint)
    if database not in couch:
        couch.create(database)
    db = couch[database]
    records=[]
    with open(file_path, 'r') as f:
        data = ijson.items(f,'item',use_float=True)
        for obj in data:
            doc = {
                    'lga_code':obj[" lga_code"],
                    'state_code':obj["state_code"],
                    # total count
                    'female':int(obj["tot_p_f"])/(int(obj["tot_p_f"])+int(obj[" total_lsa"])),
                    'male':int(obj[" tot_p_m"])/(int(obj["tot_p_f"])+int(obj[" total_lsa"])),
                    # total number in the chart
                    #'total_gla':obj[" total_lsa"],
                    # language used at home
                    'lang_en':int(obj[" lang_used_home_eng_only_p"])/(int(obj[" lang_used_home_eng_only_p"])+int(obj[" lang_used_home_oth_lang_p"])),
                    'lang_other':int(obj[" lang_used_home_oth_lang_p"])/(int(obj[" lang_used_home_eng_only_p"])+int(obj[" lang_used_home_oth_lang_p"])),
                    # age
                    'age_0_4':int(obj[" age_0_4_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_5_14':int(obj[" age_5_14_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_15_19':int(obj[" age_15_19_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_20_24':int(obj[" age_20_24_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_25_34':int(obj[" age_25_34_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_35_44':int(obj[" age_35_44_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_45_54':int(obj[" age_45_54_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_55_64':int(obj[" age_55_64_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_65_74':int(obj[" age_65_74_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_75_84':int(obj[" age_75_84_yr_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'age_85ov':int(obj[" age_85ov_p"])/(int(obj[" age_0_4_yr_p"])
                                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'preschool':int(obj["preschool"])/int(obj["tot_edu_p"]),
                    'primary':int(obj["primary"])/int(obj["tot_edu_p"]),
                    'secondary':int(obj["secondary"])/int(obj["tot_edu_p"]),
                    'tertiary_vocational_edu':int(obj["tert_voc_edu"])/int(obj["tot_edu_p"]),
                    'tertiary_uni_other_high':int(obj["tert_uni_other_high_edu"])/int(obj["tot_edu_p"]),
                    'type_educanl_institution_not_stated':int(obj["type_educanl_institution_not_stated"])/int(obj["tot_edu_p"]),
                    'other_type_educ_instit':int(obj["other_type_educ_instit"])/int(obj["tot_edu_p"])
                }
            records.append(Document(doc))
        db.update(records)
 
def upload_state_raw_data(file_path: str, couchdb_endpoint: str, database: str)-> None:
    """
    - Extract fields related to gender/age/language used at home/education level in sudo file
    - calculate the total number of each category
    - upload data to couch DB.
        Parameters:
            file_path (str): pre-processed sudo JSON file path
            couchdb_endpoint (str): CouchDB endpoint
            database (str): Database name
    """   
    couch = Server(couchdb_endpoint)
    if database not in couch:
        couch.create(database)
    db = couch[database]
    records=[]
    with open(file_path, 'r') as f:
        data = ijson.items(f,'item',use_float=True)
        for obj in data:
            doc = {
                    'lga_code':obj[" lga_code"],
                    'state_code':obj["state_code"],
                    # total count
                    'female':int(obj["tot_p_f"]),
                    'male':int(obj[" tot_p_m"]),
                    'total_gender':int(obj["tot_p_f"])+int(obj[" tot_p_m"]),

                    # language used at home
                    'lang_en':int(obj[" lang_used_home_eng_only_p"]),
                    'lang_other':int(obj[" lang_used_home_oth_lang_p"]),
                    'total_lang':int(obj[" lang_used_home_eng_only_p"])+int(obj[" lang_used_home_oth_lang_p"]),
                    # age
                    'age_0_4':int(obj[" age_0_4_yr_p"]),
                    'age_5_14':int(obj[" age_5_14_yr_p"]),
                    'age_15_19':int(obj[" age_15_19_yr_p"]),
                    'age_20_24':int(obj[" age_20_24_yr_p"]),
                    'age_25_34':int(obj[" age_25_34_yr_p"]),
                    'age_35_44':int(obj[" age_35_44_yr_p"]),
                    'age_45_54':int(obj[" age_45_54_yr_p"]),
                    'age_55_64':int(obj[" age_55_64_yr_p"]),
                    'age_65_74':int(obj[" age_65_74_yr_p"]),
                    'age_75_84':int(obj[" age_75_84_yr_p"]),
                    'age_85ov':int(obj[" age_85ov_p"]),
                    'total_age':(int(obj[" age_0_4_yr_p"])
                                    +int(obj[" age_5_14_yr_p"])+int(obj[" age_15_19_yr_p"])+int(obj[" age_20_24_yr_p"])+int(obj[" age_25_34_yr_p"])
                                    +int(obj[" age_35_44_yr_p"])+int(obj[" age_45_54_yr_p"])+int(obj[" age_55_64_yr_p"])+int(obj[" age_65_74_yr_p"])
                                    +int(obj[" age_75_84_yr_p"])+int(obj[" age_85ov_p"])),
                    'preschool':int(obj["preschool"]),
                    'primary':int(obj["primary"]),
                    'secondary':int(obj["secondary"]),
                    'tertiary_vocational_edu':int(obj["tert_voc_edu"]),
                    'tertiary_uni_other_high':int(obj["tert_uni_other_high_edu"]),
                    'type_educanl_institution_not_stated':int(obj["type_educanl_institution_not_stated"]),
                    'other_type_educ_instit':int(obj["other_type_educ_instit"]),
                    'total_edu':(int(obj["preschool"])+int(obj["primary"])+int(obj["secondary"])+int(obj["tert_voc_edu"])
                                +int(obj["tert_uni_other_high_edu"])+int(obj["type_educanl_institution_not_stated"])
                                +int(obj["other_type_educ_instit"]))
                }
            records.append(Document(doc))
        db.update(records)


def main(): 
    """
    Main method of the program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pop_sudo_data_in_file_path", type=str, help="population sudo data input file path"
    )
    parser.add_argument(
        "--other_sudo_data_in_file_path", type=str, help="input file path of sudo data related with gender/language/age/edu"
    )
    parser.add_argument(
        "--couchdb_endpoint", type=str, help="CouchDB endpoint"
    )
    parser.add_argument(
        "--sudo_pop_db", type=str, help="CouchDB database to store pop data"
    )
    parser.add_argument(
        "--sudo_other_data_db", type=str, help="CouchDB database to store lga_based percentage data"
    )
    parser.add_argument(
        "--sudo_other_data_raw_db", type=str, help="CouchDB database to store state_based raw data"
    )
    args = parser.parse_args()


    start_time=time.time()
    # upload population data
    print(f"Starting upload pop data to {args.couchdb_endpoint}/{args.sudo_pop_db}")
    upload_pop_data(args.pop_sudo_data_in_file_path,args.couchdb_endpoint, args.sudo_pop_db)
    end_time1=time.time()
    time_used1=(end_time1-start_time)/60
    print(f"Time used of uploading population data: {time_used1} mins")
    
    print()
    print(f"Starting upload sudo percentage data to {args.couchdb_endpoint}/{args.sudo_other_data_db}")
    upload_lga_percentage(args.other_sudo_data_in_file_path,args.couchdb_endpoint, args.sudo_other_data_db)
    end_time2=time.time()
    time_used2=(end_time2-start_time)/60
    print(f"Time used of uploading sudo percentage data: {time_used2} mins")
    
    print()
    print(f"Starting upload state_based raw data to {args.couchdb_endpoint}/{args.sudo_other_data_raw_db}")
    upload_state_raw_data(args.other_sudo_data_in_file_path,args.couchdb_endpoint, args.sudo_other_data_raw_db)
    end_time3=time.time()
    time_used3=(end_time3-start_time)/60
    print(f"Time used of uploading state_based raw data: {time_used3} mins")
    
if __name__ == "__main__":
    main()
    
