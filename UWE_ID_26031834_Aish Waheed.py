# Imports datetime so movie dates can be stored and formatted properly.
from datetime import datetime

# Maximum number of bookings allowed per movie.
MAX_BOOKINGS = 5

# Password required to access admin mode.
PASSWORD = "Welcome@123"

# Tracks the latest movie ID so new movies can receive unique IDs.
last_movie_id = 1005


# Stores all movie records in memory.
# Each movie is represented as a dictionary with an ID, title, price, date, and booking count.
movies = [
    {
        "id": 1000,
        "title": "Inception",
        "price": 10.0,
        "date": datetime(2026, 5, 1),
        "bookings": 0,
    },
    {
        "id": 1001,
        "title": "The Dark Knight",
        "price": 12.5,
        "date": datetime(2026, 5, 2),
        "bookings": 0,
    },
    {
        "id": 1002,
        "title": "Interstellar",
        "price": 11.0,
        "date": datetime(2026, 5, 3),
        "bookings": 5,
    },
    {
        "id": 1003,
        "title": "Avengers: Endgame",
        "price": 13.0,
        "date": datetime(2026, 5, 4),
        "bookings": 5,
    },
    {
        "id": 1004,
        "title": "Spider-Man: No Way Home",
        "price": 12.0,
        "date": datetime(2026, 5, 5),
        "bookings": 0,
    },
]


def prompt_confirm(message):
    # Asks the user to confirm an action using Y or N.
    # Returns True only when the user enters "y".
    input_confirm = input(f"\n{message} ([Y]es / [N]o) => ")
    if input_confirm.strip().lower() == "y":
        return True
    else:
        return False


def prompt_choice(message):
    # Repeatedly asks the user for a valid integer input.
    # Used for menu choices and movie ID selection.
    while True:
        # Infinite loop used intentionally
        # Breaks only when valid input is received
        choice = input(f"\n{message}")
        try:
            choice = int(choice.strip())
            return choice
        except ValueError:
            print("\n[!] Choose a valid option")
        # Prevents program crash when user enters invalid input


def prompt_date():
    # Repeatedly asks the user for a date in DD-MM-YYYY format.
    # Converts the valid input into a datetime object.
    while True:
        input_date = input("Enter movie date (DD-MM-YYYY) => ")
        try:
            input_date = datetime.strptime(input_date.strip(), "%d-%m-%Y")
            return input_date
        except ValueError:
            print("\n[!] Input a valid date in the format DD-MM-YYYY")


def prompt_title():
    # Repeatedly asks the user for a movie title.
    # Prevents blank or whitespace-only titles from being accepted.
    while True:
        input_title = input("Enter the Movie title => ").strip()
        if not input_title:
            print("\n[!] Title can't be blank or only whitespaces")
        else:
            return input_title


def prompt_float(message):
    # Repeatedly asks the user for a valid decimal number.
    # Used for values such as ticket price and payment amount.
    while True:
        input_float = input(message)
        try:
            input_float = float(input_float.strip())
            return input_float
        except ValueError:
            print("\n[!] Enter a valid value")


def run_menu(menu_list, menu_title):
    # Displays a reusable menu using the menu title and list of menu options.
    # Each menu item contains text to display and an action function to run.
    # The loop continues until the user chooses 0 to go back.
    while True:
        print("=" * 90)
        print(f" {menu_title:^90}")
        print("=" * 90)

        for i, item in enumerate(menu_list, start=1):
            # enumerate gives (index, value)
            # start=1 makes menu numbering user-friendly instead of starting at 0

            print(f"  [{i}] {item['entry_name']}")
        print("  [0] Back")
        print("_" * 90)
        choice = prompt_choice("Choose an option => ")

        if choice == 0:
            break

        if choice < 0 or choice > len(menu_list):
            print("\n[!] Enter a valid choice")
            continue
        print("-" * 90)
        menu_list[choice - 1]["action"]()
        # Access selected menu item
        # Retrieve its stored function
        # Execute it immediately using ()


