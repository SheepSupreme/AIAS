from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
from ctktable import *
from errno import errorcode
import mysql.connector
from Spinbox import *
import serial
import threading

from MainFrameOrder import *
from MainFrameAddPackage import *
from MainFrameDashboard import *
from MainFrameDeletePackage import *
from MainFrameInventory import *
from Menu import *
from TopLeiste import *
from Dashboard_New import *
from package_to_issue import *


# serial_port = 'COM3'
# baud_rate = 9600
# ser = serial.Serial(serial_port, baud_rate, timeout=2)

def on_closing():
    if messagebox.askokcancel("Exit", "Are you sure you want to quit the application?"):
        root.destroy()
        exit()

class App(CTk):
    def __init__(self):
        #main setup
        super().__init__() 
        set_appearance_mode("dark")
        self._state_before_windows_set_titlebar_color = 'zoomed'
        self.title('Inventory')  
        self.protocol("WM_DELETE_WINDOW", on_closing)

        #layout 
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=15, uniform='a')


        self.topleiste = TopLeiste(self)
        self.menu = Menu(self, self.show_frameDashboard, self.show_frameInventory, self.show_frameAddPackage)
        self.MainFrame = None  # Um das aktuelle Frame-Objekt zu speichern

        self.show_frameDashboard()  # Zeige das Dashboard-Frame standardmäßig an


    
    def show_frameDashboard(self):
        if self.MainFrame:
            self.MainFrame.destroy()  # Zerstöre das aktuelle Frame, bevor du ein neues erstellst
        self.MainFrame = MainFrameDashboard(self)
 
    def show_frameInventory(self):
        if self.MainFrame:
            self.MainFrame.destroy()
        self.MainFrame = MainFrameInventory(self)

    def show_frameAddPackage(self):
        if self.MainFrame:
            self.MainFrame.destroy()
        self.MainFrame = MainFrameAddPackage(self)

#def serial_listener(port):
    # ser = serial.Serial(port, 9600)  # Serielle Schnittstelle öffnen

    # while True:
    #     if ser.in_waiting > 0:
    #         data = ser.readline().decode().strip()  # Daten von serieller Schnittstelle lesen
    #         if data:
    #             add_package_to_issue(data)


if __name__ == "__main__":

    # serial_thread = threading.Thread(target=serial_listener)
    # serial_thread.daemon = True  

    # serial_thread.start()

    root = App()
    root.mainloop()
    




        