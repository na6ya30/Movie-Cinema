"""Movie theatre ticketing system - v4
confirm order
"""
def confirm_order(ticket, number, cost):
    """confirms ticket order"""
    confirm = ""
    while confirm != "Y" and confirm != 'N':
        confirm = input(f"\nYou have ordered {number} {ticket} ticket(s) at a cost of ${cost * number:.2f}\n'Y' or 'N'").upper()
    if confirm == 'Y':
        return True
    else:
        return  False

def get_price(type_):
    """calculate price"""
    prices = [["A", 12.5,],["C", 7],["S", 9],["G", 0]]
    for price in prices: 
        if price[0] == type_: 
            return price[1]

def sell_ticket():
    """component 1 of project: welcome screen and set up variables"""

    print("************ FanFare Movies - ticketing system *************")

    print ("welcome to fanfare movies")

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
                            \t'A' for adult, or\n\
                            \t'S' for student, or\n\
                            \t'C' for  child, or\n\
                            \t'G' for gift voucher\n\
                            >> ").upper()
        num_tickets = int(input(f"How many {ticket_type} tickets do you want: "))
        cost = get_price(ticket_type)

        if confirm_order(ticket_type, num_tickets, cost):
         print("order confirmed")
        else: 
         print("order cancelled")

        ticket_wanted = input("Do you want to order another ticket (Y/N): ").upper()

# main routine
sell_ticket()