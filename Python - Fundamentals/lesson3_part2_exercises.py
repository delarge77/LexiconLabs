# Part 1 create departure data

flights_info = [
    {
        "number": 756,
        "destination": "Los Angeles",
        "departure_time": "8:30",
        "gate": "A4",
        "passengers": 135,
        "maximum_capacity": 180,
        "delay_in_minutes": 0,
        "cancelled_status": False
    },
    {
        "number": 757,
        "destination": "Miami",
        "departure_time": "11:00",
        "gate": "B4",
        "passengers": 132,
        "maximum_capacity": 180,
        "delay_in_minutes": 0,
        "cancelled_status": False
    },
    {
        "number": 758,
        "destination": "Copenhagen",
        "departure_time": "9:00",
        "gate": "C4",
        "passengers": 132,
        "maximum_capacity": 180,
        "delay_in_minutes": 100,
        "cancelled_status": True
    },
    {
        "number": 759,
        "destination": "Helsink",
        "departure_time": "17:00",
        "gate": "D4",
        "passengers": 0,
        "maximum_capacity": 180,
        "delay_in_minutes": 100,
        "cancelled_status": False
    },
    {
        "number": 760,
        "destination": "Oslo",
        "departure_time": "15:30",
        "gate": "D4",
        "passengers": 130,
        "maximum_capacity": 180,
        "delay_in_minutes": 10,
        "cancelled_status": False
    },
    {
        "number": 761,
        "destination": "Oslo",
        "departure_time": "15:30",
        "gate": "",
        "passengers": 130,
        "maximum_capacity": 180,
        "delay_in_minutes": 10,
        "cancelled_status": False
    }
]

# Part 2 - Process the departure board
# for flight_info in flights_info:
#     print(flight_info["destination"][:2].upper()+str(flight_info["number"])+ " - ",flight_info["destination"]+ " - ",flight_info["departure_time"]+ " - GATE",flight_info["gate"])
# # EX: SK142 - London - 14:30 - GATE B4

# Part 3 
# for flight_info in flights_info:
#     if flight_info["cancelled_status"] == True:
#         print(flight_info["destination"][:2].upper()+str(flight_info["number"])+ " - ",flight_info["destination"]+ " - ","CANCELLED")
#         continue
#     if flight_info["cancelled_status"] == False and flight_info["delay_in_minutes"] >=1 and flight_info["delay_in_minutes"] <= 19:
#         print(flight_info["destination"][:2].upper()+str(flight_info["number"])+ " - ",flight_info["destination"]+ " - ","SLIGHT_DELAY")
#     elif flight_info["cancelled_status"] == False and flight_info["delay_in_minutes"] >=20 and flight_info["delay_in_minutes"] <= 59:
#         print(flight_info["destination"][:2].upper()+str(flight_info["number"])+ " - ",flight_info["destination"]+ " - ","DELAYED")
#     elif flight_info["cancelled_status"] == False and flight_info["delay_in_minutes"] >= 59:
#         print(flight_info["destination"][:2].upper()+str(flight_info["number"])+ " - ",flight_info["destination"]+ " - ","SEVERELY DELAYED")
#     else:
#         print(flight_info["destination"][:2].upper()+str(flight_info["number"])+ " - ",flight_info["destination"]+ " - ","ON TIME")

# Part 4 - Analyse the flights
# Number of flights scheduled
# print("Number of flights scheduled:", len(flights_info))

# Number of cancelled flights
# cancelled = 0 
# for flight in flights_info:
#     if flight["cancelled_status"] == True:
#         cancelled = cancelled + 1 

# print("Flights cancelled:", cancelled)

# Number of delayed flights
# delayed = 0 
# for flight in flights_info:
#     if flight["delay_in_minutes"] >= 1:
#         delayed = delayed + 1 

# print("Flights delayed:", delayed)

# Number of flights departing on time
# onTime = 0 
# for flight in flights_info:
#     if flight["delay_in_minutes"] == 0:
#         onTime = onTime + 1 

# print("Flights departing on time:", onTime)

# Total number of passengers
# passengers = 0 
# for flight in flights_info:
#     passengers = passengers + flight["passengers"]

# print("Total number of passengers:", passengers)

# Average number of passengers per flight
# passengers = 0 
# for flight in flights_info:
#     passengers = passengers + flight["passengers"]

# print("Average number of passengers per flight:", passengers // len(flights_info))

# Flight with largest number of passengers
# passengers = 0 
# flightMax = {}
# for flight in flights_info:
#     if flight["passengers"] > passengers:
#         passengers = flight["passengers"]
#         flightMax = {"destination":flight["destination"], "number":flight["number"]}

# # print("Flight with largest number of passengers:", flightMax["destination"][:2].upper()+str(flightMax["number"]))
# flight = flightMax["destination"][:2].upper()+str(flightMax["number"])
# print(f"Flight with largest number of passengers: {flight} with: {passengers}")

# Number of flights with more than 80% of their capacity filled
# max_capacity = 0 
# flightMax = []
# for flight in flights_info:
#     if flight["passengers"] >= flight["maximum_capacity"] * 0.8:
#         print(flight["destination"])
#         flightMax.append(flight)

# print(len(flightMax))

# 5 Search for a flight
def search_flight():
     flight_number = int(input("Enter flight number: "))
     flightFound = {}
     for flight in flights_info:
        if flight["number"] == flight_number:
             flightFound = flight
             break
        else:
             flightFound = {}
     if len(flightFound) > 0:
        flight = flightFound["destination"][:2].upper()+str(flightFound["number"])
        print(f"Flight was found: {flight}")
     else:
        print("Flight not find")


# 6 Handle unvailable flights

def delayed_flights():
    delayed_flights = []
    for flight in flights_info:
        if flight["delay_in_minutes"] > 0 :
            delayed_flights.append(flight)
    if len(delayed_flights) > 0:
        print(*delayed_flights)
    else:
        print("There are no delayed flights")


def view_all_flights():
     passengers = 0

     for flight_info in flights_info:
        flight_time = f" - {flight_info['departure_time']}" if flight_info["cancelled_status"] != True else "FLIGHT CANCELLED"
        flight_gate = f"GATE {flight_info['gate']}" if flight_info["gate"] != "" else "GATE NOT ASSIGNED"

        if flight_info["passengers"] > 0:
            for flight in flights_info: 
                 passengers = passengers + flight["passengers"]

        print(flight_info["destination"][:2].upper()+str(flight_info["number"])+ " - ",flight_info["destination"]+ " - ",flight_time+ " - ",flight_gate)
     print("Average number of passengers per flight:", passengers // len(flights_info))

# 7

def handle_input(option):
    if option == 1:
        view_all_flights()
    elif option == 2:
        delayed_flights()
    elif option == 3:
        print("Option 3")
    elif option == 4:
        search_flight()
    elif option == 5:
        print("Option 5")
    else:
        print("Option 6")


def showAirportMenu():
    print("AIRPORT DEPARTURE SYSTEM")
    print("1. View all flights")
    print("2. View delayed flights")
    print("3. View cancelled flights")
    print("4. Search for a flight")
    print("5. View flights statistics")
    print("6. Quit")
    option = int(input("Choose an option: "))

    handle_input(option)

showAirportMenu()
