from tkinter import *
from addUpdateFlightGUI import *
from addUpdatePassengerGUI import *
from addUpdatePlaneGUI import *
from addUpdateReservationGUI import *

class AirlineGUI:
  def __init__(self):
    self.window = Toplevel()
    self.window.title("Airline")
    
    self.btUpdateFlight = Button(self.window, text="Add or Update Flight", command=self.updateFlight)
    self.btUpdatePlane = Button(self.window, text="Add or Update Plane", command=self.updatePlane)
    self.btUpdatePassenger = Button(self.window, text="Add or Update Customer", command=self.updatePassenger)
    self.btUpdateReservation = Button(self.window, text="Add or Update Reservation", command=self.updateReservation)
    
    self.btUpdateFlight.pack()
    self.btUpdatePlane.pack()
    self.btUpdatePassenger.pack()
    self.btUpdateReservation.pack()
    
    self.window.mainloop()
    
  def updateFlight(self):
    FlightGUI()
  
  def updatePlane(self):
    PlaneGUI()
  
  def updatePassenger(self):
    AddUpdatePassengerGUI()
  
  def updateReservation(self):
    ReservationGUI()
