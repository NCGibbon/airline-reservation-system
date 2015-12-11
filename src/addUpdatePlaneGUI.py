from airplane import *
from tkinter import *
import tkinter.messagebox

class PlaneGUI:
  def __init__(self):
    self.rows = []
    self.currentRow = 0
    
    self.window = Tk()
    self.window.title("Add/Update Plane")
    
    self.model = StringVar()
    self.manufacturer = StringVar()
    self.age = IntVar()
    self.planeID = IntVar()
    
    self.lbID = Label(self.window, text="ID:")
    self.enID = Entry(self.window, textvariable=self.planeID)
    self.lbManufacturer = Label(self.window, text="Manufacturer:")
    self.enManufacturer = Entry(self.window, textvariable=self.manufacturer)
    self.lbModel = Label(self.window, text="Model:")
    self.enModel = Entry(self.window, textvariable=self.model)
    self.lbAge = Label(self.window, text="Age:")
    self.enAge = Entry(self.window, textvariable=self.age)
    self.btAdd = Button(self.window, text="Add Plane", command=self.saveNewPlane)
    self.btUpdate = Button(self.window, text="Update Plane", command=self.updatePlane)
    self.btDelete = Button(self.window, text="Delete Plane", command=self.deletePlane)
    self.btNext = Button(self.window, text="Next", command=self.getNext)
    self.btPrev = Button(self.window, text="Prev", command=self.getPrev)
    self.btSearchID = Button(self.window, text="Search by ID", command=self.searchID)
    self.btSearch = Button(self.window, text="Search", command=self.search)

    self.lbID.grid(row=1, column=3)
    self.enID.grid(row=1, column=4)
    self.lbManufacturer.grid(row=2, column=1)
    self.enManufacturer.grid(row=2, column=2)
    self.lbModel.grid(row=2, column=3)
    self.enModel.grid(row=2, column=4)
    self.lbAge.grid(row=2, column=5)
    self.enAge.grid(row=2, column=6)
    self.btAdd.grid(row=3, column=2)
    self.btUpdate.grid(row=3, column=3)
    self.btDelete.grid(row=3, column=4)
    self.btSearchID.grid(row=3, column=6)
    self.btSearch.grid(row=3, column=5)
    self.btNext.grid(row=4, column=3)
    self.btPrev.grid(row=4, column=4)

    self.window.mainloop()


  # instantiates an Airplane object, saves it, then finds its ID  
  def saveNewPlane(self):
    obj = Airplane(self.model.get(), self.manufacturer.get(), self.age.get())
    obj.saveToDatabase()
    cursor.execute(findID)
    self.planeID = cursor.fetchone()
    tkinter.messagebox.showinfo(message="Plane saved")
  
  # instantiates an Airplane object based on a previous
  def updatePlane(self):
    obj = Airplane(self.model.get(), self.manufacturer.get(), self.age.get(), self.planeID.get())
    obj.update() 
    tkinter.messagebox.showinfo(message="Plane updated")
  
  # gets the airplane with a given ID, and updates the entry boxes
  def searchID(self):
    cursor.execute(findPlaneByID, (self.planeID.get(),))
    row = cursor.fetchone()
    try:
      self.model.set(row[0])
      self.manufacturer.set(row[1])
      self.age.set(row[2])
    except:
      tkinter.messagebox.showerror(message="Record not found")
  
  # searches for an airplane with the given characteristics
  def search(self):
    self.rows = []
    cursor.execute(findPlanes, (self.model.get(), self.manufacturer.get(), self.age.get()))
    for row in cursor:
      self.rows.append(row)
  
  # deletes a plane given an ID
  def deletePlane(self):
    if tkinter.messagebox.askokcancel(message="Are you sure you want to delete this?"):
      cursor.execute(deletePlane, (self.planeID.get(),))
      cnx.commit()
  
  # gets the next plane from the results
  def getNext(self):
    try:
      self.currentRow += 1
      row = self.rows[self.currentRow]
      self.model.set(row[0])
      self.manufacturer.set(row[1])
      self.age.set(row[2])
    except IndexError:
      pass
    except:
      tkinter.messagebox.showerror(message="Record not found")
  
  # gets the previous plane from the results    
  def getPrev(self):
    try:
      self.currentRow -= 1
      row = self.rows[self.currentRow]
      self.model.set(row[0])
      self.manufacturer.set(row[1])
      self.age.set(row[2])
    except IndexError:
      pass
    except:
      tkinter.messagebox.showerror(message="Record not found")
