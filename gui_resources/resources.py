from typing import Type
from utilities.utils import Utils
from path_resources.structures import Directory

class RootResouces:


    def __init__(
        self: Type['RootResouces']
    ) -> None:
        pass

    def restore_position(
        self: Type['RootResouces']
    ) -> None:

        coord_x, coord_y = Utils.get_data(
            data_key=['coordinates', self.name],
            file_path=Directory.GUI_RESOURCES / 'config.json'
        )
        self.root.geometry(
            f'+{coord_x}+{coord_y}'
        )
    
    def save_position(
        self: Type['RootResouces']
    ) -> None:
        
        Utils.save_data(
            data=(self.root.winfo_rootx(), self.root.winfo_rooty()),
            data_key=['coordinates', self.name],
            file_path=Directory.GUI_RESOURCES / 'config.json'
        )
