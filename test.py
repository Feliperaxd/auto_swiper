from utilities.utils import Utils
from path_resources.structures import *

print(
    Utils.get_data(
        data_key=['coordinates', 'fit_screen'],
        file_path=Directory.GUI_RESOURCES / 'config.json'
    )
)