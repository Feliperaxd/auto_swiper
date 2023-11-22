from pathlib import Path
from gui_resources.commands import Commands
from gui_resources.fit_screen import FitScreen
from gui_resources.square_eye import SquareEye

LOCAL = Path(__file__).parent

if __name__ == '__main__':
    fit_screen = FitScreen('fit_screen')
    fit_screen.restore_position()

    photo_eye = SquareEye(
        name='photo_eye',
        color='blue',
        width=360,
        height=360,
        border_thickness=8
    )
    photo_eye.restore_position()

    left_eye = SquareEye(
        name='left_eye',
        color='red',
        width=50,
        height=50,
        border_thickness=8
    )
    left_eye.restore_position()

    right_eye = SquareEye(
        name='right_eye',
        color='green',
        width=50,
        height=50,
        border_thickness=8
    )
    right_eye.restore_position()

    commands = Commands(
        left_eye=left_eye,
        right_eye=right_eye,
        photo_eye=photo_eye,
        fit_screen=fit_screen    
    )
    fit_screen.update_commands(
        left_btn_command=commands.left_swipe,
        right_btn_command=commands.right_swipe,
        fit_btn_command=commands.fit_it
    )
    
    while True:
        
        commands.get_and_show_profile_photo()
        fit_screen.root.update()
