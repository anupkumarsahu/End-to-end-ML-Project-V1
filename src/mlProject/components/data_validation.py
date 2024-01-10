import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig
from mlProject.logging import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        logger.debug("Instiating DataValidation class.")
        self.config = config
        logger.debug("DataValidation class initialized.")
        
    def validate_all_columns(self) -> bool:
        logger.debug("Entered into validate_all_columns method of DataValidation class.")
        try:
            validation_status = True
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        
            logger.debug("Exiting validate_all_columns method of DataValidation class.")
            
            return validation_status
                
            
        except Exception as e:
            raise e