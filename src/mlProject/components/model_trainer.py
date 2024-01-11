import os
import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet
from mlProject.entity.config_entity import ModelTrainerConfig
from mlProject.logging import logger


class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig) :
        logger.debug("Instiating ModelTrainer class.")
        self.config = config
        logger.debug("ModelTrainer class initialized.")

    def train(self):
        logger.debug("Entered into train method of ModelTrainer class.")
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        
        logger.debug("Exiting train method of ModelTrainer class.")


