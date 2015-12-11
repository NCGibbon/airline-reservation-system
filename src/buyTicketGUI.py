from tkinter import *
from databaseConnection import *
import tkinter.messagebox

class BuyTicketGUI:
  def __init__(self, customerID):
    self.customerID = customerID
    self.window = Toplevel()
    self.window.title("Buy a Ticket")
    
    self.flightID = IntVar()
    self.flightOrigin = StringVar()
    self.flightDestination = StringVar()
    self.flightDeparture = StringVar()
    self.flightArrival = StringVar()
    self.airplaneID = IntVar()
    self.flightSeatsLeft = IntVar()
    self.flightPrice = IntVar()
    
    self.currentRow = -1
    self.rows = []
    
    self.data = (self.flightOrigin.get(), self.flightDestination.get(), self.flightDeparture.get(), self.flightArrival.get(), self.airplaneID.get(),
                 self.flightPrice.get(), self.flightSeatsLeft.get(), self.flightID.get())
    
    self.lbFlightID = Label(self.window, text="ID:")
    self.enFlightID = Entry(self.window, textvariable=self.flightID)
    
    self.lbFlightOrigin = Label(self.window, text="Origin:")
    self.enFlightOrigin = Entry(self.window, textvariable=self.flightOrigin)
    
    self.lbFlightDestination = Label(self.window, text="Destination:")
    self.enFlightDestination = Entry(self.window, textvariable=self.flightDestination)
    
    self.lbFlightDeparture = Label(self.window, text="Departure:")
    self.enFlightDeparture = Entry(self.window, textvariable=self.flightDeparture)
    
    self.lbFlightArrival = Label(self.window, text="Arrival:")
    self.enFlightArrival = Entry(self.window, textvariable=self.flightArrival)
    
    self.lbAirplaneID = Label(self.window, text="Airplane ID:")
    self.enAirplaneID = Entry(self.window, textvariable=self.airplaneID)
    
    self.lbPrice = Label(self.window, text="Price:")
    self.enPrice = Entry(self.window, textvariable=self.flightPrice)
    
    self.lbSeatsLeft = Label(self.window, text="Seats Left:")
    self.enSeatsLeft = Entry(self.window, textvariable=self.flightSeatsLeft)
    
    self.btBuy = Button(self.window, text="Buy ticket", command=self.buyTicket)
    self.btSrchID = Button(self.window, text="Search by ID", command=self.searchID)
    self.btSearch = Button(self.window, text="Search", command=self.search)
    self.btNext = Button(self.window, text="Next", command=self.getNext)
    self.btPrev = Button(self.window, text="Previous", command=self.getPrev)
    
    self.lbFlightID.pack()
    self.enFlightID.pack()
    
    self.lbFlightOrigin.pack()
    self.enFlightOrigin.pack()
    
    self.lbFlightDestination.pack()
    self.enFlightDestination.pack()
    
    self.lbFlightDeparture.pack()
    self.enFlightDeparture.pack()
    
    self.lbFlightArrival.pack()
    self.enFlightArrival.pack()
    
    self.lbAirplaneID.pack()
    self.enAirplaneID.pack()
    
    self.lbPrice.pack()
    self.enPrice.pack()
    
    self.lbSeatsLeft.pack()
    self.enSeatsLeft.pack()
    
    self.btBuy.pack()
    self.btSrchID.pack()
    self.btSearch.pack()
    self.btNext.pack()
    self.btPrev.pack()
    
    self.window.mainloop()

  # this adds a ticket w/o seat values for the given flight and customer IDs
  # it also subtracts 1 from the seats left and updates the flight accordingly 
  def buyTicket(self):
    cursor.execute(addReservation, (self.flightID.get(), self.customerID, None, None))
    cnx.commit()
    self.seatsLeft.set(self.flightSeatsLeft.get()-1)
    self.data = (self.flightOrigin.get(), self.flightDestination.get(), self.flightDeparture.get(), self.flightArrival.get(), self.airplaneID.get(),
                 self.flightPrice.get(), self.flightSeatsLeft.get(), self.flightID.get())
    cursor.execute(updateFlight, self.data)
    cnx.commit()
    tkinter.messagebox.showinfo(message="Ticket bought")
  
  # this method gets the flight info given an ID
  def searchID(self):
    cursor.execute(findFlightByID, (self.flightID.get(),))
    row = cursor.fetchone()
    try:
      self.flightOrigin.set(row[0])
      self.flightDestination.set(row[1])
      self.flightDeparture.set(row[2])
      self.flightArrival.set(row[3])
      self.airplaneID.set(row[4])
      self.flightPrice.set(row[5])
      self.flightSeatsLeft.set(row[6])
      self.flightID.set(row[7])
    except TypeError:
      tkinter.messagebox.showerror(message="Record not found")
  
  # this should search given a desired origin, destination, departure, and arrival
  def search(self):
    self.rows = []
    cursor.execute(findFlights, (self.flightOrigin.get(), self.flightDestination.get()))    
    for row in cursor:
      self.rows.append(row)
  
  # this gets the next record
  def getNext(self):
    try:
      self.currentRow += 1
      row = self.rows[self.currentRow]
      self.flightOrigin.set(row[0])
      self.flightDestination.set(row[1])
      self.flightDeparture.set(row[2])     
      self.flightArrival.set(row[3])
      self.airplaneID.set(row[4])
      self.flightPrice.set(row[5])
      self.flightSeatsLeft.set(row[6])
      self.flightID.set(row[7])
    except IndexError:
      pass
    except:
      tkinter.messagebox.showerror(message="Record not found")
  
  # this gets the previous record    
  def getPrev(self):
    try:
      self.currentRow -= 1
      row = self.rows[self.currentRow]
      self.flightOrigin.set(row[0])
      self.flightDestination.set(row[1])
      self.flightDeparture.set(row[2])
      self.flightArrival.set(row[3])
      self.airplaneID.set(row[4])
      self.flightPrice.set(row[5])
      self.flightSeatsLeft.set(row[6])
      self.flightID.set(row[7])
    except IndexError:
      pass
    except:
      tkinter.messagebox.showerror(message="Record not found")
