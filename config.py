import os

CFG_PATH = '/config'
CFG_FILE_PATH = f"{CFG_PATH}/config.json"

STAT_DIR = 16384
STAT_FILE = 32768

def save():

    # make sure directory exists
    try:
        stat = os.stat(CFG_PATH)
        if stat[0] != STAT_DIR:
            os.remove(CFG_PATH)
            os.mkdir(CFG_PATH)
    except OSError:
        os.mkdir(CFG_PATH)

    # ok, lets write

def load():
    try:
        stat = os.stat(CFG_PATH)
        if stat[0] != STAT_FILE:
            print("config is not file.")
            return
    except OSError:
        print("No config! load failed.")
        return

    