import os
from pathlib import Path
from urllib import request
import zipfile
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.utils.yaml_operations import get_size
from mlProject.logging import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        logger.debug("Instiating DataIngestion class.")
        self.config = config
        logger.debug("DataIngestion class initialized.")


    
    def download_file(self):
        logger.debug("Entered into download_file method of DataIngestion class.")
        
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            
        logger.debug("Exiting download_file method of DataIngestion class.")



    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        logger.debug("Entered into extract_zip_file method of DataIngestion class.")
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
        logger.debug("Exiting extract_zip_file method of DataIngestion class.")