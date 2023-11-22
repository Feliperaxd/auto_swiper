import os, time, shutil
from pathlib import Path
from utilities.utils import Utils
from typing import Union, Optional
from path_resources.structures import *
from gui_resources.square_eye import SquareEye
from gui_resources.fit_screen import FitScreen


class Commands:
    

    def __init__(
        self: 'Commands',
        left_eye: Optional[SquareEye] = None,
        right_eye: Optional[SquareEye] = None,
        photo_eye: Optional[SquareEye] = None,
        fit_screen: Optional[FitScreen] = None
    ) -> None:
        
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.photo_eye = photo_eye
        self.fit_screen = fit_screen        

    def get_and_show_profile_photo(
        self: 'Commands'
    ) -> None:

        image = self.photo_eye.get_view()
        self.fit_screen.change_photo(image)

    def update_widgets(
        self: 'Commands'
    ) -> None:
        
        self.fit_screen.left_meter.configure(
            amountused=len(os.listdir(Directory.LEFT_SWIPES))
        )
        self.fit_screen.right_meter.configure(
            amountused=len(os.listdir(Directory.RIGHT_SWIPES))
        )

    def left_swipe(
        self: 'Commands',
    ) -> None:
        
        self.photo_eye.get_view(
            Directory.TEMP / 'temp.png'
        )
        self.left_eye.touch()
        name = Utils.rename_like_last(
            directory=Directory.LEFT_SWIPES,
            file_name='left',
            file_extension='.png'
        )
        os.rename(
            Directory.TEMP / 'temp.png',
            Directory.TEMP / name
        )
        shutil.move(
            Directory.TEMP / name,
            Directory.RIGHT_SWIPES / name
        )

        time.sleep(0.7)
        self.update_widgets()     

    def right_swipe(
        self: 'Commands',
    ) -> None:

        self.photo_eye.get_view(
            Directory.TEMP / 'temp.png'
        )
        self.left_eye.touch()
        name = Utils.rename_like_last(
            directory=Directory.RIGHT_SWIPES,
            file_name='right',
            file_extension='.png'
        )
        os.rename(
            Directory.TEMP / 'temp.png',
            Directory.TEMP / name
        )
        shutil.move(
            Directory.TEMP / name,
            Directory.RIGHT_SWIPES / name
        )

        time.sleep(0.7)
        self.update_widgets()
        
    def fit_it(
        self: 'Commands'
    ) -> None:
        
        self.update_widgets()
        self.fit_screen.save_position()
        self.anchor()

    def anchor(
        self: 'Commands'
    ) -> None:

        self.left_eye.save_position()
        self.right_eye.save_position()
        self.photo_eye.save_position()
        self.fit_screen.save_position()
