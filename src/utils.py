import os
import sys
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.custom_exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as fileobj:
            dill.dump(obj, fileobj)
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as fileobj:
            return dill.load(fileobj)
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model      = list(models.values())[i]
            model_name = list(models.keys())[i]
            para       = param[model_name]   # ✅ dict se lo

            gs = GridSearchCV(
                estimator=model,
                param_grid=para,
                cv=3,
                n_jobs=-1,
                verbose=0
            )
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_predict = model.predict(X_train)
            y_test_predict  = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_predict)
            test_model_score  = r2_score(y_test,  y_test_predict)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)