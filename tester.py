import datetime
import random

# Dictionary to store room availability (mock data)
ROOMS = {
    "single": {"total": 10, "booked": 2, "price": 100},
    "double": {"total": 8, "booked": 3, "price": 150},
    "suite": {"total": 5, "booked": 1, "price": 250},
}


def greet_user():
    """Greet the user and introduce the chatbot."""
    print("Hello! Welcome to Hotel Sunshine Booking Assistant.")
    print("I'm here to help you book a room. May I know your name?")


def get_user_name():
    """Get the user's name."""
    return input("Your Name: ").strip()


def display_room_options():
    """Display available room types and their prices."""
    print("\nWe have the following room types available:")
    for room_type, details in ROOMS.items():
        available = details["total"] - details["booked"]
        print(
            f"- {room_type.capitalize()} Room: ${details['price']} per night "
            f"(Available: {available})"
        )


def check_availability(room_type, num_rooms):
    """Check if the requested number of rooms is available."""
    room_type = room_type.lower()
    if room_type not in ROOMS:
        return False, "Sorry, invalid room type."
    available = ROOMS[room_type]["total"] - ROOMS[room_type]["booked"]
    if available >= num_rooms:
        return True, f"We have {available} {room_type} rooms available."
    else:
        return False, f"Sorry, only {available} {room_type} rooms are available."


def get_booking_details():
    """Collect booking details from the user."""
    print("\nLet's get your booking details.")
    display_room_options()
    room_type = input("Which room type would you like to book? (Single/Double/Suite): ")
    num_rooms = int(input("How many rooms would you like to book?: "))
    check_in = input("Check-in date (YYYY-MM-DD): ")
    check_out = input("Check-out date (YYYY-MM-DD): ")
    return room_type, num_rooms, check_in, check_out


def calculate_cost(room_type, num_rooms, check_in, check_out):
    """Calculate the total cost of the booking."""
    check_in_date = datetime.datetime.strptime(check_in, "%Y-%m-%d")
    check_out_date = datetime.datetime.strptime(check_out, "%Y-%m-%d")
    num_nights = (check_out_date - check_in_date).days
    cost_per_night = ROOMS[room_type.lower()]["price"]
    total_cost = cost_per_night * num_rooms * num_nights
    return total_cost, num_nights


def confirm_booking(name, room_type, num_rooms, check_in, check_out, total_cost):
    """Confirm the booking with the user."""
    print(f"\nDear {name}, here are your booking details:")
    print(f"Room Type: {room_type.capitalize()}")
    print(f"Number of Rooms: {num_rooms}")
    print(f"Check-in Date: {check_in}")
    print(f"Check-out Date: {check_out}")
    print(f"Total Cost: ${total_cost}")
    confirmation = input("Do you want to confirm this booking? (yes/no): ").lower()
    return confirmation == "yes"


def update_room_availability(room_type, num_rooms):
    """Update the booked rooms in the ROOMS dictionary."""
    ROOMS[room_type.lower()]["booked"] += num_rooms


def generate_booking_id():
    """Generate a random booking ID."""
    return f"BK{random.randint(1000, 9999)}"


def main():
    """Main function to run the hotel booking chatbot."""
    greet_user()
    name = get_user_name()
    print(f"Nice to meet you, {name}! Let's proceed with your booking.")

    while True:
        try:
            room_type, num_rooms, check_in, check_out = get_booking_details()
            is_available, message = check_availability(room_type, num_rooms)
            print(message)

            if not is_available:
                retry = input("Would you like to try a different room type or number? (yes/no): ").lower()
                if retry != "yes":
                    print("Thank you for visiting Hotel Sunshine. Goodbye!")
                    break
                continue

            total_cost, num_nights = calculate_cost(room_type, num_rooms, check_in, check_out)
            if confirm_booking(name, room_type, num_rooms, check_in, check_out, total_cost):
                update_room_availability(room_type, num_rooms)
                booking_id = generate_booking_id()
                print(f"\nBooking confirmed! Your Booking ID is {booking_id}.")
                print("Thank you for choosing Hotel Sunshine. We look forward to hosting you!")
            else:
                print("\nBooking cancelled. Thank you for considering Hotel Sunshine.")
            break

        except ValueError:
            print("Invalid input. Please enter valid numbers or dates.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    exit_choice = input("\nWould you like to make another booking? (yes/no): ").lower()
    if exit_choice == "yes":
        main()
    else:
        print("Thank you for using Hotel Sunshine Booking Assistant. Goodbye!")


if __name__ == "__main__":
    main()