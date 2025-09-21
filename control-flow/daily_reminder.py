# A simple personal daily reminder program

# Prompting user for the task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound (yes/no): ")

# Processing the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task that reqiures immediate attention today!"
    case "medium":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a medium priority task that should be completed today."
        elif time_bound == "no":
            reminder = f"Note: '{task}' is a medium priority task that can be scheduled for later."
        else:
            reminder = "Invalid input for time sensitivity. Please enter yes or no."
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered. Please enter high, medium, or low."
        
# Displaying the reminder
print(reminder)