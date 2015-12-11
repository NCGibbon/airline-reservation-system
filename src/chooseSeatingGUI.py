from databaseConnection import *
from tkinter import *
import tkinter.messagebox

class ChooseSeatingGUI:
  def __init__(self, customerid, flightid):
    self.window = Toplevel()
    self.window.title("Choose a Seat")
    
    self.seatingButtons = []
    self.customer = customerid
    self.flight = flightid
    
    
    self.label = Label(self.window, text="Choose a seat:")
    
    for number in range(11):
      self.seatingButtons.append([])
      for otherNumber in range(9):
        btn = SeatingButton(self.window, number+2, otherNumber, text="")
        btn["command"] = lambda: self.selectSeat(btn)  # use a lambda function so a parameter can be passed
        self.seatingButtons[number].append(btn)
    
    self.getSeats()
    
    for lst in self.seatingButtons:
      for button in lst:
        if button.isOccupied:
          button["state"] = DISABLED
          
        button.grid(row=button.row, column=button.column)
    
    self.label.grid(row=1, column=3, columnspan=3)
    self.window.mainloop()
  
  # this gets all occupied seats from the database and sets the isOccupied attribute for that object to True 
  def getSeats(self):
     cursor.execute(getSeat, (self.flight,))
     for row in cursor:
      try:
        self.seatingButtons[row[0]][row[1]].isOccupied = True
      except TypeError:
        try:
          self.seatingButtons[int(row[0])][int(row[1])].isOccupied = True
        except:
          pass
      except:
        pass
  
  # this selects a seat, then refreshes
  def selectSeat(self, button):
    if button.selectSeat(self.customer, self.flight):
      tkinter.messagebox.showinfo(message="Seat selected")
    else:
      tkinter.messagebox.showerror(message="Seat not selected")
    self.getSeats()  

    
# this class inherits from the tkinter Button widget, and adds on a row, column, and isOccupied
# so that any SeatingButton knows where it is and whether it's occupied  
class SeatingButton(Button):
  def __init__(self, master=None, row=0, column=0, occupied=False, cnf={} , **kw):    
    Button.__init__(self, master, cnf, **kw)
    self.row = row
    self.column = column
    self.isOccupied = occupied
    
  # this selects a seat and saves it to the database
  def selectSeat(self, customerid, flightid):
    if not self.isOccupied:
      cursor.execute(selectSeat, (self.row, self.column, flightid, customerid))
      cnx.commit()
      return True
    else:
      return False


