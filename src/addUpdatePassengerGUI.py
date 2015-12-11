from passenger import *
from returningPassengerGUI import *
from tkinter import *
import tkinter.messagebox

# Internal class. Doesn't do much other than instantiate a bunch of variables and widgets
class PassengerGUI:
  def __init__(self):
    self.window = Toplevel()
    
    self.firstName = StringVar()
    self.lastName= StringVar()
    self.dob = StringVar()
    self.email = StringVar()
    self.phone = StringVar()
    self.cardholder = StringVar()
    self.cardType = StringVar()
    self.cardNumber = IntVar()
    self.expiration = StringVar()
    self.securityNumber = IntVar()
    self.firstAddress = StringVar()
    self.secondAddress = StringVar()
    self.city = StringVar()
    self.state = StringVar()
    self.zip = IntVar()
    self.country = StringVar()
    
    self.lbFirst = Label(self.window, text="First name:")
    self.enFirst = Entry(self.window, textvariable=self.firstName)
    
    self.lbLast = Label(self.window, text="Last name:")
    self.enLast = Entry(self.window, textvariable=self.lastName)
    
    self.lbDOB = Label(self.window, text="Date of birth:")
    self.enDOB = Entry(self.window, textvariable=self.dob)
    
    self.lbEmail = Label(self.window, text="Email:")
    self.enEmail = Entry(self.window, textvariable=self.email)
    
    self.lbPhone = Label(self.window, text="Phone:")
    self.enPhone = Entry(self.window, textvariable=self.phone)
    
    self.lbCardholder = Label(self.window, text="Cardholder:")
    self.enCardholder = Entry(self.window, textvariable=self.cardholder)
    
    self.lbType = Label(self.window, text="Card type:")
    self.enType = Entry(self.window, textvariable=self.cardType)
    
    self.lbCardNumber = Label(self.window, text="Card number:")
    self.enCardNumber = Entry(self.window, textvariable=self.cardNumber)
    
    self.lbExpiration = Label(self.window, text="Expiration:")
    self.enExpiration = Entry(self.window, textvariable=self.expiration)
    
    self.lbSecurityNumber = Label(self.window, text="Security number:")
    self.enSecurityNumber = Entry(self.window, textvariable=self.securityNumber)
    
    self.lbFirstLine = Label(self.window, text="Street address:")
    self.enFirstLine = Entry(self.window, textvariable=self.firstAddress)
    
    self.lbSecondLine = Label(self.window, text="Street address (cont'd):")
    self.enSecondLine = Entry(self.window, textvariable=self.secondAddress)
    
    self.lbCity = Label(self.window, text="City:")
    self.enCity = Entry(self.window, textvariable=self.city)
    
    self.lbState = Label(self.window, text="State:")
    self.enState = Entry(self.window, textvariable=self.state)
    
    self.lbZIP = Label(self.window, text="ZIP:")
    self.enZIP = Entry(self.window, textvariable=self.zip)
    
    self.lbCountry = Label(self.window, text="Country:")
    self.enCountry = Entry(self.window, textvariable=self.country)
    
    self.lbFirst.grid(row=2, column=1)
    self.enFirst.grid(row=2, column=2)
    self.lbLast.grid(row=2, column=3)
    self.enLast.grid(row=2, column=4)
    self.lbDOB.grid(row=2, column=5)
    self.enDOB.grid(row=2, column=6)
    self.lbEmail.grid(row=3, column=1)
    self.enEmail.grid(row=3, column=2)
    self.lbPhone.grid(row=3, column=3)
    self.enPhone.grid(row=3, column=4)
    self.lbCardholder.grid(row=4, column=2)
    self.enCardholder.grid(row=4, column=3, columnspan=2)
    self.lbType.grid(row=4, column=5)
    self.enType.grid(row=4, column=6)
    self.lbCardNumber.grid(row=5, column=1)
    self.enCardNumber.grid(row=5, column=2)
    self.lbExpiration.grid(row=5, column=5)
    self.enExpiration.grid(row=5, column=6)
    self.lbSecurityNumber.grid(row=5, column=3)
    self.enSecurityNumber.grid(row=5, column=4)
    self.lbFirstLine.grid(row=6, column=1)
    self.enFirstLine.grid(row=6, column=2)
    self.lbSecondLine.grid(row=6, column=3)
    self.enSecondLine.grid(row=6, column=4)
    self.lbCity.grid(row=6, column=5)
    self.enCity.grid(row=6, column=6)
    self.lbState.grid(row=7, column=1)
    self.enState.grid(row=7, column=2)
    self.lbZIP.grid(row=7, column=3)
    self.enZIP.grid(row=7, column=4)
    self.lbCountry.grid(row=7, column=5)
    self.enCountry.grid(row=7, column=6)
    
    
