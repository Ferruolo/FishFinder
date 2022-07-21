# Methodology:
#   1. Scrape
#   2. Preprocess
#   3. Apply Model
#   4. Display to GUI


import xarray as xr
import pandas as pd
import numpy as np
import pickle
from tqdm.notebook import tqdm
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Sequential, losses


class DataProcessor:
    def __init__(self):
        self.climate_data_page = "selected-data-2021.nc"
        self.train_data = None
        self.model = model = Sequential([
            layers.Conv3D(50, kernel_size=(5, 5, 6), activation='ReLU'),
            layers.Conv3D(25, kernel_size=(10, 10, 1)),
            layers.Conv3D(1, kernel_size=1),
            layers.Flatten(),
            layers.Dense(5000, activation="ReLU"),
            layers.Dense(90*150, activation="sigmoid"),
            layers.Reshape((90, 150, 1)),
            layers.Conv2D(1, 1, activation = "sigmoid")
        ])


    def Preprocess(self):
        DS = xr.open_dataset(self.climate_data_page)
        DS_ARRAY = DS.to_array().to_numpy()
        # DS_ARRAY = DS_ARRAY.reshape((154, 91, 151, 6))
        DS_ARRAY = np.nan_to_num(DS_ARRAY, nan=0.0)[:, :, 0, :, :]
        DS_new = list()
        for i in range(DS_ARRAY.shape[1]):
            new_var_list = list()
            for j in range(DS_ARRAY.shape[0]):
                new_var_list.append(DS_ARRAY[j, i, :, :])
            new_var_list = np.stack(new_var_list, axis=-1)
            DS_new.append(new_var_list)
        variables = np.stack(DS_new)
        self.train_data = np.reshape(variables, (variables.shape[0], variables.shape[1], variables.shape[2], variables.shape[3], 1))


    def run_model(self, x):
        if self.train_data == None:
            return
        y = self.model.predict(x)
        return y



