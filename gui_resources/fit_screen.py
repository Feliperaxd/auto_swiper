from pathlib import Path
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap.constants import *
from path_resources.structures import Directory
from typing import Any, Callable, Optional, Union

from gui_resources.resources import RootResouces
from gui_resources.animated_gif import AnimatedGif
from gui_resources.custom_styles import CustomStyles


class FitScreen(CustomStyles, RootResouces):


    def __init__(
        self: 'FitScreen',
        name: str
    ) -> None:
    
        # --Attributes!--
        self.name = name
        self.root = ttk.Window(themename='tinderbotdark')
        self.root.geometry('400x600')
        self.root.wm_attributes('-topmost', True)
        self.root.resizable(
            width=False, height=False
        )

        # --Supers!--
        CustomStyles.__init__(self)
        RootResouces.__init__(self)

        # --Frames!--
        self.header_frame = ttk.Frame(
            master=self.root,
            height=50
        )
        self.header_frame.pack(fill=X)
        self.header_frame.propagate(False)
        
        self.photo_frame = ttk.Frame(
            master=self.root,
            height=250
        )
        self.photo_frame.pack(fill=X)
        self.photo_frame.propagate(False)

        self.choice_frame = ttk.Frame(
            master=self.root,
            height=200
        )
        self.choice_frame.pack(fill=X)
        self.choice_frame.propagate(False)

        self.footer_frame = ttk.Frame(
            master=self.root,
            height=100
        )
        self.footer_frame.pack(fill=X)
        self.footer_frame.propagate(False)

        # --Subframes!--
        self.left_frame = ttk.Frame(
            master=self.choice_frame,
            width=200
        ) 
        self.left_frame.pack(
            fill=Y, side=LEFT 
        )
        self.left_frame.propagate(False)

        self.right_frame = ttk.Frame(
            master=self.choice_frame,
            width=200
        ) 
        self.right_frame.pack(
            fill=Y, side=RIGHT 
        )
        self.right_frame.propagate(False)
        
        # --Header Frame Widgets!--
        """self.menu_btn = ttk.Button(
            master=self.header_frame,
            text='Menu',
            style='medium.info.TButton'
        )
        self.menu_btn.pack(side=RIGHT, padx=20)"""

        # --Photo Frame Widgets!--
        self.photo_container = ttk.Label(
            master=self.photo_frame
        )
        self.photo_container.pack()

        self.loading_gif = AnimatedGif(
            container=self.photo_container,
            file_path=Directory.IMG / 'loading_gif.gif'
        )

        # --Left Frame Widgets!--
        self.left_btn = ttk.Button(
            master=self.left_frame,
            text='No!',
            style='big.danger.TButton'
        )
        self.left_btn.pack(pady=30)
        
        self.left_meter = ttk.Meter(
            master=self.left_frame,
            metersize=100,
            metertype='semi',
            bootstyle=DANGER,
            amounttotal=100
        )
        self.left_meter.pack()

        # --Right Frame Widgets!--
        self.right_btn = ttk.Button(
            master=self.right_frame,
            text='Yep!',
            style='big.success.TButton'
        )
        self.right_btn.pack(pady=30)
        
        self.right_meter = ttk.Meter(
            master=self.right_frame,
            metersize=100,
            metertype='semi',
            bootstyle=SUCCESS,
            amounttotal=100
        )
        self.right_meter.pack()

        # --Footer Frame Widgets!--
        self.fit_btn = ttk.Button(
            master=self.footer_frame,
            text='Fit!',
            style='big.info.TButton'
        )
        self.fit_btn.pack(pady=25)

    def update_commands(
        self: 'FitScreen',
        left_btn_command: Callable[[Any], None],
        right_btn_command: Callable[[Any], None],
        fit_btn_command: Callable[[Any], None]
    ) -> None:
        
        self.left_btn.configure(
            command=left_btn_command
        )
        self.right_btn.configure(
            command=right_btn_command
        )
        self.fit_btn.configure(
            command=fit_btn_command
        )

    def loading(
        self: 'FitScreen'
    ) -> None:
        
        self.loading_gif.start()
        self.left_btn.configure(state=DISABLED)
        self.right_btn.configure(state=DISABLED)

    def change_photo(
        self: 'FitScreen',
        image: Optional[Union[Image.Image, Path, str]]
    ) -> None:

        self.left_btn.configure(state=ACTIVE)
        self.right_btn.configure(state=ACTIVE)
        self.loading_gif.stop()

        if isinstance(image, Path) or isinstance(image, str):
            self.profile_photo = Image.open(image)
        elif isinstance(image, Image.Image):
            self.profile_photo = image

        self.profile_photo = self.profile_photo.resize(size=(250, 250))

        self.profile_photo = ImageTk.PhotoImage(
            master=self.photo_frame,
            image=self.profile_photo
        )
        self.photo_container.configure(
            image=self.profile_photo
        )
