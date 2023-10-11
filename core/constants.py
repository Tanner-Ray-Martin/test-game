import os

CONSTANTS_NAME = __file__

CONSTANTS_PATH = os.path.abspath(CONSTANTS_NAME)

CORE_DIR = CONSTANTS_PATH.replace(os.path.basename(CONSTANTS_PATH), "")

SPLIT_CORE_DIR = CORE_DIR.split(os.sep)

SPLIT_GAME_DIR = SPLIT_CORE_DIR[:-2]

GAME_DIR = os.sep.join(SPLIT_GAME_DIR)

RESOURCE_DIR = os.path.join(GAME_DIR, "resources")

TILES_DIR = os.path.join(RESOURCE_DIR, "Tiles")
