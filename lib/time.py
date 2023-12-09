# function starts 
def time_converter(hour, minute, period):
    if period.lower() == "am":
        hour = hour % 12
    else:
        hour = (hour % 12) + 12

    formatted_time = f"{hour:02d}{minute:02d}"
    return formatted_time

# allows the user to input the hour within the range of 1-12
while True:
    try:
        hour = int(input("Enter hour (1 to 12): "))
        if 1 <= hour <= 12:
            break
        else:
            print("Please enter a valid hour between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# allows the user to input the min within the range of 0-59
while True:
    try:
        minute = int(input("Enter the minute (0 to 59): "))
        if 0 <= minute <= 59:
            break
        else:
            print("Please enter a valid minute between 0 and 59.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        
# allows the user to input the period of the time in a 12hour
while True:
    period = input("Enter 'am' or 'pm': ").lower()
    if period in ['am', 'pm']:
        break
    else:
        print("Please enter 'am' or 'pm'.")

result = time_converter(hour, minute, period)

print(f"The 24-hour time is: {result} hrs")