import sys
import os
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.custom_exception import CustomException
from src.logger import get_logger
from src.utils import save_object

logger = get_logger(__name__)

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file: str = os.path.join("artifact", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self):
        try:
            num_features = ["reading_score", "writing_score"]
            cat_features = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),  # ✅ comma
                    ("scaler",  StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",          SimpleImputer(strategy="most_frequent")),  # ✅ comma
                    ("one_hot_encoder",  OneHotEncoder()),                           # ✅ comma
                    ("scaler",           StandardScaler(with_mean=False))           # ✅ fix
                ]
            )

            logger.info(f"Categorical columns: {cat_features}")
            logger.info(f"Numerical columns:   {num_features}")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline",   num_pipeline, num_features),   # ✅ comma
                    ("categorical_pipeline", cat_pipeline, cat_features)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiated_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df  = pd.read_csv(test_path)
            logger.info("Train and test data read completed")

            preprocessing_obj  = self.get_data_transformation()
            target_column_name = "math_score"

            input_features_train_df = train_df.drop([target_column_name], axis=1)
            target_feature_train    = train_df[target_column_name]

            input_features_test_df  = test_df.drop([target_column_name], axis=1)
            target_feature_test     = test_df[target_column_name]

            input_features_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_arr  = preprocessing_obj.transform(input_features_test_df)

            train_arr = np.c_[input_features_train_arr, np.array(target_feature_train)]
            test_arr  = np.c_[input_features_test_arr,  np.array(target_feature_test)]

            logger.info("Saving preprocessing object")

            save_object(
                self.data_transformation_config.preprocessor_obj_file,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file
            )

        except Exception as e:
            raise CustomException(e, sys)