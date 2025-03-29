from src.DataScienceWorkflow import logger
from urllib import request
import zipfile
import os
from src.DataScienceWorkflow.entity.config_entity import DataIngestionConfig
import pandas as pd

class DataIngestion:

    def __init__(self,config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):

        if not os.path.exists(self.config.local_datafile):
            filename,headers = request.urlretrieve(
                url = str(self.config.source_url),
                filename = self.config.local_datafile
            )
            logger.info(f"{filename} downloaded! with following info {headers}")
        else:
            logger.info(f"File already exists")
    
    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_datafile,'r') as zip_ref:
            zip_ref.extractall(unzip_path)



