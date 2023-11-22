import os
import threading
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from typing import Optional, Union
from tensorflow import keras
from keras.preprocessing import image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class AutoSwiper:


    def __init__(
        self: 'AutoSwiper'
    ) -> None:
        
        self.model_history = None
        self.data_generator = image.ImageDataGenerator(
            rescale=1 / 255,
            fill_mode='nearest',
            zoom_range=0.3,
            rotation_range=180,
            horizontal_flip=True,
            width_shift_range=0.3,
            height_shift_range=0.3
        )
        self.sobel = np.array(
            [
                1, 2, 1,
                0, 0, 0,
                -1, -2, -1
            ]
        )
        self.sobel_init = keras.initializers.Constant(self.sobel)

        self.edge_detection_model = keras.Sequential(
            [
                # --Convolution Block--
                keras.layers.Input(
                    shape=(360, 360, 1)
                ),
                keras.layers.Conv2D(
                    filters=1, kernel_size=3,
                    padding='same', kernel_initializer=self.sobel_init
                ),
                keras.layers.Conv2D(
                    filters=32, kernel_size=3,
                    padding='valid', activation='relu'
                ),
                keras.layers.MaxPooling2D(
                    pool_size=(2, 2)
                ),
                keras.layers.Conv2D(
                    filters=64, kernel_size=3,
                    padding='valid', activation='relu'
                ),
                keras.layers.MaxPool2D(
                    pool_size=(2, 2)
                ),
                keras.layers.Conv2D(
                    filters=128, kernel_size=3,
                    padding='valid', activation='relu'
                ),
                keras.layers.Flatten(),
                
                # --Dense Layers--
                keras.layers.Dense(
                    units=64, activation='relu'
                ),
                keras.layers.Dense(
                    units=64, activation='relu'
                ),
                keras.layers.Dense(
                    units=2, activation='softmax'
                )
            ]
        )
        self.color_detection_model = keras.Sequential(
            [
                # --Convolution Block--
                keras.layers.Input(
                    shape=(360, 360, 3)
                ),
                keras.layers.Conv2D(
                    filters=32, kernel_size=3,
                    padding='valid', activation='relu'
                ),
                keras.layers.MaxPooling2D(
                    pool_size=(2, 2)
                ),
                keras.layers.Conv2D(
                    filters=64, kernel_size=3,
                    padding='valid', activation='relu'
                ),
                keras.layers.MaxPool2D(
                    pool_size=(2, 2)
                ),
                keras.layers.Conv2D(
                    filters=128, kernel_size=3,
                    padding='valid', activation='relu'
                ),
                keras.layers.Flatten(),
                
                # --Dense Layers--
                keras.layers.Dense(
                    units=64, activation='relu'
                ),
                keras.layers.Dense(
                    units=64, activation='relu'
                ),
                keras.layers.Dense(
                    units=2, activation='softmax'
                )
            ]
        )
        
        self.main_model = keras.Sequential(
            [
                keras.layers.Concatenate(
                    self.edge_detection_model, self.color_detection_model
                )
            ]
        )
        

    def fit_from_directory(
        self: 'AutoSwiper',
        epochs: int,
        directory: Union[Path, str],
        batch_size: Optional[int] = 1,
        steps_per_epoch: Optional[int] = 1,
        data_save_path: Optional[Union[Path, str]] = 'photo_counter_data.keras'
    ) -> keras.callbacks.History:

        all_images = self.data_generator.flow_from_directory(
            directory=directory,
            batch_size=32,
            target_size=(360, 20),
            class_mode='categorical',
            color_mode='grayscale'
        )
        self.model_history = self.model.fit(
            x=all_images,
            epochs=epochs,
            batch_size=batch_size,
            steps_per_epoch=steps_per_epoch
        )

        self.main_model.save(
            filepath=data_save_path
        )

        return self.model_history

a = AutoSwiper()
