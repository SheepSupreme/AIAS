from customtkinter import *
import datetime as dt
from tkcalendar import *
import mysql.connector
from errno import errorcode


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


        inhalt1_label = CTkLabel(inhalt_frame, text="1. Inhalt:", text_color= "#FF99FF",  font=("Arial",16,"bold"))
        inhalt1_label.grid(column=0, row=0, sticky="nsew")

        inhalt1_entry = CTkEntry(inhalt_frame)
        inhalt1_entry.grid(column=1, row=0, sticky="nsew", pady=10, padx=10)

        inhalt2_label = CTkLabel(inhalt_frame, text="2. Inhalt:", text_color= "#FF99FF",  font=("Arial",16,"bold"))
        inhalt2_label.grid(column=0, row=1, sticky="nsew")

        inhalt2_entry = CTkEntry(inhalt_frame)
        inhalt2_entry.grid(column=1, row=1, sticky="nsew", pady=10, padx=10)

        datetime_frame = CTkFrame(create_package_frame, corner_radius=5)
        datetime_frame.grid(column=0 , row= 2, sticky="nsew", pady=10, padx=10)

        datetime_frame.columnconfigure(0, weight=1, uniform='a')
        datetime_frame.columnconfigure(1, weight=2, uniform='a')
        datetime_frame.rowconfigure((0,1), weight=1, uniform='a')
        datetime_frame.rowconfigure(2, weight=1, uniform='a')

        Datum = CTkLabel(datetime_frame, text="Datum:", text_color= "#FF99FF",  font=("Arial",16,"bold"))
        Datum.grid(column=0, row=0, sticky="nsew", pady=10, padx=10)

        Uhrzeit = CTkLabel(datetime_frame, text="Uhrzeit:", text_color="#FF99FF", font=("Arial",16,"bold"))
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

            cal = Calendar(datetime_choose, selectmode = 'day', date_pattern ="dd-mm-yyyy",
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
            Datetime = Date + " " + Time 

            inhalt1 = inhalt1_entry.get()
            inhalt2 = inhalt2_entry.get()
            ID = 1

            query = '''INSERT INTO aks.tdim_inventory(ID, issue_datetime, content_1, content_2)
                    VALUES(%d, %s, %s, %s)''' %ID %Datetime %inhalt1 %inhalt2
            
            cursor.execute(query)
            print("Package has added!")

        button_add = CTkButton(create_package_frame,
                                text="ADD",
                                text_color = "#990099",
                                font=("Arial",16,"bold"),
                                fg_color = "#FF99FF",
                                hover_color="#FFB7FF",
                                command=package_add)
        button_add.grid(column=0, row=3, sticky="nsew", pady=(5,10), padx=10)


            

            

            
            
            

            


