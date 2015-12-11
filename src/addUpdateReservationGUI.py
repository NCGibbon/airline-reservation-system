from reservation import *
from databaseConnection import *
from tkinter import *
import tkinter.messagebox

# this class is for airlines to add, update, or remove specific reservations
class ReservationGUI:
  def __init__(self):
    self.rows = []
    self.currentRow = 0
    
    self.window = Toplevel()
    self.window.title("Add/Update Reservation")
    
    self.flight = IntVar()
    self.customer = IntVar()
    self.row = IntVar()
    self.column = IntVar()
    self.reservation = IntVar()
    
    self.lbReservation = Label(self.window, text="Reservation ID:")
    self.enReservation = Entry(self.window, textvariable=self.reservation)
    self.lbFlight = Label(self.window, text="Flight ID:")
    self.enFlight = Entry(self.window, textvariable=self.flight)
    self.lbCustomer = Label(self.window, text="Customer ID:")
    self.enCustomer = Entry(self.window, textvariable=self.customer)
    self.lbRow = Label(self.window, text="Row:")
    self.enRow = Entry(self.window, textvariable=self.row)
    self.lbColumn = Label(self.window, text="Column:")
    self.enColumn = Entry(self.window, textvariable=self.column)
    
    self.btAdd = Button(self.window, text="Add", command=self.add)
    self.btUpdate = Button(self.window, text="Update", command=self.update)
    self.btSearchFlight = Button(self.window, text="Search by Flight", command=self.searchFlight)
    self.btSearchCustomer = Button(self.window, text="Search by Customer", command=self.searchCustomer)
    self.btgetFlight = Button(self.window, text="Search by Reservation", command=self.getID)
    self.btDelete = Button(self.window, text="Delete", command=self.delete)
    self.btNext = Button(self.window, text="Next", command=self.getNext)
    self.btPrev = Button(self.window, text="Previous", command=self.getPrev)
    
    self.lbReservation.grid(row=1, column=2)
    self.enReservation.grid(row=1, column=3)
    self.lbFlight.grid(row=2, column=1)
    self.enFlight.grid(row=2, column=2)
    self.lbCustomer.grid(row=2, column=3)
    self.enCustomer.grid(row=2, column=4)
    self.lbRow.grid(row=3, column=1)
    self.enRow.grid(row=3, column=2)
    self.lbColumn.grid(row=3, column=3)
    self.enColumn.grid(row=3, column=4)
    self.btAdd.grid(row=4, column=1)
    self.btUpdate.grid(row=4, column=2)
    self.btSearchFlight.grid(row=5, column=1)
    self.btSearchCustomer.grid(row=5, column=2)
    self.btgetFlight.grid(row=4, column=4)
    self.btDelete.grid(row=4, column=3)
    self.btNext.grid(row=5, column=3)
    self.btPrev.grid(row=5, column=4)
    
    self.window.mainloop()
    
    
  def add(self):
    obj = Reservation(self.flight.get(), self.customer.get(), self.row.get(), self.column.get())
    obj.saveToDatabase()
    self.flight.set(obj.getID())
    tkinter.messagebox.showinfo(message="Reservation added")
  
  def update(self):
    obj = Reservation(self.flight.get(), self.customer.get(), self.row.get(), self.column.get(), self.reservation.get())
    obj.update()
    tkinter.messagebox.showinfo(message="Reservation updated")
  
  def searchFlight(self):
    self.rows = []
    cursor.execute(findByFlight, (self.flight.get(),))
    for row in cursor:
      self.rows.append(row)
  
  def searchCustomer(self):
    self.rows = []
    cursor.execute(findByCustomer, (self.customer.get(),))
    for row in cursor:
      self.rows.append(row)
  
  def getID(self):
    cursor.execute(findByID, (self.reservation.get(),))
    row = cursor.fetchone()
    try:
      self.flight.set(row[0])
      self.customer.set(row[1])
      self.row.set(row[2])
      self.column.set(row[3])
      self.reservation.set(row[4])
    except:
      tkinter.messagebox.showerror(message="Record not found")
  
  def delete(self):
    if tkinter.messagebox.askokcancel(message="Are you sure you want to delete this?"):
      cursor.execute(deleteReservation, (self.reservation.get(),))
      cnx.commit()
    
  def getNext(self):
    self.currentRow += 1
    try:
      row = self.rows[self.currentRow]
      self.flight.set(row[0])
      self.customer.set(row[1])
      self.row.set(row[2])
      self.column.set(row[3])
      self.reservation.set(row[4])
    except IndexError:
      pass
    except:
      tkinter.messagebox.showerror(message="Record not found")
  
  def getPrev(self):
    self.currentRow -= 1
    try:
      row = self.rows[self.currentRow]
      self.flight.set(row[0])
      self.customer.set(row[1])
      self.row.set(row[2])
      self.column.set(row[3])
      self.reservation.set(row[4])
    except IndexError:
      pass
    except:
      tkinter.messagebox.showerror(message="Record not found")
