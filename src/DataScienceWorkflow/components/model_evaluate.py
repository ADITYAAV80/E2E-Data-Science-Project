import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
import mlflow
from urllib.parse import urlparse
from src.DataScienceWorkflow.utils.common import save_json
from mlflow.models.signature import infer_signature
from src.DataScienceWorkflow.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
import os

# os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/adityaav80/wine_quality.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"] = "ADITYAAV80" 
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "7c7d5f1b5994f5230784a07f1f9573168c40c053"


class ModelEvaluate:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self,actual,pred):

        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)

        return rmse,mae,r2

    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        x_test = test_data.drop([self.config.target_column],axis = 1)
        y_test = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        signature = infer_signature(x_test,y_test)

        with mlflow.start_run():

            y_pred = model.predict(x_test)
            (rmse, mae, r2) = self.eval_metrics(y_test, y_pred)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel",signature=signature)
            else:
                mlflow.sklearn.log_model(model, "model",signature=signature)
    