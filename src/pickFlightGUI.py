from tkinter import *
from databaseConnection import *
from chooseSeatingGUI import *
from addUpdateReservationGUI import *

class PickFlightGUI:
  def __init__(self, customerid):  
    self.rows = []
    self.currentRow = 0
    self.customer = customerid
    
    self.window = Toplevel()
    self.window.title("Pick Flight")
    
    self.origin = StringVar()
    self.destination = StringVar()
    self.departure = StringVar()
    self.arrival = StringVar()
    self.price = IntVar()
    self.seatsLeft = IntVar()
    self.airplaneID = IntVar()
    self.flightID = IntVar()
    
    self.lbID = Label(self.window, text="ID:")
    self.enID = Entry(self.window, textvariable=self.flightID)
    
    self.lbOrigin = Label(self.window, text="Origin:")
    self.enOrigin = Entry(self.window, textvariable=self.origin)
    
    self.lbDest = Label(self.window, text="Destination:")
    self.enDest = Entry(self.window, textvariable=self.destination)
    
    self.lbDept = Label(self.window, text="Departure:")
    self.enDept = Entry(self.window, textvariable=self.departure)
    
    self.lbArrival = Label(self.window, text="Arrival:")
    self.enArrival = Entry(self.window, textvariable=self.arrival)
    
    self.lbAirplane = Label(self.window, text="Airplane ID:")
    self.enAirplane = Entry(self.window, textvariable=self.airplaneID)
    
    self.lbPrice = Label(self.window, text="Price:")
    self.enPrice = Entry(self.window, textvariable=self.price)
    
    self.lbSeatsLeft = Label(self.window, text="Seats Left:")
    self.enSeatsLeft = Entry(self.window, textvariable=self.seatsLeft)
    
    self.btSearch = Button(self.window, text="Get Flights", command=self.search)
    self.btNext = Button(self.window, text="Next", command=self.getNext)
    self.btPrev = Button(self.window, text="Previous", command=self.getPrev)
    
    self.lbID.pack()
    self.enID.pack()
    self.lbOrigin.pack()
    self.enOrigin.pack()
    self.lbDest.pack()
    self.enDest.pack()
    self.lbDept.pack()
    self.enDept.pack()
    self.lbArrival.pack()
    self.enArrival.pack()
    self.lbAirplane.pack()
    self.enAirplane.pack()
    self.lbPrice.pack()
    self.enPrice.pack()
    self.lbSeatsLeft.pack()
    self.enSeatsLeft.pack()
    self.btSearch.pack()
    self.btNext.pack()
    self.btPrev.pack()
    
    
  def search(self):
    cursor.execute(getFlights, (self.customer,))
    for ID in cursor:
      cursor.execute(findFlightByID, ID)
      for row in cursor:
        self.rows.append(row)
    try:
      row = self.rows[self.currentRow]
      self.origin.set(row[0])
      self.destination.set(row[1])
      self.departure.set(row[2])
      self.arrival.set(row[3])
      self.airplaneID.set(row[4])
      self.price.set(row[5])
      self.seatsLeft.set(row[6])
      self.flightID.set(row[7])
    except:
      tkinter.messagebox.showerror(message="Record not found")
  
  def getNext(self):
    try:
      self.currentRow += 1
      row = self.rows[self.currentRow]
      self.origin.set(row[0])
      self.destination.set(row[1])
      self.departure.set(row[2])
      self.arrival.set(row[3])
      self.airplaneID.set(row[4])
      self.price.set(row[5])
      self.seatsLeft.set(row[6])
      self.flightID.set(row[7])
    except IndexError:
      pass
    except:
      tkinter.messagebox.showerror(message="Record not found")
      
  def getPrev(self):
    try:
      self.currentRow -= 1
      row = self.rows[self.currentRow]
      self.origin.set(row[0])
      self.destination.set(row[1])
      self.departure.set(row[2])
      self.arrival.set(row[3])
      self.airplaneID.set(row[4])
      self.price.set(row[5])
      self.seatsLeft.set(row[6])
      self.flightID.set(row[7])
    except IndexError:
      pass
    except:
      tkinter.messagebox.showerror(message="Record not found")

    
class PickFlightSeatGUI(PickFlightGUI):
  def __init__(self, customerid):
    PickFlightGUI.__init__(self, customerid)
    self.btPick = Button(self.window, text="Pick Seating", command=self.pick)
    self.btPick.pack()

    self.window.mainloop()
    
  def pick(self):
    ChooseSeatingGUI(self.customer, self.flightID.get())
  
    

class PickFlightCancelGUI(PickFlightGUI):
  def __init__(self, customerid):
    PickFlightGUI.__init__(self, customerid)
    self.btCancel = Button(self.window, text="Cancel Ticket", command=self.cancel)
    self.btCancel.pack()

    self.window.mainloop()
   
  # this gets the id of the ticket this customer has for the current flight, and deletes that row from the reservations table 
  def cancel(self):
    if tkinter.messagebox.askokcancel(message="Are you sure you want to delete this?"):
      cursor.execute(getReservation, (self.flightID.get(), self.customer))
      idreservation = cursor.fetchone()
      cursor.execute(deleteReservation, idreservation)
      cnx.commit()
