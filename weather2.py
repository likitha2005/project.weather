from tkinter import*
class Weather_report:
    def __init__(self,root):
        self.root = root
    
        self.root.title('WEATHER FORECAST AND TRAVEL RECOMMENDATION')
        self.root.geometry('500x350+550+200')
        self.ig_img = Image.open('report.png')
        self.ig_img = self.ig_img.resize((100, 100))
        self.ig_img = ImageTk.PhotoImage(self.ig_img)
        
        self.ig_lbl = Label(root,image= self.ig_img)
    
root = Tk()
obj = Weather_report(root)
root.mainloop()
