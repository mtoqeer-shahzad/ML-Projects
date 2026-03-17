import os
import sys
from sklearn.ensemble import (
    GradientBoostingRegressor,
    AdaBoostRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from dataclasses import dataclass
from src.custom_exception import CustomException
from src.logger import get_logger
from src.utils import save_object, evaluate_model

logger = get_logger(__name__)

@dataclass
class TrainModelConfig:
    train_model_file_path: str = os.path.join("artifact", "model.pkl")

class TrainModel:
    def __init__(self):
        self.train_model_config_path = TrainModelConfig()

    def initiated_model_trainer(self, train_array, test_array):
        try:
            logger.info("Splitting training and testing input data")

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Random Forest":        RandomForestRegressor(),
                "Decision Tree":        DecisionTreeRegressor(),
                "XG Boost":             XGBRegressor(),
                "K-Neighbor Regressor": KNeighborsRegressor(),
                "Linear Regression":    LinearRegression(),
                "AdaBoost Regressor":   AdaBoostRegressor(),
                "Gradient Boosting":    GradientBoostingRegressor()
            }

            params = {
                "Decision Tree": {
                    'criterion': [
                        'squared_error',
                        'friedman_mse',
                        'absolute_error',
                        'poisson'
                    ]
                },
                "Random Forest": {
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "Gradient Boosting": {
                    'learning_rate': [.1, .01, .05, .001],
                    'subsample':     [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    'n_estimators':  [8, 16, 32, 64, 128, 256]
                },
                "Linear Regression": {},
                "XG Boost": {              # ✅ models jaisa naam
                    'learning_rate': [.1, .01, .05, .001],
                    'n_estimators':  [8, 16, 32, 64, 128, 256]
                },
                "K-Neighbor Regressor": { # ✅ add kiya
                    'n_neighbors': [3, 5, 7, 9]
                },
                "AdaBoost Regressor": {
                    'learning_rate': [.1, .01, 0.5, .001],
                    'n_estimators':  [8, 16, 32, 64, 128, 256]
                }
                # ✅ CatBoosting hata diya — models mein nahi tha
            }

            model_report: dict = evaluate_model(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models,
                param=params    # ✅ param — s nahi!
            )

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No Best Model Found", sys)

            logger.info(
                f"Best Model: {best_model_name} | "
                f"Score: {best_model_score:.4f}"
            )

            save_object(
                file_path=self.train_model_config_path.train_model_file_path,
                obj=best_model
            )

            return best_model_score

        except Exception as e:
            raise CustomException(e, sys)