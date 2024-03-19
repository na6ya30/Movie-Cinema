"""Movie theatre ticketing system - v3
calculate ticket price
"""
def get_price(type_):
    prices = [["A", 12.5,], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices: 
        if price[0] == type_: 
            return price[1]
def sell_ticket():
    """Component 1 of project: welcome screen and set up variables"""
    
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
                            \t'C' for child, or\n\
                            \t'G' for gift voucher\n\
                            >> ").upper()
        num_tickets = int(input(f"How many {ticket_type} tickets do you want: "))
        cost = get_price(ticket_type)

        print(f"\nYou have ordered {num_tickets} {ticket_type} tickets(s) at a cost of ${cost * num_tickets:.2f!}")
        
        ticket_wanted = input("Do you want to order another ticket (Y/N): ").upper()
    
# main routine
sell_ticket()