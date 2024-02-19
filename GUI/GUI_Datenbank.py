from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
from ctktable import *
from errno import errorcode
import mysql.connector
from Spinbox import *
import serial


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

class Menu(CTkFrame):
    def __init__(self, master,  cmd_dashboard, cmd_inventory, cmd_order, cmd_addPackage, cmd_deletePackage):
        super().__init__(master, fg_color="#FF99FF")
        
        self.grid(row=1, column=0, sticky="nsew", padx=5, pady=10)


        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure((1,2,3,4), weight=2, uniform='a')
        self.rowconfigure(5, weight=8, uniform='a')
        self.rowconfigure((6,7), weight=2, uniform='a')

    
        self.create_widgets(cmd_dashboard, cmd_inventory, cmd_order, cmd_addPackage, cmd_deletePackage)
       


    def create_widgets(self, cmd_dashboard, cmd_inventory, cmd_order, cmd_addPackage, cmd_deletePackage):

        button_menu_dashboard = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial",16, "bold"),
                                    anchor="w",
                                    text="Dashboard",
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    hover_color="#FFB7FF",
                                    command= cmd_dashboard)
        button_menu_dashboard.grid(row=1, column=0, sticky="nsew", padx=5, pady= 5)

        button_menu_inventory = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial",16, "bold"),
                                    anchor="w",
                                    text="Inventory",
                                    fg_color="transparent",
                                    hover_color="#FFB7FF",
                                    command=cmd_inventory)
        button_menu_inventory.grid(row=2, column=0, sticky="nsew", padx=5, pady= 5)

        button_menu_order = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial",16, "bold"),
                                    anchor="w",
                                    text="Order",
                                    fg_color="transparent",
                                    hover_color="#FFB7FF",
                                    command=cmd_order)
        button_menu_order.grid(row=3, column=0, sticky="nsew", padx=5, pady= 5)

        button_menu_addpackage = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial",16,"bold"),
                                    anchor="w",
                                    text="Add Package",
                                    fg_color="transparent",
                                    hover_color="#FFB7FF",
                                    command=cmd_addPackage)
        button_menu_addpackage.grid(row=4, column=0, sticky="nsew", padx=5, pady= 5)

        button_menu_deletepackage = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial", 16, "bold"),
                                    anchor="w",
                                    text="Delete Package",
                                    fg_color="transparent",
                                    hover_color="#FFB7FF",
                                    command=cmd_deletePackage)
        button_menu_deletepackage.grid(row=7, column=0, sticky="nsew", padx=5, pady= 5)

