# A simple personal daily reminder program

# Prompting user for the task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Processing the task based on priority and time sensitivity
match priority:
    case "high":
        customized_reminder = "is a high priority task that reqiures immediate attention today!"
    case "medium":
        if time_bound == "yes":
            customized_reminder = "is a medium priority task that should be completed today."
        elif time_bound == "no":
            customized_reminder = "is a medium priority task that can be scheduled for later."
        else:
            print ("Invalid input for time sensitivity. Please enter yes or no.")
    case "low":
        reminder = "is a low priority task. Consider completing it when you have free time."
    case _:
        print ("Invalid priority level entered. Please enter high, medium, or low.")
        
# Displaying the reminder
print(f"Reminder: '{task}' {customized_reminder}")