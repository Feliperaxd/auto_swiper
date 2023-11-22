import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Optional,Union

from tensorflow import keras
from keras.preprocessing import image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class PhotoCounter:


    def __init__(
        self: 'PhotoCounter'
    ) -> None:

        self.data_generator = image.ImageDataGenerator(
            rescale=1 / 255,
            fill_mode='constant',
            width_shift_range=0.1,
            height_shift_range=0.1
        )
        self.prewitt_filter = np.array(
            [
                [1, 0, -1], 
                [1, 0, -1], 
                [1, 0, -1]
            ],
            dtype=np.float32
        )
        """self.prewitt_filter = np.stack(
            [self.prewitt_filter] * 3, 
            axis=-1
        )"""
        self.prewitt_initializer = keras.initializers.Constant(self.prewitt_filter)
        
        self.model = keras.Sequential(
                [
                # --Convolution Block--
                keras.layers.Input(
                    shape=(360, 20, 1)
                ),
                keras.layers.Conv2D(
                    filters=1, kernel_size=3,
                    padding='same', kernel_initializer=self.prewitt_initializer
                ),
                keras.layers.Conv2D(
                    filters=32, kernel_size=3,
                    padding='same', activation='relu'
                ),
                keras.layers.MaxPool2D(
                    pool_size=(2, 2)
                ),
                keras.layers.Conv2D(
                    filters=64, kernel_size=3,
                    padding='same', activation='relu'
                ),
                keras.layers.MaxPool2D(
                    pool_size=(2, 2)
                ),
                keras.layers.Conv2D(
                    filters=128, kernel_size=3,
                    padding='same', activation='relu'
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
                    units=8, activation='softmax'
                )
            ]
        )
        self.model.compile(
            loss=keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy'],
            optimizer=keras.optimizers.Adam()
        )
    
    def fit_from_directory(
        self: 'PhotoCounter',
        epochs: int,
        directory: Union[Path, str],
        batch_size: Optional[int] = 1,
        steps_per_epoch: Optional[int] = 1,
        data_save_path: Optional[Union[Path, str]] = 'photo_counter_data.keras'
    ) -> keras.callbacks.History:


        self.all_images = self.data_generator.flow_from_directory(
            directory=directory,
            batch_size=32,
            target_size=(360, 20),
            class_mode='categorical',
            color_mode='grayscale'
        )

        self.model_history = self.model.fit(
            x=self.all_images,
            epochs=epochs,
            batch_size=batch_size,
            steps_per_epoch=steps_per_epoch
        )

        self.model.save(
            filepath=data_save_path
        )

        return self.model_history

    def predict_count(
        self: 'PhotoCounter',
        file_path: Union[Path, str]
    ) -> int:

        img = image.load_img(
            path=file_path,
            target_size=(360, 20, 1),
            color_mode='grayscale'
        )        
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        output = self.model.predict(img)[0]
        output = np.argmax(output) + 2

        return output


LOCAL = Path(__file__).parent
a = PhotoCounter()
history = a.fit_from_directory(
    epochs=100,
    steps_per_epoch=407 // 32,
    batch_size=32,
    directory=LOCAL/'training_data'/'data_to_training_photo_counter',
    data_save_path='photo_counter_data.keras'
)

accuracy = history.history['accuracy']
loss = history.history['loss']
epochs = range(1, len(loss) + 1)

print(f'AVG accuracy: {np.average(accuracy)}')
print(f'MAX accuracy: {np.max(accuracy)}')
print(f'MIN accuracy: {np.min(accuracy)}')

print(f'AVG loss: {np.average(loss)}')
print(f'MAX loss: {np.max(loss)}')
print(f'MIN loss: {np.min(loss)}')

fig, axs = plt.subplots(
    nrows=1, ncols=2, 
    figsize=(12, 4)
)

axs[0].plot(
    epochs, 
    accuracy, 
    color='#035efc',
    linewidth=2
)
axs[0].grid(True)
axs[0].set_title('Accuracy')
axs[0].set_xlabel('Epoch')
axs[0].set_ylabel('Accuracy')

axs[1].plot(
    epochs, 
    loss, 
    color='#7205f7',
    linewidth=2
)
axs[1].grid(True)
axs[1].set_title('Loss')
axs[1].set_xlabel('Epoch')
axs[1].set_ylabel('Loss')

plt.tight_layout()
plt.show()

