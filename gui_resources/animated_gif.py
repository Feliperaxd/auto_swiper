from pathlib import Path
import ttkbootstrap as ttk
from itertools import cycle
from typing import Optional, Union
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence



class AnimatedGif:


    def __init__(
        self: 'AnimatedGif', 
        container: ttk.Label,
        file_path: Union[Path, str]
    ) -> None:

        self.container = container
        self.file_path = file_path
        self.stop_animation = False

        with Image.open(self.file_path) as img:
            sequence = ImageSequence.Iterator(img)
            images = [ImageTk.PhotoImage(s) for s in sequence]
            self.image_cycle = cycle(images)
            self.framerate = img.info["duration"]

    def _next_frame(
        self: 'AnimatedGif'
    ) -> None:

        if self.stop_animation == False:
            self.container.configure(
                image=next(self.image_cycle)
            )
            self.container.after(
                ms=self.framerate, 
                func=self._next_frame
            )
    
    def start(
        self: 'AnimatedGif'
    ) -> None:
        
        self.stop_animation = False

        self.container.configure(
            image=next(self.image_cycle)
        )
        self.container.after(
            ms=self.framerate,
            func=self._next_frame
        )

    def stop(
        self: 'AnimatedGif'
    ) -> None:
        
        self.stop_animation = True  
    