import pyautogui
import tkinter as tk
from pathlib import Path
from PIL import ImageGrab, Image
from typing import Optional, Union
from gui_resources.resources import RootResouces


class SquareEye(RootResouces):


    def __init__(
        self: 'SquareEye',
        name: str,
        color: str,
        width: int,
        height: int,
        coord_x: Optional[int] = 0,
        coord_y: Optional[int] = 0,
        draggable: Optional[bool] = True, 
        border_thickness: Optional[int] = 5,
    ) -> None:
        
        # --Attributes!--
        self.name = name
        self.color = color
        self.width = width
        self.height = height
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.draggable = draggable
        self.border_thickness = border_thickness
        self.transparent_color = '#1f1f1f'
        # 4 is to discount the difference in pixels that form in the window!
        self.total_width = self.width + self.border_thickness * 2 + 4 
        self.total_height = self.height + self.border_thickness * 2 + 4

        self.viewing_area = (
            self.border_thickness,              # x1
            self.border_thickness,              # y1
            self.border_thickness + self.width, # x2
            self.border_thickness + self.height # y2
        )
        self.viewing_area_in_display = (
            self.viewing_area[0] + self.coord_x, # x1
            self.viewing_area[1] + self.coord_y, # y1
            self.viewing_area[2] + self.coord_x, # x2
            self.viewing_area[3] + self.coord_y  # y2
        )   
        self.root = tk.Tk()
        
        # Blank image to convert measurement unit!
        self._blank_image = tk.PhotoImage(
            master=self.root, width=1, height=1
        )
        self.root.geometry(
            f'{self.total_width}x{self.total_height}+{self.coord_x}+{self.coord_y}'
        )
        self.root.resizable(
            width=False, height=False
        )
        self.root.configure(
            background=self.color
        )
        self.root.wm_attributes(
            '-topmost', True
        )
        self.root.wm_attributes(
            '-transparentcolor', self.transparent_color
        )
        self.root.overrideredirect(True)        
        
        # --Supers!--
        RootResouces.__init__(self)

        # --Crosshair Engine!--
        # Square Left Top
        self.sqr_lt = tk.Label(
            master=self.root,
            image=self._blank_image,
            compound='c',
            background=self.transparent_color
        )
        # Square Right Top
        self.sqr_rt = tk.Label(
            master=self.root,
            image=self._blank_image,
            compound='c',
            background=self.transparent_color
        )
        # Square Left Bottom
        self.sqr_lb = tk.Label(
            master=self.root,
            image=self._blank_image,
            compound='c',
            background=self.transparent_color
        )
        # Square Right Bottom
        self.sqr_rb = tk.Label(
            master=self.root,
            image=self._blank_image,
            compound='c',
            background=self.transparent_color
        )
        self.crosshair(
            show_vertical_line=False,
            show_horizontal_line=False
        )
        
        # --Drag Engine!--
        self._dragging = False
        self._offset_x = 0
        self._offset_y = 0
        
        self.root.bind(
            sequence='<Button-1>', func=self._start_drag
        )
        self.root.bind(
            sequence='<Motion>', func=self._drag_sq
        )
        self.root.bind(
            sequence='<ButtonRelease-1>', func=self._stop_drag
        )
        
    def _start_drag(
        self: 'SquareEye',
        event: tk.Event
    ) -> None:
        
        self._dragging = True
        self._offset_x = event.x
        self._offset_y = event.y
        
    def _drag_sq(
        self: 'SquareEye',
        event: tk.Event
    ) -> None:

        if self.draggable:
            if self._dragging:
                self.coord_x = event.x_root - self._offset_x
                self.coord_y = event.y_root - self._offset_y
                self.root.geometry(f'+{self.coord_x}+{self.coord_y}')
            self.update_geometry_attributes()

    def _stop_drag(
        self: 'SquareEye',
        event: tk.Event
    ) -> None:
        
        self._dragging = False

    def crosshair(
        self: 'SquareEye',
        line_thickness: Optional[int] = 1,
        show_vertical_line: Optional[bool] = False,
        show_horizontal_line: Optional[bool] = False
    ) -> None:
        
        if show_vertical_line:
            self.sqr_width = self.width / 2 - line_thickness / 2 - 2
        else:
            self.sqr_width = self.width / 2
            
        if show_horizontal_line:
            self.sqr_height = self.height / 2 - line_thickness / 2 - 2    
        else:
            self.sqr_height = self.height / 2

        self.sqr_lt.configure(
            width=self.sqr_width,
            height=self.sqr_height
        )
        self.sqr_lt.place(
            x=self.viewing_area[0],
            y=self.viewing_area[1]
        )

        self.sqr_rt.configure(
            width=self.sqr_width,
            height=self.sqr_height
        )
        self.sqr_rt.place(
            x=self.viewing_area[2] - self.sqr_width,
            y=self.viewing_area[1]
        )
        
        self.sqr_lb.configure(
            width=self.sqr_width,
            height=self.sqr_height
        )
        self.sqr_lb.place(
            x=self.viewing_area[0],
            y=self.viewing_area[3] - self.sqr_height
        )

        self.sqr_rb.configure(
            width=self.sqr_width,
            height=self.sqr_height
        )
        self.sqr_rb.place(
            x=self.viewing_area[2] - self.sqr_width,
            y=self.viewing_area[3] - self.sqr_height
        )
         
    def update_geometry_attributes(
        self: 'SquareEye'
    ) -> None:
        
        self.coord_x = self.root.winfo_x()
        self.coord_y = self.root.winfo_y()

        # 4 is to discount the difference in pixels that form in the window!
        self.total_width = self.width + self.border_thickness * 2 + 4 
        self.total_height = self.height + self.border_thickness * 2 + 4

        self.viewing_area = (
            self.border_thickness,              # x1
            self.border_thickness,              # y1
            self.border_thickness + self.width, # x2
            self.border_thickness + self.height # y2
        )
        self.viewing_area_in_display = (
            self.viewing_area[0] + self.coord_x, # x1
            self.viewing_area[1] + self.coord_y, # y1
            self.viewing_area[2] + self.coord_x, # x2
            self.viewing_area[3] + self.coord_y  # y2
        )   

    def get_view(
        self: 'SquareEye',
        file_path: Optional[Union[Path, str]] = None
    ) -> Image.Image:

        self.update_geometry_attributes()

        image = ImageGrab.grab(
            bbox=self.viewing_area_in_display
        )
        if file_path is not None:
            image.save(file_path)
        
        return image
    
    def touch(
        self: 'SquareEye'
    ) -> None:
        
        self.update_geometry_attributes()

        pyautogui.FAILSAFE = False
        last_cursor_position = pyautogui.position()
    
        pyautogui.click(
            x=self.viewing_area_in_display[0] + self.width / 2,
            y=self.viewing_area_in_display[1] + self.height / 2
        )
        pyautogui.moveTo(
            x=last_cursor_position[0], 
            y=last_cursor_position[1]
        )
