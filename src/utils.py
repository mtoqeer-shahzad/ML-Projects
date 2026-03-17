import os
import dill
from src.custom_exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as fileobj:
            dill.dump(obj,fileobj)
            
    except :
        pass