from pyboy import pyboy
from pyboy.pyboy import PyBoy, WindowEvent

if __name__ == '__main__':

    pyboy = PyBoy('ROMs/gamerom.gbc')
    while not pyboy.tick():
        pass