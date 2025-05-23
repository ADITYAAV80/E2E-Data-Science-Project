from src.DataScienceWorkflow.config.configuration import ConfigurationManager
from src.DataScienceWorkflow.components.data_ingestion import DataIngestion
from src.DataScienceWorkflow import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass
    def initiate_data_ingestion(self):

        try:
            cm = ConfigurationManager()
            data_ingestion_config = cm.get_data_ingestion_config()
            di = DataIngestion(data_ingestion_config)
            di.download_file()
            di.extract_zip_file()
        except Exception as e:
            raise e


if __name__=="__main__":

    try:
        logger.info(f">>>>>Stage {STAGE_NAME} started <<<<<<")
        ditp = DataIngestionTrainingPipeline()
        ditp.initiate_data_ingestion()
        logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e