# this just allows someone to create a new passenger/customer
class AddPassengerGUI(PassengerGUI):
  def __init__(self):
    PassengerGUI.__init__(self)
    self.window.title("Add Customer")
    self.id = IntVar()
    self.lbID = Label(self.window, text="ID:")
    self.enID = Entry(self.window, textvariable=self.id)    
    self.btAdd = Button(self.window, text="Add", command=self.add)
    self.btGo = Button(self.window, text="Go to Customer Info", command=self.go)
    
    self.lbID.grid(row=1, column=3)
    self.enID.grid(row=1, column=4)
    self.btAdd.grid(row=8, column=3)
    self.btGo.grid(row=8, column=4)
    
    self.window.mainloop()
  
  # this instantiates a Passenger object, saves it, and then finds its ID
  def add(self):
    obj = Passenger(self.firstName.get(), self.lastName.get(), self.dob.get(), self.email.get(), self.phone.get(), self.cardholder.get(),
                    self.cardType.get(), self.cardNumber.get(), self.securityNumber.get(), self.expiration.get(), self.firstAddress.get(),
                    self.secondAddress.get(), self.city.get(), self.state.get(), self.zip.get(), self.country.get())
    obj.saveToDatabase()
    cursor.execute(findID)
    self.id.set(cursor.fetchone()[0])
    tkinter.messagebox.showinfo(message="Passenger added")
  
  # this goes to the returning passenger GUI, passing the ID
  # hopefully, the one which corresponds to the passenger just instantiated
  def go(self):
    ReturningPassengerGUI(self.id.get())
    

# this class is for a specific customer/passenger to update their data
# in this class self.id is NOT an IntVar, it's just a normal int
class UpdateSelfGUI(PassengerGUI):
  def __init__(self, customerID):
    PassengerGUI.__init__(self)
    self.window.title("Update Self")
    self.id = customerID
    idStr = "ID:" + str(self.id)
    self.lbID = Label(self.window, text=idStr)
    
    self.btUpdate = Button(self.window, text="Update", command=self.update)
    self.btDelete = Button(self.window, text="Delete", command=self.delete)
    self.btRefresh = Button(self.window, text="Refresh", command=self.populate)
    
    self.lbID.grid(row=1, column=3, columnspan=2)
    self.btUpdate.grid(row=8, column=2)
    self.btRefresh.grid(row=8, column=3)
    self.btDelete.grid(row=8, column=4)
    
    self.populate()
    
    self.window.mainloop()
    
  # this method gets a specific passenger/customer and sets the entry fields to whatever values
  # are given by the database
  def populate(self):
    cursor.execute(findPassengerByID, (self.id,))
    row = cursor.fetchone()
    try:
      self.firstName.set(row[0])
      self.lastName.set(row[1])
      self.dob.set(row[2])
      self.email.set(row[3])
      self.phone.set(row[4])
      self.cardholder.set(row[5])
      self.cardType.set(row[6])
      self.cardNumber.set(row[7])
      self.securityNumber.set(row[8])
      self.expiration.set(row[9])
      self.firstAddress.set(row[10])
      self.secondAddress.set(row[11])
      self.city.set(row[12])
      self.state.set(row[13])
      self.zip.set(row[14])
      self.country.set(row[15])
    except:
      tkinter.messagebox.showerror(message="Record not found")
      
  # this instantiates a Passenger object and uses its update method
  def update(self):
    obj = Passenger(self.firstName.get(), self.lastName.get(), self.dob.get(), self.email.get(), self.phone.get(), self.cardholder.get(),
                    self.cardType.get(), self.cardNumber.get(), self.securityNumber.get(), self.expiration.get(), self.firstAddress.get(),
                    self.secondAddress.get(), self.city.get(), self.state.get(), self.zip.get(), self.country.get(), self.id)    
    obj.update()
    tkinter.messagebox.showinfo(message="Passenger updated")
  
  # this deletes a passenger
  def delete(self):
    if tkinter.messagebox.askokcancel(message="Are you sure you want to delete this?"):
      cursor.execute(deletePassenger, (self.id,))
      cnx.commit()
    

