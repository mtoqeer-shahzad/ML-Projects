import os
import sys
from sklearn.ensemble import (
    GradientBoostingRegressor,
    AdaBoostRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression   # ✅ fix
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
    #                      ↑ str type add kiya

class TrainModel:
    def __init__(self):
        self.train_model_config_path = TrainModelConfig()

    def initiated_model_trainer(self, train_array, test_array):
        try:
            logger.info("Splitting training and testing input data")

            # ✅ Sahi order
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            # ✅ Dict sahi banaya — colon use kiya
            models = {
                "Random Forest":        RandomForestRegressor(),
                "Decision Tree":        DecisionTreeRegressor(),
                "XG Boost":             XGBRegressor(),
                "K-Neighbor Regressor": KNeighborsRegressor(),
                "Linear Regression":    LinearRegression(),
                "AdaBoost Regressor":   AdaBoostRegressor(),
                "Gradient Boosting":    GradientBoostingRegressor()
            }

            # ✅ X_test uppercase
            model_report: dict = evaluate_model(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models
            )

            # Best model score
            best_model_score = max(sorted(model_report.values()))

            # Best model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No Best Model Found", sys)

            logger.info(f"Best Model: {best_model_name} | Score: {best_model_score}")

            # ✅ Sahi path
            save_object(
                file_path=self.train_model_config_path.train_model_file_path,
                obj=best_model
            )

            return best_model_score

        except Exception as e:
            raise CustomException(e, sys)  # ✅ except fix kiya