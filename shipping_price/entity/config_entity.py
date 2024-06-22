import os
from dataclasses import dataclass
from from_root import from_root
#from shipping_price.configuration.s3_operations import S3Operation
from shipping_price.utils.main_utils import MainUtils
from shipping_price.constant import *


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.UTILS = MainUtils()
        self.SCHEMA_CONFIG = self.UTILS.read_yaml_file(filename=SCHEMA_CONFIG_FILE)
        self.DB_NAME = DB_NAME
        self.COLLECTION_NAME = COLLECTION_NAME
        self.DROP_COLS = list(self.SCHEMA_CONFIG["drop_columns"])
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(
            from_root(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR
        )
        self.TRAIN_DATA_ARTIFACTS_FILE_DIR: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_TRAIN_DIR
        )
        self.TEST_DATA_ARTIFACTS_FILE_DIR: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_TEST_DIR
        )
        self.TRAIN_DATA_FILE_PATH: str = os.path.join(
            self.TRAIN_DATA_ARTIFACTS_FILE_DIR, DATA_INGESTION_TRAIN_FILE_NAME
        )
        self.TEST_DATA_FILE_PATH: str = os.path.join(
            self.TEST_DATA_ARTIFACTS_FILE_DIR, DATA_INGESTION_TEST_FILE_NAME
        )
        
@dataclass
class DataValidationConfig:
    def __init__(self):
        self.UTILS = MainUtils()
        self.SCHEMA_CONFIG = self.UTILS.read_yaml_file(filename=SCHEMA_CONFIG_FILE)
        self.DATA_VALIDATION_ARTIFACTS_DIR: str = os.path.join(
            from_root(), ARTIFACTS_DIR, DATA_VALIDATION_ARTIFACTS_DIR
        )
        self.DATA_DRIFT_FILE_PATH: str = os.path.join(
            self.DATA_VALIDATION_ARTIFACTS_DIR, DATA_DRIFT_FILE_NAME
        )
        
    
@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.UTILS = MainUtils()
        self.SCHEMA_CONFIG = self.UTILS.read_yaml_file(filename=SCHEMA_CONFIG_FILE)
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(
            from_root(), ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR
        )
        self.TRANSFORMED_TRAIN_DATA_DIR: str = os.path.join(
            self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_TRAIN_DATA_DIR
        )
        self.TRANSFORMED_TEST_DATA_DIR: str = os.path.join(
            self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_TEST_DATA_DIR
        )
        self.TRANSFORMED_TRAIN_FILE_PATH: str = os.path.join(
            self.TRANSFORMED_TRAIN_DATA_DIR, TRANSFORMED_TRAIN_DATA_FILE_NAME
        )
        self.TRANSFORMED_TEST_FILE_PATH: str = os.path.join(
            self.TRANSFORMED_TEST_DATA_DIR, TRANSFORMED_TEST_DATA_FILE_NAME
        )
        self.PREPROCESSOR_FILE_PATH: str = os.path.join(
            from_root(),
            ARTIFACTS_DIR,
            DATA_TRANSFORMATION_ARTIFACTS_DIR, 
            PREPROCESSOR_OBJECT_FILE_NAME,
        )
        
@dataclass
class ModelTrainerConfig:
    def __init__(self):
        self.UTILS = MainUtils()
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR = os.path.join(
            from_root(), ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR
        )
        self.MODEL_TRAINER_ARTIFACTS_DIR = os.path.join(
            from_root(), ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR
        )
        self.PREPROCESSOR_OBJECT_FILE_PATH = os.path.join(
            self.DATA_TRANSFORMATION_ARTIFACTS_DIR, PREPROCESSOR_OBJECT_FILE_NAME
        )
        self.TRAINED_MODEL_FILE_PATH = os.path.join(
            from_root(), ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR, MODEL_FILE_NAME
        )