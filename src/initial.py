from tkinter import *
from returningPassengerGUI import *
from addUpdatePassengerGUI import *
from airlineGUI import *

class InitialGUI:
  def __init__(self):
    self.window = Tk()
    self.window.title("Airline System")

    self.framePass = Frame(self.window)
    self.frameAir = Frame(self.window)

    self.label = Label(self.window, text = "I am a...")
    self.btReturn = Button(self.framePass, text = "Returning Passenger", command=self.returning)
    self.btAirline = Button(self.frameAir, text = "Airline", command=self.airline)
    self.btNew = Button(self.framePass, text = "New Passenger", command=self.newPassenger)

    self.label.pack()
    self.framePass.pack()
    self.frameAir.pack()
    self.btReturn.pack()
    self.btNew.pack()
    self.btAirline.pack()
    
    self.window.mainloop()
  
  def returning(self):
    ReturningPassengerGUI()
  
  def newPassenger(self):
    AddPassengerGUI()
  
  def airline(self):
    AirlineGUI()



InitialGUI()
