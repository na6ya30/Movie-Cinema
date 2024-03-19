"""Movie theatre ticketing system - v5
update totals
"""
def confirm_order(ticket, number, cost):
    """confirm ticket order - component 4"""
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nYou have ordered {number} {ticket} ticket(s) at a cost of %{cost * number:.2f}\n'Y' or 'N'").upper()
    if confirm == "Y":
        return True
    else:
        return  False

def get_price(type_):
    """calculate price - component 3"""

    prices = [["A", 12.5,],["C", 7],["S", 9],["G", 0]]
    for price in prices: 
        if price[0] == type_: 
            return price[1]

def sell_ticket():
    print("************ FanFare Movies - ticketing system *************")

    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_sales = 0
    
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
        cost = get_price(ticket_type)

    if confirm_order(ticket_type, num_tickets, cost):
        print("order confirmed")
        #component 5 - update totals
        total_sales += cost
        tickets_sold += num_tickets
        if ticket_type == "A":
            adult_tickets += num_tickets
        elif ticket_type == "S":
            student_tickets += num_tickets
        elif ticket_type == "C":
            child_tickets += num_tickets
        else:
            print("order cancelled")
            
    ticket_wanted = input("Do you want to order another ticket (Y/N): ").upper()


    print(f"\n you have ordered {num_tickets} {ticket_type} tickets(s) at a cost of $ {cost * num_tickets:.2f}!")
# main routine
sell_ticket()