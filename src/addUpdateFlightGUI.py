from flight import *
from tkinter import *
from addUpdatePlaneGUI import *
import tkinter.messagebox

class FlightGUI():
  def __init__(self):
    self.rows = []
    self.currentID = 0
    
    self.window = Toplevel()
    self.window.title("Add/Update Flight")
    
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
    
    self.btSave = Button(self.window, text="Add Flight",command=self.saveFlight)
    self.btUpdate = Button(self.window, text="Update", command=self.updateFlight)
    self.btAdd = Button(self.window, text="Add an Airplane", command=self.addPlane)
    self.btSearchID = Button(self.window, text="Search by ID", command=self.searchID)
    self.btSearch = Button(self.window, text="Search", command=self.search)
    self.btNext = Button(self.window, text="Next", command=self.getNext)
    self.btPrev = Button(self.window, text="Previous", command=self.getPrev)
    self.btDelete = Button(self.window, text="Delete", command=self.delete)
    
    self.lbID.grid(row=1, column=2)
    self.enID.grid(row=1, column=3)
    self.lbOrigin.grid(row=2, column=1)
    self.enOrigin.grid(row=2, column=2)
    self.lbDest.grid(row=2, column=3)
    self.enDest.grid(row=2, column=4)
    self.lbDept.grid(row=3, column=1)
    self.enDept.grid(row=3, column=2)
    self.lbArrival.grid(row=3, column=3)
    self.enArrival.grid(row=3, column=4)
    self.lbAirplane.grid(row=4, column=2)
    self.enAirplane.grid(row=4, column=3)
    self.lbPrice.grid(row=5, column=1)
    self.lbSeatsLeft.grid(row=5, column=3)
    self.enPrice.grid(row=5, column=2)
    self.enSeatsLeft.grid(row=5, column=4)
    self.btSave.grid(row=6, column=1)
    self.btAdd.grid(row=6, column=4)
    self.btDelete.grid(row=6, column=3)
    self.btSearchID.grid(row=7, column=3)
    self.btSearch.grid(row=7, column=4)
    self.btNext.grid(row=7, column=1)
    self.btPrev.grid(row=7, column=2)

    self.window.mainloop()

  
  # this method instantiates a Flight object and saves it, then finds its ID
  def saveFlight(self):
    obj = Flight(self.origin.get(), self.destination.get(), self.departure.get(), self.arrival.get(), self.airplaneID.get(),
                 self.price.get(), self.seatsLeft.get())
                   
    obj.saveToDatabase()
    cursor.execute(findID)
    self.flightID.set(cursor.fetchone()[0])
    tkinter.messagebox.showinfo(message="Flight added")
    
  # this method instantiates a Flight object corresponding to a pre-existent one, and uses its update method  
  def updateFlight(self):
    obj = Flight(self.origin.get(), self.destination.get(), self.departure.get(), self.arrival.get(), self.airplaneID.get(),
                 self.price.get(), self.seatsLeft.get(), self.flightID.get())
                                      
    obj.update()
    tkinter.messagebox.showinfo(message="Flight updated")
   
    
  # allows the user to add a plane  
  def addPlane(self):
    PlaneGUI()
  
  # deletes a flight
  def delete(self):
    if tkinter.messagebox.askokcancel(message="Are you sure you want to delete this?"):
      cursor.execute(deleteFlight, (self.flightID.get(),))
      cnx.commit()
  
  # finds a specific flight given an ID 
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
    except:
      tkinter.messagebox.showerror(message="Record not found")
  
  # tries to find a flight corresponding to whatever's in the origin, destination, departure, and arrival entry widgets
  def search(self):
    self.rows = []
    cursor.execute(findFlights, (self.origin.get(), self.destination.get()))
    for row in cursor:
      self.rows.append(row)
  
  # gets the next result
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
      
  # gets the previous result    
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
