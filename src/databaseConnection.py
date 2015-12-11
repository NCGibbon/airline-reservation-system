import mysql.connector

cnx = mysql.connector.connect(user='', password='', host='', database='')  # add your own things here
cursor = cnx.cursor(buffered=True)

findID = ("SELECT LAST_INSERT_ID()")


# Plane-Related Queries

addPlane = ("INSERT INTO airplane "
            "(model, manufacturer, age) "
            "VALUES (%s, %s, %s)")
            
updatePlane = ("UPDATE airplane "
               "SET model = %s, manufacturer = %s, age = %s "
               "WHERE idairplane = %s")

deletePlane = ("DELETE FROM airplane WHERE idairplane = %s")
findPlaneByID = ("SELECT * FROM airplane WHERE idairplane = %s")
findPlanes = ("SELECT idairplane FROM airplane WHERE model=%s AND manufacturer=%s AND age=%s")



# Flight-Related Queries    

addFlight = ("INSERT INTO flight "
             "(origin, destination, departure, arrival, airplaneID, price, seatsLeft) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s)")
             
updateFlight = ("UPDATE flight "
                "SET origin = %s, destination = %s, departure = %s, arrival = %s, airplaneID = %s, "
                "price = %s, seatsLeft = %s"
                "WHERE idflight = %s")

deleteFlight = ("DELETE FROM flight WHERE idflight = %s")

findFlights = ("SELECT * FROM flight WHERE origin = %s AND destination = %s AND seatsLeft > 1")

findFlightByID = ("SELECT * FROM flight WHERE idflight = %s")



# Reservation-Related Queries
             
addReservation = ("INSERT INTO reservations (idflight, idcustomer, seatRow, seatCol) VALUES (%s, %s, %s, %s)")
                  
updateReservation = ("UPDATE reservations "
                     "idflight = %s, idcustomer = %s, seatRow = %s, seatCol = %s "
                     "WHERE idreservations = %s")
                     
selectSeat = ("UPDATE reservations SET seatRow = %s, seatCol = %s WHERE idflight = %s AND idcustomer = %s")

deleteReservation = ("DELETE FROM reservations "
                     "WHERE idreservations = %s")

getFlights = ("SELECT idflight FROM reservations "
              "WHERE idcustomer = %s")

getSeat = ("SELECT seatRow, seatCol FROM reservations WHERE idflight = %s")
getReservation = ("SELECT idreservations FROM reservations WHERE idflight = %s AND idcustomer = %s")
findByCustomer = ("SELECT * FROM reservations WHERE idcustomer = %s")
findByFlight = ("SELECT * FROM reservations WHERE idflight = %s")
findByID = ("SELECT * FROM reservations WHERE idreservations = %s")


              
# Passenger-Related Queries

addPassenger = ("INSERT INTO passengers "
                "(firstName, lastName, DOB, email, phone, billingName, cardType, cardNumber, securityNumber, expirationDate,"
                "address1, address2, city, state, ZIP, country) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                   
updatePassenger = ("UPDATE passengers "
                   "SET firstName = %s, lastName = %s, DOB = %s, email = %s, phone = %s, billingName = %s, cardType = %s,"
                   "cardNumber = %s, securityNumber = %s, expirationDate = %s, address1 = %s, address2 = %s, city = %s,"
                   "state = %s, ZIP = %s, country = %s "
                   "WHERE idpassengers = %s")

deletePassenger = ("DELETE FROM passengers WHERE idpassengers = %s")

findPassengerByID = ("SELECT * FROM passengers WHERE idpassengers = %s")
