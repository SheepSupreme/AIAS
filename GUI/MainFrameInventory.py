from customtkinter import *
import time
from tkinter import messagebox
from customtkinter import *
import datetime as dt
from tkcalendar import *
import mysql.connector
from errno import errorcode
from datetime import datetime, timedelta
import qrcode
import png
from PIL import Image, ImageTk

host = "127.0.0.1"
user = "userdb"
password = "userdb"
database = "aks" 

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


class MainFrameInventory(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure((2,3), weight=32, uniform='a')

        self.create_headline()
        self.table1()
        self.table2()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Inventory", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=0, row=0, columnspan=2, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=10)

    def table1(self):
        package_table_frame = CTkFrame(self, corner_radius=5)
        package_table_frame.grid(column=0, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)
        package_table_frame.columnconfigure(0, weight=1, uniform='a')
        package_table_frame.rowconfigure(0, weight=1, uniform='a')
        package_table_frame.rowconfigure(1, weight=10, uniform='a')

        storage_label = CTkLabel(package_table_frame, text="Package Storage", text_color="#FF99FF",
                                 font=("Arial", 24, "bold"))
        storage_label.grid(column=0, row=0, columnspan=2, sticky="nsew", pady=5, padx=5)

        table = CTkScrollableFrame(package_table_frame, corner_radius=5)
        table.grid(column=0,row=1, pady=10, padx=10, sticky="nsew")
        table.columnconfigure(0,weight=1)
        
        #scrollbar = CTkScrollbar(package_table_frame, orientation="vertical")
        #scrollbar.grid(column=1, row=1, rowspan=9, sticky="nsew")




        class TimerEntry:
            def __init__(self, end_time, ID):
                self.container = CTkFrame(master=table, corner_radius=5, border_width=1)
                self.container.grid(row=0, column=0, sticky='nswe', pady=(5,0), padx=5)
                self.ID = ID
                self.end_time = end_time
                self.current_time = end_time - datetime.now()
                self.container.columnconfigure((0,1), weight=2, uniform='a')
                self.container.columnconfigure((2,3), weight=1, uniform='a')
                self.container.rowconfigure(0, weight=1,  uniform='a')
                self.label1 = CTkLabel(self.container,font=('Arial', 20))
                self.label1.grid(column=0, row=0,padx=5, pady=5, sticky="nsew")
                self.label2 = CTkLabel(self.container, font=('Arial', 20))
                self.label2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
                self.qr_button = CTkButton(self.container, text="QR-Code", command=self.generate_qr)
                self.qr_button.grid(row=0, column=2, padx=5, pady=5)
                self.info_button = CTkButton(self.container, text="Info", command=self.info)
                self.info_button.grid(row=0, column=3, padx=5, pady=5)
                self.update()

            def update(self):
                self.current_time = self.end_time - datetime.now()
                seconds = self.current_time.total_seconds()
                self.label2.configure(text=int(seconds))
                self.label1.configure(text=self.ID)
                if seconds < 0:
                    self.label2.configure(bg_color='red')
                self.container.after(1000, self.update)

            
            def info(self):
                label_text = self.label1.cget("text")

                query = "SELECT issue_datetime, content_1, content_2 FROM aks.tdim_inventory WHERE ID = %s" %label_text
                cursor.execute(query)
                results = cursor.fetchall()

                for row in results:
                    issue_datetime = row [0]
                    content1 = row[1]
                    content2 = row[2]

                message = (
                    f"Package ID: {label_text}\n"
                    f"Datetime for Issue: {issue_datetime}\n"
                    f"1. Content: {content1}\n"
                    f"2. Content: {content2}"
                )

                messagebox.showinfo(
                    title="INFO",
                    message=message
                )

            def generate_qr(self):
                label_text = self.label1.cget("text")

                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(label_text)
                qr.make(fit=True)
                qr_image = qr.make_image(fill='black', back_color='white')


                qr_image.show()
                    


        def get_endtimes_from_db():
            query = "SELECT issue_datetime FROM aks.tdim_inventory"
            cursor.execute(query)
            results = cursor.fetchall()
            conn.commit()
            return [result[0] for result in results] if results else []

        def get_Id_from_db():
            query= "SELECT ID FROM aks.tdim_inventory"
            cursor.execute(query)
            results = cursor.fetchall()
            conn.commit()
            return [result[0] for result in results] if results else []



        def add_timer_from_db():
            end_times = get_endtimes_from_db()
            Ids = get_Id_from_db()

            for i, (end_time, ID) in enumerate(zip(end_times, Ids), start=1):
                TimerEntry(end_time, ID).container.grid(row=i, column=0, sticky='nswe')
            
            self.after(5000, add_timer_from_db)
            

        add_timer_from_db()

    def table2(self):
       
        package_table_frame = CTkFrame(self, corner_radius=5)
        package_table_frame.grid(column=1, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)
        package_table_frame.columnconfigure(0, weight=1, uniform='a')
        package_table_frame.rowconfigure(0, weight=1, uniform='a')
        package_table_frame.rowconfigure(1, weight=10, uniform='a')

        storage_label = CTkLabel(package_table_frame, text="Issue-System", text_color="#FF99FF",
                                 font=("Arial", 24, "bold"))
        storage_label.grid(column=0, row=0, columnspan=2, sticky="nsew", pady=5, padx=5)

        table = CTkScrollableFrame(package_table_frame, corner_radius=5)
        table.grid(column=0,row=1, pady=10, padx=10, sticky="nsew")
        table.columnconfigure(0,weight=1)

        class TimerEntry:
            def __init__(self, end_time, ID):
                self.container = CTkFrame(master=table, corner_radius=5, border_width=1)
                self.container.grid(row=0, column=0, sticky='nswe', pady=(5,0), padx=5)
                self.ID = ID
                self.end_time = end_time
                self.current_time = end_time - datetime.now()
                self.container.columnconfigure((0,1), weight=2, uniform='a')
                self.container.columnconfigure(2, weight=1, uniform='a')
                self.container.rowconfigure(0, weight=1, uniform='a')
                self.label1 = CTkLabel(self.container,font=('Arial', 20))
                self.label1.grid(column=0, row=0,padx=5, pady=5, sticky="nsew")
                self.label2 = CTkLabel(self.container, font=('Arial', 20))
                self.info_button = CTkButton(self.container, text="Info", command=self.info)
                self.info_button.grid(row=0, column=2, padx=5, pady=5)
                self.label2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
                self.update()

            def update(self):
                self.current_time = self.end_time - datetime.now()
                seconds = self.current_time.total_seconds()
                self.label2.configure(text=int(seconds))
                self.label1.configure(text=self.ID)
                if seconds < 0:
                    self.label2.configure(bg_color='red')
                self.container.after(1000, self.update)

            def info(self):
                label_text = self.label1.cget("text")

                query = "SELECT issue_datetime, content_1, content_2 FROM aks.tdim_inventory WHERE ID = %s" %label_text
                cursor.execute(query)
                results = cursor.fetchall()

                for row in results:
                    issue_datetime = row [0]
                    content1 = row[1]
                    content2 = row[2]
                
                query = "SELECT position_x, position_y FROM aks.tfact_issue_inventory WHERE ID = %s" %label_text
                cursor.execute(query)
                results = cursor.fetchall()

                for row in results:
                    x = row[0]
                    y = row[1]
                    
                message = (
                    f"Package ID: {label_text}\n"
                    f"Datetime for Issue: {issue_datetime}\n"
                    f"1. Content: {content1}\n"
                    f"2. Content: {content2}\n"
                    f"Regal: {x}\n"
                    f"Höhe: {y}"
                )

                messagebox.showinfo(
                    title="INFO",
                    message=message
                )


        def get_endtimes_from_db():
            query = "SELECT issue_datetime FROM aks.tfact_issue_inventory"
            cursor.execute(query)
            results = cursor.fetchall()
            conn.commit()
            return [result[0] for result in results] if results else []
        
        def get_Id_from_db():
            query = "SELECT ID FROM aks.tfact_issue_inventory"
            cursor.execute(query)
            results = cursor.fetchall()
            conn.commit()
            return [result[0] for result in results] if results else []
        

        def add_timer_from_db():
            end_times = get_endtimes_from_db()
            Ids = get_Id_from_db()

            for i, (end_time, ID) in enumerate(zip(end_times, Ids), start=1):
                TimerEntry(end_time, ID).container.grid(row=i, column=0, sticky='nswe')
        
            self.after(5000, add_timer_from_db)
                                
            
        add_timer_from_db()
            
