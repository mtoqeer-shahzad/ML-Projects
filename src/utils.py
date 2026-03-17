import os
import sys
import dill
from sklearn.metrics import r2_score
from src.custom_exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as fileobj:
            dill.dump(obj, fileobj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}  # ✅ list ki jagah dict

        for i in range(len(list(models))):
            model = list(models.values())[i]

            # Train karo
            model.fit(X_train, y_train)

            # Predict karo
            y_train_predict = model.predict(X_train)
            y_test_predict  = model.predict(X_test)   # ✅ X_test fix kiya

            # Score nikalo
            train_model_score = r2_score(y_train, y_train_predict)
            test_model_score  = r2_score(y_test,  y_test_predict)

            # Report mein save karo
            report[list(models.keys())[i]] = test_model_score

        return report  # ✅ loop ke bahar

    except Exception as e:
        raise CustomException(e, sys)