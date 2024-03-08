from customtkinter import *
import datetime as dt
from tkcalendar import *

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

            cal = Calendar(datetime_choose, selectmode = 'day',
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


            print(current_hour)
            print(current_min)
            print(current_sec)

            Entry_hour = CTkEntry(Entry_Frame, text=current_hour)
            Entry_hour.grid(column=0, row=0, sticky="nsew", pady=10, padx=10)
        
            datetime_choose.mainloop() 
    
    

        SelectDate = CTkButton(datetime_frame,
                                text="Select Datetime",
                                text_color = "#990099",
                                font=("Arial",16,"bold"),
                                fg_color = "#FF99FF",
                                hover_color="#FFB7FF",
                                command= cal_get)
        SelectDate.grid(column=0, row=2, columnspan=2, sticky="nsew", pady=10, padx=10)        

        

        button_add = CTkButton(create_package_frame,
                                text="ADD",
                                text_color = "#990099",
                                font=("Arial",16,"bold"),
                                fg_color = "#FF99FF",
                                hover_color="#FFB7FF")
        button_add.grid(column=0, row=3, sticky="nsew", pady=(5,10), padx=10)


        # class MyDateEntry(DateEntry):
        #     def __init__(self, master=None, **kw):
        #         DateEntry.__init__(self, master=None, **kw)
        #         # add black border around drop-down calendar
        #         self._top_cal.configure(bg='black', bd=1)
        #         # add label displaying today's date below
        #         CTkLabel(self._top_cal, bg='gray90', anchor='w',
        #             text='Hoje: %s' % dt.date.today().strftime('%d/%m/%Y')).pack(fill='x')
            

            
            
            

            


