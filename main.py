from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeLine
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started")
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(f">>>> stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started")
    prepare_base_model_obj = PrepareBaseModelTrainingPipeline()
    prepare_base_model_obj.main()
    logger.info(f">>>> stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started")
    model_training_obj = ModelTrainingPipeLine()
    model_training_obj.main()
    logger.info(f">>>> stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started")
    model_eval_obj = EvaluationPipeline()
    model_eval_obj.main()
    logger.info(f">>>> stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e
