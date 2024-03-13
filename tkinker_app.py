# for the tkinter application
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ctypes
# we need 'Path' for the exe file only
from pathlib import Path
# main function to convert avi videos to mp4 videos using codec='libx265'
from convert import convert_avi_to_mp4
# appearance settings
from app_settings import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        ##############
        # icon of the app in the app window -- we use Path(__file__) only for the exe file
        self.iconbitmap(Path(__file__).parent / 'logo.ico')
        # Set the icon for the taskbar
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('convertor')
        self.set_taskbar_icon('logo.ico')  # see 'set_taskbar_icon' function
        ##############

        # app title
        self.title('Конвертация видео из AVI в MP4')

        #########
        # geometry of the app
        #########
        self.geometry(str(length) + 'x' + str(height))  # see app_settings.py
        self.minsize(length, height)  # see app_settings.py
        self.resizable(True, False)  # allow the window to be resizable only alongside the 'x' direction
        # make sure that our columns have the weight
        self.columnconfigure(0, weight=1)  # Make column 0 resizable
        self.columnconfigure(1, weight=1)  # Make column 1 resizable
        self.columnconfigure(2, weight=1)  # Make column 2 resizable
        self.rowconfigure(0, weight=1)  # Make row 0 resizable
        self.rowconfigure(1, weight=1)  # Make row 1 resizable
        self.rowconfigure(3, weight=1)  # Make row 3 resizable

        # color of the background
        self['bg'] = background_color  # see app_settings.py

        #########
        # elements of an app
        #########
        # main label
        self.main_label = Label(self, text='Введите путь до папки с файлами AVI', font=('Arial', 14),
                                background=background_color)
        self.main_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='ew')

        # area for the entry path
        self.path_for_folder_of_avi_files = Entry(self, background=background_color)
        self.path_for_folder_of_avi_files.grid(row=1, column=0, columnspan=4, ipadx=100, padx=5, pady=5, sticky='ew')

        # bitrate label
        self.bitrate_label = Label(self, text='Битрейт', background=background_color)
        self.bitrate_label.grid(row=3, column=0, padx=5, pady=5)

        # bitrate variable - see app_settings.py to find bitrate massive
        self.bitrate_var = StringVar(value=bitrate[3])
        # bitrate combobox
        self.bitrate_combobox = ttk.Combobox(self, textvariable=self.bitrate_var, values=bitrate,
                                             background=background_color)
        self.bitrate_combobox.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

        # button to evaluate the 'convert_avi_to_mp4' function
        self.button = tk.Button(self, text='Конвертировать', width=15, command=self.button_clicked,
                                background=background_color)
        self.button.grid(row=3, column=2, padx=5, pady=5)
        #########
        # to make ctrl-c and ctrl-v work in Russian
        #########
        self.language = 'ru'  # Default language is Russian
        self.main_label.bind('<Button-1>', self.switch_language)  # pressing main_label switches the language
        self.bind_all('<Key>', self.add_ctrl_v_and_c_to_the_russian, '+')

    # function "convert_avi_to_mp4" (see convert.py) is called to convert avi files to mp4 files
    def button_clicked(self):
        message = convert_avi_to_mp4(self.path_for_folder_of_avi_files.get(), self.bitrate_combobox.get(),
                                     self.language)
        if message[0]:  # this is the _error_(True or False)
            messagebox.showerror(message[1], message[2])
        else:
            messagebox.showinfo(message[1], message[2])

    # function to switch the language if there was a click on the upper label, i.e., 'main_label'
    def switch_language(self, event):
        if self.language == 'ru':
            self.title('Convert video from AVI to MP4')
            self.main_label['text'] = 'Enter the path to the AVI folder'
            self.bitrate_label['text'] = 'Bitrate'
            self.button['text'] = 'Convert'
            self.language = 'en'
        else:
            self.title('Конвертация видео из AVI в MP4')
            self.main_label['text'] = 'Введите путь до папки с файлами AVI'
            self.bitrate_label['text'] = 'Битрейт'
            self.button['text'] = 'Конвертировать'
            self.language = 'ru'

    # function to make ctrl-c and ctrl-v work in Russian
    @staticmethod
    def add_ctrl_v_and_c_to_the_russian(event):
        ctrl = (event.state & 0x4) != 0
        if event.keycode == 88 and ctrl and event.keysym.lower() != 'x':
            event.widget.event_generate('<<Cut>>')

        if event.keycode == 86 and ctrl and event.keysym.lower() != 'v':
            event.widget.event_generate('<<Paste>>')

        if event.keycode == 67 and ctrl and event.keysym.lower() != 'c':
            event.widget.event_generate('<<Copy>>')

    #  setting taskbar icon
    def set_taskbar_icon(self, icon_path):
        try:
            import winreg
        except ImportError:
            import _winreg as winreg

        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                               "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Taskband")
        winreg.SetValueEx(key, "IconPath", 0, winreg.REG_SZ, icon_path)
        winreg.SetValueEx(key, "IconIndex", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
