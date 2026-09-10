# Cinema Booking System

A simple interactive command-line cinema booking system written in Python. It supports separate admin and user modes, movie management, sorting, ticket booking, payment confirmation, and a five-ticket limit per movie.

## Requirements

- Python 3.12 or newer
- Optional: `uv` for dependency and environment management

The application uses only the Python standard library at runtime. Movie data is stored in memory and is reset to the sample data whenever the program is restarted.

## Run the application

From the project directory, run:

```bash
python "UWE_ID_26031834_Aish Waheed.py"
```

With `uv`, run:

```bash
uv run "UWE_ID_26031834_Aish Waheed.py"
```

## Main menu

- **Admin**: open the admin tools after entering the admin password.
- **User**: browse available movies, book a ticket, or sort movies.
- **Back**: enter `0` to leave the current menu. Choosing `0` at the main menu exits the application.

## Admin mode

The default admin password is:

```text
Welcome@123
```

Admin users can:

- Add a movie with a title, ticket price, and screening date.
- Remove a movie by selecting its ID and confirming the deletion.
- View all movies, including fully booked movies.
- Sort movies by title, date, or price in ascending or descending order.

Movie dates must use `DD-MM-YYYY`, for example `25-12-2026`.

## User mode

Users can view movies with available booking spaces and select a movie by its ID. To complete a booking, enter the exact ticket price when prompted for payment. A successful booking increases the movie's booking count and displays a confirmation message.

Each movie allows a maximum of five bookings. Invalid menu choices, blank titles, invalid prices, invalid dates, and invalid numeric input are rejected and prompted again.

## Project files

- `UWE_ID_26031834_Aish Waheed.py`: application source code.
- `UWE_ID_26031834_Aish Waheed.ipynb`: notebook version of the assignment.
- `question.md`: assignment requirements.
- `pyproject.toml`: project metadata and dependencies.
