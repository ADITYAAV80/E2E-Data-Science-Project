from src.DataScienceWorkflow.config.configuration import ConfigurationManager
from src.DataScienceWorkflow.components.model_evaluate import ModelEvaluate
from src.DataScienceWorkflow import logger

STAGE_NAME = "Model Evaluation Stage"
class ModelEvaluatePipeline:

    def __init__(self):
        pass

    def initiate_model_evaluate(self):
        try:
            cm = ConfigurationManager()
            model_train_evaluate = cm.get_model_evaluation_config()
            mt = ModelEvaluate(model_train_evaluate)
            mt.log_into_mlflow()
        except Exception as e:
            raise e


if __name__=="__main__":

    try:
        logger.info(f">>>>>Stage {STAGE_NAME} started <<<<<<")
        mep = ModelEvaluatePipeline()
        mep.initiate_model_evaluate()
        logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e