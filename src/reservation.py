from databaseConnection import *

class Reservation:
  def __init__(self, flight, customer, row, column, ID=-1):
    self.flight = flight
    self.customer = customer
    self.row = row
    self.column = column
    self.__id = ID
    self.__data = (flight, customer, row, column)
  
  def getID(self):
    return self.__id
    
  def __repr__(self):
    return self.__data
  
  def __str__(self):
    return str(self.flight) + " " + str(self.customer) + "\nRow " + self.row + " Seat " + self.column
  
  def saveToDatabase(self):
    cursor.execute(addReservation, self.__data)
    cnx.commit()
    cursor.execute(findID)
    self.__id = cursor.fetchone()
    self.__data = (self.flight, self.customer, self.row, self.column, self.__id)
  
  def update(self):
    self.__data = (self.flight, self.customer, self.row, self.column, self.__id)
    cursor.execute(updateReservation, self.__data)
    cnx.commit()
