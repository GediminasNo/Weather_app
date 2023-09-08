from tkinter import *

import requests
import json

class Weather_app_1:
    def __init__(self,Master):

        Master.geometry("725x80")
        Master.title("Weather_app_Main_")
        Master.configure(background="blue")
        Master.resizable(False,False)


        def Click_me():

            try:
                self.new_window = Toplevel()
                self.new_window.geometry("1350x50")
                self.new_window.title("Weather_Summary")
                self.new_window.configure(background="green")
                self.new_window.resizable(False,False)
                self.api_info = requests.get(
                        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+self.entry_main.get()+"&distance=25&API_KEY=0136A856-DCE9-4056-8AF0-DC0CE62CE5D7")
                self.api_content = json.loads(self.api_info.content)
                self.data_obs = self.api_content[0]["DateObserved"]
                self.local_time = self.api_content[0]["LocalTimeZone"]
                self.area_report = self.api_content[0]["ReportingArea"]
                self.aqi = self.api_content[0]["AQI"]
                self.category = self.api_content[0]["Category"]["Name"]
                self.listas = str([self.data_obs,' < Time Data ', ' Local time Zone > ', self.local_time, 'Area > ', self.area_report, str(self.aqi),' < AQI number ',
                               'Air Quality  > ',
                               self.category]).strip('][')

                if self.category == "Good":
                    self.weather_color = 'Green'

                elif self.category == 'Moderate':
                    self.weather_color = 'Yellow'

                elif self.category ==  'Unhealthy for Sensitive Groups':
                    self.weather_color == 'Orange'

                elif self.category == 'Unhealthy':
                    self.weather_color = 'Red'

                elif self.category == 'Very Unhealthy':
                    self.weather_color = 'Purple'

                elif self.category == 'Hazardous':
                    self.weather_color = 'Maroon'

                self.new_window.configure(bg=self.weather_color)

                self.label_1 = Label(self.new_window, text=self.listas, font=('Italic', '14'), background=self.weather_color)
                self.label_1.grid(row=0, column=1, columnspan=3)

            except EXCEPTION as e:
                self.api_content = "Eror"


        self.label_description = Label(Master, text="Place The zip code ant get The Summary Of Area ",font=('Italic','12'),
                                                bg="green",fg='white')
        self.label_description.grid(row=1,column=0)


        self.entry_main = Entry(Master)
        self.entry_main.grid(row=1, column=2, columnspan=2, padx=20, pady=10)


        self.label_main = Label(Master,text=" <<  Look up to zip code",padx=10,pady=5,font=('Italic','10'),bg="green",fg='white')
        self.label_main.grid(row=1,column=5,columnspan=2)




        self.buton_main = Button(Master,text=" Click Here",bg='black',fg='white',font=('Italic',10),command=Click_me)
        self.buton_main.grid(row=3,column=2,columnspan=3,padx=10)

root = Tk()
weather_app_1 = Weather_app_1(root)
root.mainloop()