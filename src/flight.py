from databaseConnection import *

class Flight:
  def __init__(self, origin, destination, departure, arrival, airplaneid, price, seatsLeft=99, ID=-1):
    self.origin = origin
    self.destination = destination
    self.departure = departure
    self.arrival = arrival
    self.airplaneID = airplaneid
    self.seatsLeft = seatsLeft
    self.price = price
    self.__id = ID
    self.__data = (origin, destination, departure, arrival, airplaneid, price, seatsLeft)
     
  def saveToDatabase(self):
    cursor.execute(addFlight, self.__data)
    cnx.commit()
    cursor.execute(findID)
    self.__id = cursor.fetchone()
    self.__data = (self.origin, self.destination, self.departure, self.arrival, self.airplaneID, self.price, self.seatsLeft, self.__id)

  def getID(self):
    return self.__id
    
  def __str__(self):
    return str(self.__id) + "\t" + self.origin + " " + self.destination + "\n\t" + self.departure + " " + self.arrival + "\n\t" + str(self.airplaneID)
            
  def __repr__(self):
    return self.__data
    
  def update(self):
    self.__data = (self.origin, self.destination, self.departure, self.arrival, self.airplaneID, self.price, self.seatsLeft, self.__id)
    cursor.execute(updateFlight, self.__data)      
    cnx.commit()
