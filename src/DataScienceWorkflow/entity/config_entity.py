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
    all_schema: dict