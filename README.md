# Parking Lot Management System

This Python program provides a basic parking lot management system that allows users to assign parking spots and retrieve parking spot information by vehicle number. It is designed to manage two parking levels, A and B, each with 20 parking spots.

## How to Use

1. **Initialization**: The program initializes with two parking levels, A and B, with 20 parking spots each.

2. **Assign a Parking Spot (Option 1)**: Users can assign a parking spot by entering the vehicle number. The program will search for an available spot and assign it to the vehicle. If a spot is already assigned to the same vehicle number, it will display a message indicating that the vehicle is already in the parking lot. If all spots are occupied, it will indicate that the parking lot is full.

3. **Retrieve Parking Spot by Vehicle Number (Option 2)**: Users can retrieve a parking spot by entering the vehicle number. If the vehicle is found in the parking lot, it will display the level and spot number. If the vehicle is not found, it will display a message indicating that the vehicle is not in the parking lot.

4. **Exit (Option 3)**: Users can choose to exit the application.

## Usage

1. Run the program by executing `python parking_lot.py`.

2. You will be presented with a menu with three options:
   - Option 1: Assign a parking spot
   - Option 2: Retrieve parking spot by vehicle number
   - Option 3: Exit

3. Follow the on-screen instructions to assign or retrieve parking spots.

## Sample Output

Here are some sample interactions with the program:

Options:
1. Assign a parking spot
2. Retrieve parking spot by vehicle number
3. Exit
Enter your choice: 1
Enter vehicle number: ABC123
{"level": "A", "spot": "1"}

Options:
1. Assign a parking spot
2. Retrieve parking spot by vehicle number
3. Exit
Enter your choice: 2
Enter vehicle number: XYZ789
Vehicle not in the parking lot

Options:
1. Assign a parking spot
2. Retrieve parking spot by vehicle number
3. Exit
Enter your choice: 1
Enter vehicle number: ABC123
Vehicle with the same number already in the parking lot

Options:
1. Assign a parking spot
2. Retrieve parking spot by vehicle number
3. Exit
Enter your choice: 3
Exiting the application.
