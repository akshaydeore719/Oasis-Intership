from tkinter import*
from tkinter import ttk
import requests
def data_get():
    
    city=city_name.get()
    
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0a7c66fd32f682b382612745351de16e")
    data = response.json()
    print(data)
    
    w_label1.config(text=data["weather"][0]["main"])

    wb_label1.config(text=data["weather"][0]["description"])

    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))

    per_label1.config(text=data["main"]["pressure"])


win=Tk()
win.title("Akshay")
win.config(bg="blue")
win.geometry("800x750")
name_label= Label(win,text="Akshay Weather App",font=("Time New Roman",45,"bold"))
name_label.place(x=45,y=70,height=70,width=700)

city_name = StringVar()

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


com = ttk.Combobox (win,text="Akshay Weather App", values = list_name,
                    font=("Time New Roman",25,"bold"),textvariable=city_name)

com.place(x=45,y=160,height=70,width=700)

w_label= Label(win,text="Weather Climate",
               font=("Time New Roman",30))
w_label.place(x=45,y=375,height=60,width=300)

w_label1= Label(win,text="",
               font=("Time New Roman",30))
w_label1.place(x=395,y=375,height=60,width=300)

wb_label= Label(win,text="Weather Description",
               font=("Time New Roman",25))
wb_label.place(x=45,y=455,height=60,width=310)

wb_label1= Label(win,text="",
               font=("Time New Roman",25))
wb_label1.place(x=395,y=455,height=60,width=310)

temp_label= Label(win,text="Temperature",
               font=("Time New Roman",25))
temp_label.place(x=45,y=535,height=60,width=310)

temp_label1= Label(win,text="",
               font=("Time New Roman",25))
temp_label1.place(x=395,y=535,height=60,width=310)

per_label= Label(win,text="Pressure",
               font=("Time New Roman",25))
per_label.place(x=45,y=615,height=60,width=310)

per_label1= Label(win,text="",
               font=("Time New Roman",25))
per_label1.place(x=395,y=615,height=60,width=310)

done_button = Button(win,text="Done", font=("Time New Roman",25,"bold"),command=data_get)

done_button.place(y=255,height=70, width=150,x=300)

win.mainloop()
