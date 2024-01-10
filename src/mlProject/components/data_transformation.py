import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject.logging import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        logger.debug("Instiating DataTransformation class.")
        self.config = config
        logger.debug("DataValidation class initialized.")
        
    def train_test_splitting(self,):
        logger.debug("Entered into train_test_splitting method of DataTransformation class.")
        
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index=False)
        
        logger.info("Splited data into training and test sets")
        logger.info(f"Training data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")
        
        logger.debug("Exiting train_test_splitting method of DataTransformation class.")