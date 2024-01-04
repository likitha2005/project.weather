from tkinter import *
from PIL import Image, ImageTk
#from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
#from timezonefinder import TimezoneFinder
from datetime import *



        
        
        
        
        
        
class Home():
    def __init__(self,root):
        self.root = root
        self.bg_img = Image.open('img.png')
        self.bg_img = self.bg_img.resize((600, 400))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        
        self.bg_lbl = Label(root,image= self.bg_img)
        self.bg_lbl.place(x =0,y =0)
        self.title = Label(root, text = 'WELCOME TO WEATHER FORECAST AND TRAVEL RECOMMENDATION',font = ('Times New Roman',10,'bold'))
        self.title.place(x=40,y =10)
        self.pla = Label(root,text = 'Enter City:',font =('Italic',15,'bold'),width = 10)
        self.pla.place(x= 40,y = 80)
        self.pla.entry = Entry(root,font = ('Italic',15,'bold'),)
        self.pla.entry.place(x=180,y=80)
        
        
        self.btn = Button(root,text = 'GET REPORT',justify = 'center', command = self.window_des)
        self.btn.place(x=180,y=150)
        
    def window_des(self):
        #self.btn.destroy()
        #ssself.bg_lbl()
        #self.pla.destroy()
       # self.title.destroy()
       # self.bg_img.destroy()
       self.root.destroy()
       root = Tk()
       root.geometry('500x350+550+200')
       root.title('WEATHER FORECAST AND TRAVEL RECOMMENDATION')
       self.ig_img = Image.open('report.png')
       self.ig_img = self.ig_img.resize((500, 300))
       self.ig_img = ImageTk.PhotoImage(self.ig_img)
        
        
       self.ig_lbl = Label(root,image= self.ig_img)
       self.ig_lbl.place(x =0,y =0)
        
    
       
       root.mainloop()

       
       
      
        
    
    

root = Tk()
root.geometry('500x350+550+200')

root.title('WEATHER FORECAST AND TRAVEL RECOMMENDATION')
home = Home(root)

root.mainloop()
        


