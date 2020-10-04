from pyboy import pyboy
from pyboy.pyboy import PyBoy, WindowEvent
import io

if __name__ == '__main__':

    pyboy = PyBoy('../ROMs/gamerom.gbc')
    state = open("gamerom.gbc.state", "rb")
    pyboy.load_state(state)

    while not pyboy.tick():
        pass