# this class is for the airline to update or add multiple passenger/customers
class AddUpdatePassengerGUI(PassengerGUI):
  def __init__(self):
    PassengerGUI.__init__(self)
    self.window.title("Add/Update Customer")
    self.id = IntVar()    
    self.lbID = Label(self.window, text="ID:")
    self.enID = Entry(self.window, textvariable=self.id)
    
    self.btAdd = Button(self.window, text="Add", command=self.add)
    self.btGet = Button(self.window, text="Get Customer", command=self.get)
    self.btUpdate = Button(self.window, text="Update", command=self.update)
    self.btDelete = Button(self.window, text="Delete", command=self.delete)
    
    self.lbID.grid(row=1, column=3)
    self.enID.grid(row=1, column=4)
    self.btGet.grid(row=8, column=2)
    self.btAdd.grid(row=8, column=3)
    self.btUpdate.grid(row=8, column=4)
    self.btDelete.grid(row=8, column=5)
    
    self.window.mainloop()
  
  def delete(self):
    if tkinter.messagebox.askokcancel(message="Are you sure you want to delete this?"):
      cursor.execute(deletePassenger, (self.id.get(),))
      cnx.commit()
  
  # this gets a specific customer, given their ID
  def get(self):
    cursor.execute(findPassengerByID, (self.id.get(),))
    row = cursor.fetchone()
    try:
      self.firstName.set(row[0])
      self.lastName.set(row[1])
      self.dob.set(row[2])
      self.email.set(row[3])
      self.phone.set(row[4])
      self.cardholder.set(row[5])
      self.cardType.set(row[6])
      self.cardNumber.set(row[7])
      self.securityNumber.set(row[8])
      self.expiration.set(row[9])
      self.firstAddress.set(row[10])
      self.secondAddress.set(row[11])
      self.city.set(row[12])
      self.state.set(row[13])
      self.zip.set(row[14])
      self.country.set(row[15])
    except:
      tkinter.messagebox.showerror(message="Record not found")
  
  # this updates a pre-existent passenger 
  def update(self):
    obj = Passenger(self.firstName.get(), self.lastName.get(), self.dob.get(), self.email.get(), self.phone.get(), self.cardholder.get(),
                    self.cardType.get(), self.cardNumber.get(), self.securityNumber.get(), self.expiration.get(), self.firstAddress.get(),
                    self.secondAddress.get(), self.city.get(), self.state.get(), self.zip.get(), self.country.get(), self.id)    
    obj.update()
    tkinter.messagebox.showinfo(message="Passenger updated")
  
  # this adds a passenger  
  def add(self):
    obj = Passenger(self.firstName.get(), self.lastName.get(), self.dob.get(), self.email.get(), self.phone.get(), self.cardholder.get(),
                    self.cardType.get(), self.cardNumber.get(), self.securityNumber.get(), self.expiration.get(), self.firstAddress.get(),
                    self.secondAddress.get(), self.city.get(), self.state.get(), self.zip.get(), self.country.get())
    obj.saveToDatabase()
    cursor.execute(findID)
    self.id.set(cursor.fetchone()[0])
    tkinter.messagebox.showinfo(message="Passenger added")
    
