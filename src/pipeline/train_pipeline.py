import shutil
import sys
import os
import numpy as np
import pandas as pd


from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.constant import *
from src.exception import CustomException


class TrainingPipeline:
    
    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion()
            feature_store_file_path = data_ingestion.initiate_data_ingestion()
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys)
        
  