'''to calculate the amount each participant should pay for an event'''

# input of total event cost from user
total_event_cost = float(input("Enter the total event cost: "))

# input of number of participants from user
number_of_participants = int(input("Enter the number of participants: "))

# calculation of amount per participant
print("Amount per Participant is: ", total_event_cost / number_of_participants)