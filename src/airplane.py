from databaseConnection import *

class Airplane:
  def __init__(self, model, manufacturer, age, idairplane=-1):
    self.model = model
    self.manufacturer = manufacturer
    self.age = age
    self.__data = (model, manufacturer, age)
    self.__idairplane = idairplane
    
  def saveToDatabase(self):
    cursor.execute(addPlane, self.__data)
    cnx.commit()
    cursor.execute(findID, self.__data)
    self.__idairplane = cursor.fetchone()
    self.__data = (self.model, self.manufacturer, self.age, self.__idairplane)
  
  def __str__(self):
    return self.manufacturer + " " + self.model + " " + str(self.age)
  
  def __repr__(self):
    return self.__data
    
  def getID(self):
    return self.__idairplane
  
  def update(self):
    self.__data = (self.model, self.manufacturer, self.age, self.__idairplane)
    cursor.execute(updatePlane, self.__data)
    cnx.commit()
