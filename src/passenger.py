from databaseConnection import *

class Passenger:
  def __init__(self, firstname, lastname, DOB, email, phone, cardholder, cardType, cardNumber, securityNo, expiration,
                firstline, secondline, city, state, ZIP, country="America", ID=-1):
        
    self.first = firstname
    self.last = lastname
    self.dob = DOB
    self.email = email
    self.phone = phone
    self.cardholder = cardholder
    self.type = cardType
    self.number = cardNumber
    self.security = securityNo
    self.expiration = expiration
    self.firstline = firstline
    self.secondline = secondline
    self.city = city
    self.state = state
    self.zip = ZIP
    self.country = country
    self.__id = ID
    self.__data = (self.first, self.last, self.dob, self.email, self.phone, self.cardholder, 
                    self.type, self.number, self.security, self.expiration,
                    self.firstline, self.secondline, self.city, 
                    self.state, self.zip, self.country)
  
  def saveToDatabase(self):
    cursor.execute(addPassenger, self.__data)
    cnx.commit()   
    cursor.execute(findID)
    self.__id = cursor.fetchone()[0]
    self.__data = (self.first, self.last, self.dob, self.email, self.phone, self.cardholder, 
                    self.type, self.number, self.security, self.expiration,
                    self.firstline, self.secondline, self.city, 
                    self.state, self.zip, self.country, self.__id)
    
  def getID(self):
    return self.__id
    
  def __repr__(self):
    return self.__data
  
  def __str__(self):
    return self.first + " " + self.last + " " + self.__id
    
  def update(self):
    self.__data = (self.first, self.last, self.dob, self.email, self.phone, self.cardholder, 
                    self.type, self.number, self.security, self.expiration,
                    self.firstline, self.secondline, self.city, 
                    self.state, self.zip, self.country, self.__id)
    cursor.execute(updatePassenger, self.__data)
    cnx.commit()