def add_movie():
    # Allows the admin to add a new movie.
    # Collects title, price, and date from the user.
    # Automatically assigns a new unique movie ID and sets bookings to 0.
    new_movie = {
        "title": prompt_title(),
        "price": prompt_float("Enter price => "),
        "date": prompt_date(),
        "bookings": 0,
    }
    global last_movie_id
    # Allows modification of global variable inside function
    # Without this, Python would treat it as a local variable
    last_movie_id += 1
    new_movie["id"] = last_movie_id
    movies.append(new_movie)


def list_movies(show_booked=True):
    # Displays movies in a formatted table.
    # Used by both admin mode and user mode.
    movies_list = (
        movies if show_booked else [x for x in movies if x["bookings"] < MAX_BOOKINGS]
    )
    # If show_booked is True → use full list
    # Else → create a new filtered list of only movies with available slots
    # Uses list comprehension for compact filtering

    print("=" * 90)
    print(
        f"{'Sn':<5.4}"
        f"{'ID':<8}"
        f"{'Title':<32.30}"
        f"{'Price':>10.8}"
        f"{'Date':>15}"
        f"{'Bookings':>15.13}"
    )
    # Formats table headers with alignment:
    # < = left aligned, > = right aligned
    # Numbers control column width and truncation
    print("-" * 90)

    if not movies_list:
        print(f"{'No movies available':^90}")
    else:
        for index, item in enumerate(movies_list, start=1):
            formatted_date = datetime.strftime(item["date"], "%d-%b-%y")
            # Converts datetime object into readable string format (e.g., 01-May-26)
            print(
                f"{index:<5}"
                f"{item['id']:<8}"
                f"{item['title']:<32.30}"
                f"{item['price']:>10.2f} "
                f"{formatted_date:>15}"
                f"{f'{item["bookings"]}/{MAX_BOOKINGS}':>15}"
                # Inner f-string creates "current/max" format (e.g., 2/5)
                # Outer f-string aligns the final string to the right
            )
    print("=" * 90)


def select_movie():
    # Displays the movie list and asks the user to select a movie by ID.
    # Returns both the movie index and movie dictionary when found.
    # Returns None if the user cancels the selection.
    print("-" * 90)
    print(f" {'Select Movie':^90}")
    print("*" * 90)
    list_movies()
    print("\n  [0] Cancel Selection")
    while True:
        choice = prompt_choice("\nEnter ID of movie to select => ")
        if choice == 0:
            return None
        selected_movie = next(
            ((i, m) for i, m in enumerate(movies) if m["id"] == choice), None
        )
        # Generator expression loops through movies one by one
        # Stops at FIRST match where movie ID equals user choice
        # next(..., None) → returns None if no match found
        if selected_movie is None:
            print(f"\n[!] Movie of ID:[{choice}] not found. Try again.")
            continue
        return selected_movie


def remove_movie():
    # Allows the admin to remove a selected movie.
    # Confirms the action before deleting.
    # Gives an extra warning if the movie already has bookings.
    selected_movie = select_movie()
    if selected_movie is None:
        return
    confirmed = prompt_confirm(
        f'\n>>> Are you sure you want to delete "{selected_movie[1]["title"]}" ?'
    )
    if selected_movie[1]["bookings"] > 0 and confirmed:
        confirmed = prompt_confirm(
            f"\n>>> The movie you are about to delete has been booked {selected_movie[1]['bookings']} times.\nDo you still want to proceed ?"
        )
    if confirmed:
        movies.pop(selected_movie[0])
        # Removes movie using its index (not ID)
        # selected_movie[0] is the index from enumerate()
    else:
        print("\n>>> Cancelled")


def view_all(show_booked=True):
    # Displays a heading before showing the movie list.
    # Passes the show_booked value to list_movies().
    print("-" * 90)
    print(f" {'All Movies':^90}")
    print("*" * 90)
    list_movies(show_booked)


def sort_movies_list(key, desc=False):
    # Sorts the global movies list using the selected dictionary key.
    movies.sort(key=lambda m: m[key], reverse=desc)
    # lambda extracts the value to sort by (title, price, date, etc.)
    # reverse=desc → controls ascending/descending order
    print("\n[OK] Movies sorted")
    view_all()


