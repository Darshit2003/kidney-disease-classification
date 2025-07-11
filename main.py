from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>> stage {STAGE_NAME} Started")
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(f">>>> stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e