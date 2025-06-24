import sys #sys package will be used for value exception handling

# ask the user for their starting debt amount as an integer
debt = int(input("Enter debt amount: "))

# handle value exceptions with sys.exit
if debt <= 0:
    sys.exit("Error: Input must be a positive number.")

# ask the user for their preferred plan, use .lower() method to standardize input
choice = input("Would you like to make a plan based on a timeline or a monthly payment amount? (timeline/payment):").lower()

# handle value exceptions
if choice != "timeline" and choice != "payment":
    sys.exit("Error: Please type either 'timeline' or 'payment'.")

# set variables for the next if/else statements
time_frame = 0
payment_amount = 0

# if/else statements to print follow-up questions based on input
if choice == "timeline":
    time_frame = int(input("Over how many months would you like to pay back your debt?"))
else:
    payment_amount = int(input("Enter desired payment amount: "))

# if/else statements to calculate and print the final output for the user
if time_frame != 0:
    plan_amt = round(debt/time_frame,2) # divide debt by desired # of months, use round() function to shorten to the hundredths place
    print("To pay off your debt in", time_frame, "months, you will need to pay $", plan_amt, "each month.")
else:
    plan_time = round(debt/12) # divide debt by 12 for a monthly value, use round() function to shorten to the hundredths place
    print("It will take ", plan_time, "months to pay off your debt.")