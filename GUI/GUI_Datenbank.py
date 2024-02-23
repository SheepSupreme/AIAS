from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
from ctktable import *
from errno import errorcode
import mysql.connector
from Spinbox import *
import serial

from MainFrameOrder import *
from MainFrameAddPackage import *
from MainFrameDashboard import *
from MainFrameDeletePackage import *
from MainFrameInventory import *
from Menu import *
from TopLeiste import *
from Dashboard_New import *


# serial_port = 'COM3'
# baud_rate = 9600
# ser = serial.Serial(serial_port, baud_rate, timeout=2)

class App(CTk):
    def __init__(self):

        #main setup
        super().__init__() 
        set_appearance_mode("dark")
        self._state_before_windows_set_titlebar_color = 'zoomed'
        self.title('Inventory')  

        #layout 
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=15, uniform='a')


        self.topleiste = TopLeiste(self)
        self.menu = Menu(self, self.show_frameDashboard, self.show_frameInventory, self.show_frameOrder, self.show_frameAddPackage, self.show_frameDeletePackage)
        self.MainFrame = None  # Um das aktuelle Frame-Objekt zu speichern

        self.show_frameDashboard()  # Zeige das Dashboard-Frame standardmäßig an

        
        self.mainloop()
    
    def show_frameDashboard(self):
        if self.MainFrame:
            self.MainFrame.destroy()  # Zerstöre das aktuelle Frame, bevor du ein neues erstellst
        self.MainFrame = Dashboard_New(self)

    def show_frameInventory(self):
        if self.MainFrame:
            self.MainFrame.destroy()
        self.MainFrame = MainFrameInventory(self)

    def show_frameOrder(self):
        if self.MainFrame:
            self.MainFrame.destroy()
        self.MainFrame = MainFrameOrder(self)

    def show_frameAddPackage(self):
        if self.MainFrame:
            self.MainFrame.destroy()
        self.MainFrame = MainFrameAddPackage(self)

    def show_frameDeletePackage(self):
        if self.MainFrame:
            self.MainFrame.destroy()
        self.MainFrame = MainFrameDeletePackage(self)


App()