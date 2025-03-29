from src.DataScienceWorkflow import logger
from src.DataScienceWorkflow.pipeline.data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>Stage {STAGE_NAME} started <<<<<<")
    ditp = DataIngestionTrainingPipeline()
    ditp.initiate_data_ingestion()
    logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e