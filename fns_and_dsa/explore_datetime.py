# A simple program to explore datetime
from datetime import datetime, timedelta

# Display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    
display_current_datetime()

# Calculate a future date
get_date = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    future_date = datetime.now() + timedelta(days=get_date)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    # future_date2 = date.today() + timedelta(days=get_date) # Alternate way to do it, after importing date
    # print("Future date:", future_date2)
    
calculate_future_date()