class Dashboard_New(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure(2, weight=32, uniform='a')
        self.rowconfigure(3, weight=32, uniform='a')

        self.create_headline()
        self.kapazity()
        self.ausgabe()
        self.steuerung()
        self.timer()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Dashboard", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=10)

    def kapazity(self):

        Kapazity_Box = CTkFrame(self, corner_radius=5 )
        Kapazity_Box.grid(column=0, row=2, sticky="nsew", pady=10, padx=10)

        Kapazity_Box.columnconfigure(0, weight=1, uniform='a')
        Kapazity_Box.columnconfigure(1, weight=1, uniform='a')
        Kapazity_Box.columnconfigure(2, weight=1, uniform='a')
        Kapazity_Box.rowconfigure(0, weight=1, uniform='a')
        Kapazity_Box.rowconfigure(1, weight=4, uniform='a')
        Kapazity_Box.rowconfigure(2, weight=1, uniform='a')

        headline = CTkLabel(Kapazity_Box, text="Auslastung", text_color= "#FF99FF", font=("Arial",24,"bold"))
        headline.grid(column= 0, row=0, columnspan=3, pady=2, padx=2, sticky="nsew")
        
        box1 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box1.grid(column=0, row=1, pady=2, padx=2, sticky="nsew")

        box2 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box2.grid(column=1, row=1, pady=2, padx=2, sticky="nsew")

        box3 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box3.grid(column=2, row=1, pady=2, padx=2, sticky="nsew")

        box1text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",24,"bold"))
        box1text.grid(column=0, row=2, pady=2, padx=2, sticky="nsew")

        box2text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",24,"bold"))
        box2text.grid(column=1, row=2, pady=2, padx=2, sticky="nsew")

        box3text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",24,"bold"))
        box3text.grid(column=2, row=2, pady=2, padx=2, sticky="nsew")

    def ausgabe(self):

        Ausgabe_Box = CTkFrame(self, corner_radius=5 )
        Ausgabe_Box.grid(column=0, row=3, sticky="nsew", pady=10, padx=10)

        Ausgabe_Box.columnconfigure(0, weight=1, uniform='a')
        Ausgabe_Box.rowconfigure(0, weight=2, uniform='a')
        Ausgabe_Box.rowconfigure(1, weight=4, uniform='a')
        Ausgabe_Box.rowconfigure(2, weight=4, uniform='a')

        headline = CTkLabel(Ausgabe_Box, text="Ausgabe", text_color= "#FF99FF", font=("Arial",24,"bold"))
        headline.grid(column= 0, row=0, columnspan=2, pady=2, padx=2, sticky="nsew")

        Spinbox = FloatSpinbox(Ausgabe_Box)
        Spinbox.grid(column=0, row= 1, sticky="ew")

        Button = CTkButton(Ausgabe_Box,
                            text= "Ausgeben!",
                            font=("Arial",24,"bold"),
                            fg_color = "#FF99FF",
                            text_color = "#990099",
                            hover_color="#FFB7FF")
        Button.grid(column=0, row=2, pady=(0,50), padx=20, sticky = "nsew")
        
    def steuerung(self):

        Steuerung_Box = CTkFrame(self, corner_radius=5 )
        Steuerung_Box.grid(column=1, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)

        Steuerung_Box.columnconfigure(0, weight=1, uniform='a')
        Steuerung_Box.rowconfigure(0, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(1, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(2, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(3, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(4, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(5, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(6, weight=1,uniform='a')

        headline = CTkLabel(Steuerung_Box, text="Steuerung", text_color="#FF99FF", font=("Arial",24, "bold"))
        headline.grid(column=0, row=0, sticky="nsew")

        class Button:
            def __init__(self,root,name,cmd,_row,_column):
                self.root = root
                self.name = name
                self.cmd = cmd
                self.button = customtkinter.CTkButton(master=self.root, text = self.name, command=self.send_text)
                self.button.grid(row = _row, column = _column, padx=10,pady=10, sticky="nsew")
            
            def send_text(self):
                print('sent')
            #     message = self.name
            #     print("message send:"+message)
            #     message_bytes = message.encode('ascii')
            #     ser.write(message_bytes)
            #     while True:
            #         text_mod = ser.readline()
            #         text = text_mod.decode().strip()
            #         print("message received:",text);
            #         if text == 'cmd_end': 
            #             break

        button_calibrate = Button(Steuerung_Box,'calibrate','calibration 50',1,0)
        button_blink = Button(Steuerung_Box,'blink','blink 0',2,0)
        button_pos1 = Button(Steuerung_Box,'move to pos_1', "pos_1 0",3,0)
        button_pos2 = Button(Steuerung_Box,'move to pos_2', "pos_2 0",4,0)
        button_pos3 = Button(Steuerung_Box,'move to pos_3', "pos_3 0",5,0)
        button_pos4 = Button(Steuerung_Box,'move to pos_4', "pos_4 0",6,0)


    def timer(self):

        timer_box = CTkFrame(self, corner_radius=5 )
        timer_box.grid(column=2, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)

        timer_box.columnconfigure(0, weight=1, uniform='a')
        timer_box.columnconfigure(1, weight=1, uniform='a')
        timer_box.rowconfigure(0, weight=1, uniform='a')
        timer_box.rowconfigure(1, weight=6, uniform='a')

        headline = CTkLabel(timer_box, text="Verfallszeit", text_color="#FF99FF", font=("Arial",24, "bold"))
        headline.grid(column=0, row=0, columnspan=2, sticky="nsew")

        def verfallszeit(self):
            

        
       

        

class TopLeiste(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#FF99FF", height=50, width=2000)

        self.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=1)
        
        
        #TopLeiste Grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=5, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')

        self.create_widgets()

    def create_widgets(self):
        
        #frame_text = CTkFrame(self)
        #frame_text.grid(column=0, row=0, sticky="nsew", pady=5, padx=5)

        label_text = CTkLabel(self, text="Datenbank System", text_color = "#990099", font=("Arial",16,"bold"))
        label_text.grid(column=0, row=0, sticky="nsew", pady=5, padx=5)

        button_konto = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial", 16, "bold"),
                                    anchor="e",
                                    text="Konto",
                                    fg_color="transparent",
                                    hover_color="#FFB7FF",
                                    width= 40)
        button_konto.grid(column=2, row=0, sticky="e", pady=5, padx=5)

class MainFrameDashboard(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure(2, weight=24, uniform='a')
        self.rowconfigure(3, weight=40, uniform='a')

        self.create_headline()
        self.create_Table()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Dashboard", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=10)


        
    def create_Table(self):


         
        frame_table = CTkFrame(self, fg_color="transparent", bg_color="transparent")
        frame_table.grid(column=0, row = 2, columnspan=3, sticky="nsew", pady=10, padx=20)

        frame_table.columnconfigure(0, weight=80, uniform='a')
        frame_table.columnconfigure(1, weight=1, uniform='a')
        frame_table.rowconfigure(0, weight=1, uniform='a')

        
        
        tafel_1 = ttk.Treeview(frame_table, columns=(1,2,3,4,5,6,7), show="headings", height="20")
        
        for i in range(8):
            
            tafel_1.column(column=i, anchor="center")

        
        style_table = ttk.Style(tafel_1)
        style_table.theme_use("default")
        style_table.configure("Treeview.Heading", rowheight=25, font=("ARIAL Bold", 20), foreground="Black", background="#FFB9FF")
        style_table.configure("Treeview", rowheight=25, font=("ARIAL", 14), foreground="Black", background="#FFCDFF", fieldbackground="#FFCDFF", anchor="center")
        style_table.map("Treeview", 
                  background=[('selected','White')],
                  foreground=[('selected','black')])
        
        tafel_1.grid(column=0, row=0, sticky="nsew", pady=10)
        
        tafel_1.heading(1, text="Paket-ID")
        tafel_1.heading(2, text="QR-Code")
        tafel_1.heading(3, text="Colour")
        tafel_1.heading(4, text="Weight")
        tafel_1.heading(5, text="Shelf_ID")
        tafel_1.heading(6, text="Max_Cap")
        tafel_1.heading(7, text="Cur_Cap")
        

        tafel_1.column(1, width=60)
        tafel_1.column(2, width=60)
        tafel_1.column(3, width=60)
        tafel_1.column(4, width=60)
        tafel_1.column(5, width=60)
        tafel_1.column(6, width=60)
        tafel_1.column(7, width=60)
        
        
        for i in range(100):
            tafel_1.insert(parent='', index=[i], values=(i,'0010','Red','0.5kg','2','4','2'))
        
        laufleiste = ttk.Scrollbar(frame_table, orient="vertical",
        command=tafel_1.yview)

        style_scrollbar = ttk.Style(laufleiste)
        style_scrollbar.configure("Vertical.TScrollbar", background="#FFCDFF", foreground="White")
        laufleiste.grid(column=1, row=0, sticky="nsew", pady=10)
        
        tafel_1.configure(yscrollcommand=laufleiste.set)

        

        for i in range(4):
            PaketID = i

            Query = '''SELECT PT.QRCode, PT.Colour, PT.Weight_kg, PT.Shelf_ID, PS.Capacity_Max, PI.Quantity_Current 
            FROM inventory.tfact_packageinventory as PI
            INNER JOIN inventory.tdim_packagetype as PT
            INNER JOIN inventory.tdim_shelf as PS
            ON     PI.Shelf_ID = PT.Shelf_ID = PS.Shelf_ID
            WHERE  PT.PackageType_ID = "%s"''' %PaketID 

            cursor.execute(Query)

            for row in cursor:
                
                QRCode = str(row[0])
                Colour = str(row[1])
                Weight = str(row[2])
                Shelf_ID = str(row[3])
                Capacity_Max = str(row[4])
                Quantity_Current = str(row[5])

                
                tafel_1.insert(parent='', index=[i], values=(i, "%s"%QRCode,"%s" %Colour,"%s" %Weight,"%s" %Shelf_ID, "%s" %Capacity_Max, "%s" %Quantity_Current))

class MainFrameOrder(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure((2,3), weight=32, uniform='a')

        self.create_headline()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Order", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=10)

class MainFrameInventory(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure((2,3), weight=32, uniform='a')

        self.create_headline()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Inventory", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=10)

class MainFrameAddPackage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure((2,3), weight=32, uniform='a')

        self.create_headline()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Add Package", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=10) 

class MainFrameDeletePackage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure((2,3), weight=32, uniform='a')

        self.create_headline()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Delete Package", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=10) 


# Verbindungsinformationen
host = "127.0.0.1"
user = "userdb"
password = "userdb"
database = "inventory"  

# Verbindung herstellen
try:
    conn = mysql.connector.connect(host=host,user=user,password=password)
    print("Connection established")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()



App()