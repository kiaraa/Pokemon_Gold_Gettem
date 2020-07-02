from abc import ABC

from pyboy import pyboy
from pyboy.__main__ import args, kwargs
from pyboy.pyboy import PyBoy, WindowEvent
import io
from pyboy.logger import logger
import PyBoyHandler.OpenEmulator
import pyboy.plugins.base_plugin
import sys


class InitialSaveGetter():

    def start_game(self):
        # for _ in range(660):
        #     self.pyboy_instance.tick()
        # print("reached tick 660")
        # self.pyboy_instance.send_input(WindowEvent.PRESS_BUTTON_START)
        # self.pyboy_instance.tick()
        # self.pyboy_instance.send_input(WindowEvent.RELEASE_BUTTON_START)
        # self.pyboy_instance.send_input(WindowEvent.PRESS_BUTTON_START)
        # self.pyboy_instance.tick()
        # self.pyboy_instance.send_input(WindowEvent.RELEASE_BUTTON_START)
        # for _ in range(60):
        #     self.pyboy_instance.tick()
        # self.pyboy_instance.send_input(WindowEvent.PRESS_BUTTON_A)
        # self.pyboy_instance.tick()
        # self.pyboy_instance.send_input(WindowEvent.RELEASE_BUTTON_A)
        # for _ in range(30):
        #     self.pyboy_instance.tick()
        # self.pyboy_instance.send_input(WindowEvent.PRESS_BUTTON_A)
        # self.pyboy_instance.tick()
        # self.pyboy_instance.send_input(WindowEvent.RELEASE_BUTTON_A)

        save_file = open("base_save_state.state", "rb")

        for _ in range(36):
            self.pyboy_instance.tick()
        #
        #
        self.pyboy_instance.load_state(save_file)

        print(self.pyboy_instance.get_memory_value(55850))

        save_file.close()

        # self.pyboy_instance.load_state(save_file)
        # save_file.close()

        while not self.pyboy_instance.tick():
            pass

    def __init__(self):
        self.pyboy_instance = PyBoy('../ROMs/gamerom.gbc')
        # while not self.pyboy_instance.tick():
        #     pass


if __name__ == '__main__':

    inital_save_getter = InitialSaveGetter()
    inital_save_getter.start_game()


