# Part A
"""
Author: Mariia Shmidt
Assignment #1
"""

# Part B
# String
gym_member = "Alex Alliton"
# Float number
preferred_weight_kg = 20.5
# Integer
highest_reps = 25
# Boolean
membership_active = True

# Part C
# Dictionary
# Keys are string type. Values are tuples with integers.
workout_stats = {"Alex": (30,45,20), "Taylor": (20,20,20), "Jaime": (50, 60, 10)}

# Part D
# Calculate workout total
workout_stats_copy = workout_stats.copy()
for person, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    workout_stats_copy[f"{person}_Total"] = total_minutes
print(f"Dictionary with total workout stats: {workout_stats_copy}")

# Part E
# Each row of the nested list is a list with integers
workout_list = [list(minutes) for person, minutes in workout_stats.items()]
for i in workout_list:
    print(i)

# Part F
yoga_minutes = [row[:2] for row in workout_list]
print(f"Yoga and Running minutes for everyone: {yoga_minutes}")

weight_minutes = [row[2] for row in workout_list[1:]]
print(f"Weightlifting minutes for last two friends: {weight_minutes}")

# Part G
for person, total in workout_stats_copy.items():
    if person.endswith("_Total") and total >= 120:
        name = person.replace("_Total", "")
        print(f"Great job staying active, {name}!")

# Part H
friend_name = input("Enter the name: ")
if friend_name in workout_stats:
    yoga, running, weightlifting = workout_stats[friend_name]
    total_minutes = sum(workout_stats[friend_name])

    print(f"{friend_name} Workout Minutes:")
    print(f"- Yoga: {yoga} minutes")
    print(f"- Running: {running} minutes")
    print(f"- Weightlifting: {weightlifting} minutes")
    print(f"- Total: {total_minutes} minutes")
else:
    print(f"Friend {friend_name} not found in the records.")

# Part I
total_workouts = {friend: total for friend, total in workout_stats_copy.items() if friend.endswith("_Total")}
max_workout = max(total_workouts)
print(f"{max_workout.replace('_Total', '')} has the highest total of workout minutes.")
min_workout = min(total_workouts)
print(f"{min_workout.replace('_Total', '')} has the lowest total of workout minutes.")