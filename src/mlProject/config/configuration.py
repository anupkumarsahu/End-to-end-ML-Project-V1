from mlProject.constants import *
from mlProject.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelTrainerConfig
from mlProject.utils.yaml_operations import create_directories, read_yaml
from mlProject.logging import logger


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        param_filepath=PARAM_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
    ):
        logger.debug("Instiating ConfigurationManager class")
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(param_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        
        logger.debug("Instiation of ConfigurationManager class completed successfully")

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logger.debug("Entering into get_data_ingestion_config method of ConfigurationManager class")
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        logger.debug("Exiting get_data_ingestion_config method of ConfigurationManager class")
        
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        logger.debug("Entering into get_data_validation_config method of ConfigurationManager class")
        
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
        )

        logger.debug("Exiting get_data_validation_config method of ConfigurationManager class")
        
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        logger.debug("Entering into get_data_transformation_config method of ConfigurationManager class")
        
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )
        
        logger.debug("Exiting get_data_transformation_config method of ConfigurationManager class")
        
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        logger.debug("Entering into get_model_trainer_config method of ConfigurationManager class")
        config = self.config.model_trainer
        params = self.param.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        logger.debug("Exiting get_model_trainer_config method of ConfigurationManager class")

        return model_trainer_config
