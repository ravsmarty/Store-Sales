from store.logger import logging
from store.exception import StoreException
from store.utils import get_collection_as_dataframe
import sys,os
from store.entity import config_entity
from store.components import data_ingestion
from store.components.data_ingestion import DataIngestion

if __name__=="__main__":
    try:
        #data ingestion
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        print(data_ingestion.initiate_data_ingestion())
    
    except Exception as e:
        print(e)
