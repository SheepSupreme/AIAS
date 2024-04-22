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

class MainFrameAddPackage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure((2,3), weight=32, uniform='a')

        self.create_headline()
        self.create_package()
        self.package_tabel()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Add Package", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=0, row=0, columnspan=2, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=10) 

    def create_package(self):


        create_package_frame = CTkFrame(self, corner_radius= 5)
        create_package_frame.grid(column= 0, row = 2, rowspan=2, sticky="nsew", pady=10, padx=10)

        create_package_frame.columnconfigure(0, weight=1, uniform='a')
        # create_package_frame.columnconfigure(1, weight=8, uniform='a')
        create_package_frame.rowconfigure(0, weight=2, uniform='a')
        create_package_frame.rowconfigure(1, weight=6, uniform='a')
        create_package_frame.rowconfigure(2, weight=8, uniform='a')
        create_package_frame.rowconfigure(3, weight=2, uniform='a')


        add_package = CTkLabel(create_package_frame, text="New Package:", text_color= "#FF99FF",  font=("Arial",24,"bold"))
        add_package.grid(column=0, row=0, sticky="nsew", pady=5, padx=5)


        inhalt_frame = CTkFrame(create_package_frame, corner_radius=5)
        inhalt_frame.grid(column=0, row=1, sticky = "nsew", pady=10, padx=10)

        inhalt_frame.columnconfigure(0, weight=1, uniform='a')
        inhalt_frame.columnconfigure(1, weight=2, uniform='a')
        inhalt_frame.rowconfigure(0, weight=1, uniform='a')
        inhalt_frame.rowconfigure(1, weight=1, uniform='a')


        inhalt1_label = CTkLabel(inhalt_frame, text="1. Content:", text_color= "#FF99FF",  font=("Arial",16,"bold"))
        inhalt1_label.grid(column=0, row=0, sticky="nsew")

        inhalt1_entry = CTkEntry(inhalt_frame)
        inhalt1_entry.grid(column=1, row=0, sticky="nsew", pady=10, padx=10)

        inhalt2_label = CTkLabel(inhalt_frame, text="2. Content:", text_color= "#FF99FF",  font=("Arial",16,"bold"))
        inhalt2_label.grid(column=0, row=1, sticky="nsew")

        inhalt2_entry = CTkEntry(inhalt_frame)
        inhalt2_entry.grid(column=1, row=1, sticky="nsew", pady=10, padx=10)

        datetime_frame = CTkFrame(create_package_frame, corner_radius=5)
        datetime_frame.grid(column=0 , row= 2, sticky="nsew", pady=10, padx=10)

        datetime_frame.columnconfigure(0, weight=1, uniform='a')
        datetime_frame.columnconfigure(1, weight=2, uniform='a')
        datetime_frame.rowconfigure((0,1), weight=1, uniform='a')
        datetime_frame.rowconfigure(2, weight=1, uniform='a')

        Datum = CTkLabel(datetime_frame, text="Date:", text_color= "#FF99FF",  font=("Arial",16,"bold"))
        Datum.grid(column=0, row=0, sticky="nsew", pady=10, padx=10)

        Uhrzeit = CTkLabel(datetime_frame, text="Time:", text_color="#FF99FF", font=("Arial",16,"bold"))
        Uhrzeit.grid(column=0, row=1, sticky="nsew", pady=10, padx=10)

        DatumEntry = CTkEntry(datetime_frame)
        DatumEntry.grid(column=1, row=0, sticky="nsew", pady=10, padx=10)

        UhrzeitEntry = CTkEntry(datetime_frame)
        UhrzeitEntry.grid(column=1, row=1, sticky="nsew", pady=10, padx=10)

        def cal_get():
            
            datetime_choose = CTk()
            datetime_choose.title("Datetime")
            datetime_choose.geometry("400x400")

            datetime_choose.columnconfigure(0, weight=1, uniform='a')
            datetime_choose.columnconfigure(1, weight=2, uniform='a')
            datetime_choose.rowconfigure(0, weight=1, uniform='a')
            datetime_choose.rowconfigure(1, weight=4, uniform='a')
            datetime_choose.rowconfigure(2, weight=2, uniform='a')
            datetime_choose.rowconfigure(3, weight=2, uniform='a')
            

            Headline = CTkLabel(datetime_choose, text="Select Datetime:", text_color= "#FF99FF",  font=("Arial",16,"bold"))
            Headline.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=20)

            current_date = dt.date.today()
            current_year = current_date.strftime("%Y")
            current_month = current_date.strftime("%m")
            current_day = current_date.strftime("%d")
            current_time = dt.datetime.today()
            current_hour = current_time.strftime("%H")
            current_min = current_time.strftime("%M") 
            current_sec = current_time.strftime("%S")

            cal = Calendar(datetime_choose, selectmode = 'day', date_pattern ="yyyy-mm-dd",
                year = int(current_year), month = int(current_month),
                day = int(current_day))
            
            cal.grid(column= 0, row=1, columnspan=2, pady = 20, padx=20, sticky="nsew")


            Time_Frame = CTkFrame(datetime_choose, corner_radius= 5)
            Time_Frame.grid(column=0, row=2, columnspan= 2, sticky="nsew", pady=10, padx=10)

            Time_Frame.columnconfigure(0, weight=1, uniform='a')
            Time_Frame.columnconfigure(1, weight=3, uniform='a')
            Time_Frame.rowconfigure(0, weight=1, uniform='a')

            Time_Label = CTkLabel(Time_Frame, text="Uhrzeit:", text_color= "#FF99FF",  font=("Arial",16,"bold"))
            Time_Label.grid(column=0, row=0, sticky="nsew", pady=10, padx=10)

            Entry_Frame = CTkFrame(Time_Frame, corner_radius=5)
            Entry_Frame.grid(column=1, row=0, sticky = "nsew", pady=10, padx=10)

            Entry_Frame.columnconfigure((0,1,2), weight=1, uniform='a')
            Entry_Frame.rowconfigure(0, weight=4, uniform='a')
            Entry_Frame.rowconfigure(1, weight=1, uniform='a')
            
            hour_label = CTkLabel(Entry_Frame, text="Stunde", font=("Arial",8))
            hour_label.grid(column=0, row=1, sticky="nsew", padx=(10,0), pady=(0,2))

            Entry_hour = CTkEntry(Entry_Frame,
                                    placeholder_text=current_hour,
                                    bg_color="transparent",
                                    fg_color="transparent",
                                    corner_radius=0,
                                    border_color="Grey",
                                    justify = "center")
            Entry_hour.grid(column=0, row=0, sticky="nsew", pady=(10,2), padx=(10,0))

            min_label = CTkLabel(Entry_Frame, text="Minute", font=("Arial",8))
            min_label.grid(column=1, row=1, sticky="nsew", padx=0, pady=(0,2))

            Entry_min = CTkEntry(Entry_Frame,
                                    placeholder_text=current_min,
                                    bg_color="transparent",
                                    fg_color="transparent",
                                    corner_radius=0,
                                    border_color="Grey",
                                    justify = "center")
            Entry_min.grid(column=1, row=0, sticky="nsew", pady=(10,2), padx=0)
            
            sec_label = CTkLabel(Entry_Frame, text="Sekunde", font=("Arial",8))
            sec_label.grid(column=2, row=1, sticky="nsew", padx=(0,10), pady=(0,2))

            Entry_sec = CTkEntry(Entry_Frame,
                                    placeholder_text=current_sec,
                                    bg_color="transparent",
                                    fg_color="transparent",
                                    corner_radius=0,
                                    border_color="Grey",
                                    justify = "center")
            Entry_sec.grid(column=2, row=0, sticky="nsew", pady=(10,2), padx=(0,10))
            
            def get_entry(): 
                
                date_cal = cal.get_date()        
                str_date = str(date_cal)

                hour = Entry_hour.get()
                minutes = Entry_min.get()
                seconds = Entry_sec.get()

                time = str(hour + ":" + minutes + ":" + seconds)

                DatumEntry.delete(0, END)
                UhrzeitEntry.delete(0, END)
                DatumEntry.insert(0, str_date)
                UhrzeitEntry.insert(0 ,time)

                datetime_choose.destroy()
                 

            Button_select = CTkButton(datetime_choose,
                                        text="Select",
                                        text_color = "#990099",
                                        font=("Arial",16,"bold"),
                                        fg_color = "#FF99FF",
                                        hover_color="#FFB7FF",
                                        command=get_entry)
            Button_select.grid(column=0, row=3, columnspan=2, sticky="nsew", pady=10, padx=10)
            
            
            datetime_choose.mainloop() 
    
    

        SelectDate = CTkButton(datetime_frame,
                                text="Select Datetime",
                                text_color = "#990099",
                                font=("Arial",16,"bold"),
                                fg_color = "#FF99FF",
                                hover_color="#FFB7FF",
                                command= cal_get)
        SelectDate.grid(column=0, row=2, columnspan=2, sticky="nsew", pady=10, padx=10)        

        def package_add():    
            
            Time = UhrzeitEntry.get()
            Date = DatumEntry.get()
            Datetime_str = Date + " " + Time

            try:
                datetime_object = datetime.strptime(Datetime_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print("Fehler bei der Konvertierung von Datum/Uhrzeit.")
                return
    
            print(datetime_object)
    
            inhalt1 = str(inhalt1_entry.get())
            inhalt2 = str(inhalt2_entry.get())
           # Erstellen der Basis-ID basierend auf dem Datum
            base_ID = int(datetime_object.strftime('%y%m%d')) * 1000
            
            cursor.execute("SELECT MAX(ID) FROM aks.tdim_inventory WHERE ID >= %s AND ID < %s", (base_ID, base_ID + 1000))
            last_id = cursor.fetchone()[0]

            if last_id is None:
                ID = base_ID
            else:
                ID = last_id + 1


            print(ID)
    
            try:
                query = '''INSERT INTO aks.tdim_inventory(ID, issue_datetime, content_1, content_2)
                        VALUES(%s, %s, %s, %s)'''
                cursor.execute(query, (ID, datetime_object, inhalt1, inhalt2))
                conn.commit()
                print("Package has added!")
            except Exception as e:
                print("Fehler beim Einfügen des Pakets in die Datenbank:", e)

            messagebox.showinfo("", "Package has been added!")

    
        button_add = CTkButton(create_package_frame,
                                text="Add Package",
                                text_color = "#990099",
                                font=("Arial",16,"bold"),
                                fg_color = "#FF99FF",
                                hover_color="#FFB7FF",
                                command=package_add)
        button_add.grid(column=0, row=3, sticky="nsew", pady=(5,10), padx=10)

    def package_tabel(self):
        package_table_frame = CTkFrame(self, corner_radius=5)
        package_table_frame.grid(column=1, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)
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

                self.label2.configure(text= timedelta(int(seconds)))
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
                # Holen Sie sich den Text aus label1
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
            

            

            
            
            

            


