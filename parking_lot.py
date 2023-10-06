class Parkinglot:
    def __init__(self):
        # Initialize two parking levels, A and B, each with 20 parking spots.
        self.level_A = {str(i): "" for i in range(1, 21)}
        self.level_B = {str(i): "" for i in range(21, 41)}

    def assign_parking_spot(self, vehicle_number):
        # Loop through both parking levels.
        for level, spots in [("A", self.level_A), ("B", self.level_B)]:
            for spot, v_number in spots.items():
                if v_number == vehicle_number:
                    return "Vehicle with the same number already in the parking lot"
                if v_number == "":
                    # If the parking spot is empty, assign it to the vehicle and return the spot information.
                    spots[spot] = vehicle_number
                    return {"level": level, "spot": spot}
        
        # If all spots are occupied, return a message indicating that the parking lot is full.
        return "Parking lot full"

    def get_parking_spot(self, vehicle_number):
        # Loop through both parking levels.
        for level, spots in [("A", self.level_A), ("B", self.level_B)]:
            for spot, v_number in spots.items():
                if v_number == vehicle_number:
                    # If the vehicle is found, return the spot information.
                    return {"level": level, "spot": spot}
        
        # If the vehicle is not found in the parking lot, return a message indicating that it's not present.
        return "Vehicle not in the parking lot"

def main():
    pl = Parkinglot()
    while True:
        print("\nOptions:")
        print("1. Assign a parking spot")
        print("2. Retrieve parking spot by vehicle number")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            result = pl.assign_parking_spot(vehicle_number)
            print(result)

        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            result = pl.get_parking_spot(vehicle_number)
            print(result)
        
        elif choice == "3":
            print("Exiting the application. ")
            break

        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
