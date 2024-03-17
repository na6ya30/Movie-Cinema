"""Movie theatre ticketing system - v2
Get category and number of tickets required
"""
def sell_ticket():
    print("************ FanFare Movies - ticketing system *************")

    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_sale = 0
    """Component 2 Get category and number of tickets required"""
    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What type of ticket do you want: \n\
                            \t'A' for Adult, or\n\
                            \t'S' for student, or\n\
                            \t'C' for  child, or\n\
                            \t'G' for gift voucher\n\
                            >> ").upper()
        num_tickets = int(input(f"How many {ticket_type} tickets do you want: "))
        print(f"\nYou have ordered {num_tickets} {ticket_type} tickets(s)!")
        ticket_wanted = input("Do you want to order another ticket (Y/N): ").upper()

# main routine
sell_ticket()