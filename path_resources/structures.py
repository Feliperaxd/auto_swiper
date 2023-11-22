from pathlib import Path


class Directory:
    
    
    BASE_DIR = Path(__file__).parents[1]

    # Gui Resources
    GUI_RESOURCES = BASE_DIR / 'gui_resources'
    IMG = GUI_RESOURCES / 'img'

    # Networks
    NETWORKS = BASE_DIR / 'networks'
    TRAINING_DATA = NETWORKS / 'training_data'
    LEFT_SWIPES = TRAINING_DATA / 'left_swipes'
    RIGHT_SWIPES = TRAINING_DATA / 'right_swipes'

    # Paths Resources
    PATH_RESOURCES = BASE_DIR / 'path_resources'

    # Utilities
    UTILITIES = BASE_DIR / 'utilities'
    TEMP = UTILITIES / 'temp'
