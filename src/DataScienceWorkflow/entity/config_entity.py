from pydantic import BaseModel, HttpUrl
from pathlib import Path

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_url: HttpUrl  
    local_datafile: Path
    unzip_dir: Path

class DataValidationConfig(BaseModel):

    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    ##from schema
    all_schema: dict

class DataTransformationConfig(BaseModel):

    root_dir: Path
    data_path: Path

class ModelTrainerConfig(BaseModel):
    ## from config
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    ## from params
    alpha: float  
    l1_ratio: float
    ## from schema 
    target_column: str

