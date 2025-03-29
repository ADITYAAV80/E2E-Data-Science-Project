from src.DataScienceWorkflow import logger
from src.DataScienceWorkflow.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.DataScienceWorkflow.pipeline.data_validation import DataValidationTrainingPipeline
from src.DataScienceWorkflow.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.DataScienceWorkflow.pipeline.model_train import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>Stage {STAGE_NAME} started <<<<<<")
    ditp = DataIngestionTrainingPipeline()
    ditp.initiate_data_ingestion()
    logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>Stage {STAGE_NAME} started <<<<<<")
    ditp = DataValidationTrainingPipeline()
    ditp.initiate_data_validation()
    logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>Stage {STAGE_NAME} started <<<<<<")
    dt = DataTransformationTrainingPipeline()
    dt.initiate_data_transformation()
    logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>Stage {STAGE_NAME} started <<<<<<")
    mtp = ModelTrainingPipeline()
    mtp.initiate_model_train()
    logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e