def payment_confirmation(movie_index):
    # Gets the selected movie price and asks the user to enter the payment amount.
    # Payment succeeds only if the entered amount exactly matches the ticket price.
    actual_amount = movies[movie_index]["price"]
    payment_amount = prompt_float("Enter Payment amount to confirm => ")
    if payment_amount != actual_amount:
        print("\n[!] Payment Failed")
        return False
    else:
        print("\n[OK] Payment Successful")
        return True


def book_ticket():
    # Handles the full booking process.
    # Lets the user select an available movie, confirms payment, and increases the booking count.
    while True:
        selected = select_movie()
        if selected is None:
            return
        if selected[1]["bookings"] < MAX_BOOKINGS:
            # Ensures movie is not fully booked before allowing purchase
            break
        print("\n[!] This movie has been fully booked. Try another movie.")
    payment_confirmed = payment_confirmation(selected[0])
    if not payment_confirmed:
        print("\n>>> Booking Cancelled")
        return
    selected[1]["bookings"] += 1
    # selected is a tuple: (index, movie_dict)
    # selected[1] accesses the movie dictionary
    # Increment booking count by 1
    print(f"\n[OK] Movie ticket for [{selected[1]['title']}] has been booked.")
    return


# Menu used for sorting movies by title, date, or price.
sort_menu_list = [
    {
        "entry_name": "Sort by Title (A to Z)",
        "action": lambda: sort_movies_list("title"),
        # lambda prevents function from running immediately
        # It runs only when the menu option is selected
    },
    {
        "entry_name": "Sort by Title (Z to A)",
        "action": lambda: sort_movies_list("title", desc=True),
    },
    {"entry_name": "Sort by Earliest", "action": lambda: sort_movies_list("date")},
    {
        "entry_name": "Sort by Latest",
        "action": lambda: sort_movies_list("date", desc=True),
    },
    {
        "entry_name": "Sort by Price (Lowest)",
        "action": lambda: sort_movies_list("price"),
    },
    {
        "entry_name": "Sort by Price (Highest)",
        "action": lambda: sort_movies_list("price", desc=True),
    },
]


# Menu used by the admin after entering the correct password.
# Allows adding, removing, viewing, and sorting movies.
admin_menu_list = [
    {"entry_name": "Add Movie", "action": add_movie},
    {"entry_name": "Remove Movie", "action": remove_movie},
    {"entry_name": "View All Movies", "action": view_all},
    {
        "entry_name": "Sort Movies",
        "action": lambda: run_menu(sort_menu_list, "Sort Movies"),
    },
]


def admin_mode():
    # Checks the admin password before opening the admin menu.
    # If the password is wrong, access is denied.
    password_input = input("Enter Admin Password => ")
    if password_input != PASSWORD:
        print("\n[!] Invalid Password.")
        return
    run_menu(admin_menu_list, "Admin Mode")


# Menu used by regular users.
# Users can view available movies, book tickets, and sort movie listings.
user_menu_list = [
    {
        "entry_name": "View All Movies",
        "action": lambda: view_all(show_booked=False),
    },
    {"entry_name": "Book Movie Ticket", "action": book_ticket},
    {
        "entry_name": "Sort Movies",
        "action": lambda: run_menu(sort_menu_list, "Sort Movies"),
    },
]


# Main menu of the application.
# Allows the user to choose between Admin mode and User mode.
main_menu_list = [
    {"entry_name": "Admin", "action": admin_mode},
    {"entry_name": "User", "action": lambda: run_menu(user_menu_list, "User Mode")},
]


def main():
    # Starts the cinema booking system.
    # Displays the main title and opens the main menu.
    print("\n" + "#" * 90)
    print(f"{'CINEMA BOOKING SYSTEM':^90}")
    print("#" * 90)

    run_menu(main_menu_list, "Main Menu")

    print(f"\n>>> {'Exiting Application'}")


# Runs the program only when this file is executed directly.
# Prevents main() from running automatically if the file is imported elsewhere.
if __name__ == "__main__":
    main()
