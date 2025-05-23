from src.DataScienceWorkflow.config.configuration import ConfigurationManager
from src.DataScienceWorkflow.components.model_train import ModelTrainer
from src.DataScienceWorkflow import logger

STAGE_NAME = "Model Training Stage"
class ModelTrainingPipeline:

    def __init__(self):
        pass

    def initiate_model_train(self):
        try:
            cm = ConfigurationManager()
            model_train_config = cm.get_model_trainer_config()
            mt = ModelTrainer(model_train_config)
            mt.train()
        except Exception as e:
            raise e


if __name__=="__main__":

    try:
        logger.info(f">>>>>Stage {STAGE_NAME} started <<<<<<")
        mtp = ModelTrainingPipeline()
        mtp.initiate_model_train()
        logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e