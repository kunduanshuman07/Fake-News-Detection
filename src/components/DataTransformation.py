import os
import sys
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from dataclasses import dataclass
from src.exceptions import CustomException
from src.logger import logging



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path : os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            pass
        except:
            pass

    def initiate_data_transformation(self, train_path, test_path):
        try:
            pass
        except:
            pass