from customtkinter import *
import mysql.connector
from tkinter import ttk
from errno import errorcode

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