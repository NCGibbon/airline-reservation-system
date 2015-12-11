from tkinter import *
from buyTicketGUI import *
from addUpdatePassengerGUI import *
from pickFlightGUI import *

class ReturningPassengerGUI:
  def __init__(self, customerid=None):
    self.window = Toplevel()
    self.window.title("Returning Passenger")
    
    self.customer = IntVar()
    if type(customerid) is int:
      self.customer.set(customerid)
    
    self.lbID = Label(self.window, text="Enter your customer ID:")
    self.enID = Entry(self.window, textvariable=self.customer)
    
    self.btUpdateSelf = Button(self.window, text="Update Personal Info", command=self.updateSelf)
    self.btBuyTicket = Button(self.window, text="Buy Ticket", command=self.buyTicket)
    self.btCancelTicket = Button(self.window, text="Cancel Ticket", command=self.cancelTicket)
    self.btChooseSeat = Button(self.window, text="Choose Seat", command=self.chooseSeat)
    
    self.lbID.pack()
    self.enID.pack()
    self.btUpdateSelf.pack()
    self.btBuyTicket.pack()
    self.btCancelTicket.pack()
    self.btChooseSeat.pack()
    
    self.window.mainloop()
  
  def updateSelf(self):
    UpdateSelfGUI(self.customer.get())
  
  def buyTicket(self):
    BuyTicketGUI(self.customer.get())
    
  def chooseSeat(self):
    PickFlightSeatGUI(self.customer.get())
  
  def cancelTicket(self):
    PickFlightCancelGUI(self.customer.get())
  

