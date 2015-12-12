# airline-reservation-system

Intro
------
I made this for one of my classes. It's pretty okay.

Some things it's not:
* secure
* comprehensive
* secure

No, but seriously this is not secure. I *could* make it secure, but I have neither the time nor the motivation to do that.

Start it by running initial.py. You'll need the [MySQL connector](http://dev.mysql.com/downloads/connector/python/) for Python 3.4, and the tkinter library. You'll also need to have a MySQL database set up, and the credentials inserted in databaseConnection.py.

The Database
-------------
The database will need 4 tables: airplane, flight, passengers, and reservations.

table name | column name | data type
-----------|-------------|----------
**airplane** | model           | VARCHAR
             | manufacturer    | VARCHAR
             | age             | VARCHAR
             | idairplane (PK) | INT
**flight** | origin        | VARCHAR
           | destination   | VARCHAR
           | departure     | VARCHAR
           | arrival       | VARCHAR
           | airplaneID    | INT
           | price         | INT
           | seatsLeft     | INT
           | idflight (PK) | INT
**reservations** | idflight            | INT
                 | idcustomer          | INT
                 | seatRow             | INT
                 | seatCol             | INT
                 | idreservations (PK) | INT
**passengers** | firstName         | VARCHAR
               | lastName          | VARCHAR
               | DOB               | VARCHAR
               | email             | VARCHAR
               | phone             | VARCHAR
               | billingName       | VARCHAR
               | cardType          | VARCHAR
               | cardNumber        | VARCHAR
               | securityNumber    | INT
               | expirationDate    | VARCHAR
               | address1          | VARCHAR
               | address2          | VARCHAR
               | city              | VARCHAR
               | state             | VARCHAR
               | ZIP               | VARCHAR
               | country           | VARCHAR
               | idpassengers (PK) | INT


Again, I used MySQL for this, so that's going to be the most compatible. However, to my knowledge, there's nothing tying the queries themselves to any specific version of SQL. You'd have to figure out the connector stuff, but have at it.
