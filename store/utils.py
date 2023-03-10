import pandas as pd  
from store.logger import logging
from store.exception import StoreException
from store.config import mongo_client
import os,sys
#import yaml
#import dill
import numpy as np 

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description :This function return collection as dataframe
    =========================================================
    params:
    database_name:database_name 
    collection_name: collection_name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df= pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)
