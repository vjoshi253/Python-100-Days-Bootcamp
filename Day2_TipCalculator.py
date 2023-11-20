# Greetings for the users.
print("Welcome to the tip calculator.")

# Get the total bill from the user.
total_bill = input("What was the total bill? ")

# Get the tip information from the user.
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

# Remove the $ sign from input if present.
if total_bill[0] == "$":
	total_bill = total_bill[1:]

# Convert the string input to float.
total_bill = float(total_bill)
tip_percentage = float(tip_percentage)

# Calculate the tip using the user provided tipping percentage.
total_tip = (total_bill * tip_percentage)/100

# Get the total number of people.
total_people = int(input("How many people to split the bill? "))

# Calculate the share of each person including the tip.
per_person_split = (total_bill + total_tip) / total_people

# Round the result to 2 decimal places. 
per_person_split = "{:.2f}".format(per_person_split)
print(f"Each person should pay: ${per_person_split}")


