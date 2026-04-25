# POP
Assignment Task: You have been hired to develop a simple CLI-based Cinema Booking System. The system should allow users to act as either an "Admin" or a "User".
Your program should support the following functionalities:
1. Admin Mode:
    * Add movies with a title, price, and date.
    * Remove movies by selecting from the list.
    * View all available movies.
    * Sort
2. User Mode:
    * View available movies.
    * Select a movie to book a ticket.
    * Write price to confirm
    * Display a confirmation message when a ticket is booked.
    * Sort
## Constraints:
* Do not use a database or external files, store movie data in memory (lists/dictionaries).
* The program should run in a loop until the user chooses to exit.
* Implement simple validation to prevent errors (e.g., empty movie list, invalid inputs).
## Bonus Challenge (Optional):
* Allow multiple users to book tickets and track the number of tickets booked.
* Limit ticket bookings per movie (e.g., max 5 tickets per movie).
* Implement a simple payment simulation where the user "enters" an amount and checks if it matches the price.