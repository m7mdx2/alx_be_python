task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority entered."

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium", "low"]:
    reminder += ". Consider completing it when you have free time."
else:
    reminder = "Invalid input for time sensitivity."

print("Reminder:", reminder)
