class Pad():

    def __init__(self, tickets, spaces, current_ticket= False):
        self.ticket = tickets
        self.spaces = spaces
        self.current = current_ticket

    def takeTicket(self):
        
        if self.ticket <= 0:
            print("Sorry, Max Capacity. Come back later.")
            
        else:
            self.ticket += -1
            self.spaces.remove(self.spaces[0])


        
    
    def payForParking(self):
        print(f' available spaces: {self.spaces}')
        if self.ticket == 0:
            print("Sorry, Max Capacity. Come back later.")
        
        else:
            dinero = input(f'That will be 5 dollars upon leaving, please accept: yes/no ')
            if dinero.lower() == 'yes':
                print('Ready to party! Please, take ticket. We are rockin for the next 15 mins')
            else:
                self.ticket += 1
                self.spaces.insert(1,"open")

        
    def leaveGarage(self):
        payment = input(f'gimme da loot: type $5 ')
        if payment == "$5" or "5":
            print("Thank you, come again.")
            self.current_ticket = True
        else:
            payment = input(f'You can leave when payment is made. Please type $5: ')
        if self.current == True:
            print("That was fun come back soon")
        
        self.ticket += 1
         
        self.spaces.insert(1,"open")
        

chicagoLot = Pad(10, [x for x in range(1,11)])
laLot = Pad(20, [y for y in range(1,21)])
def run(lot):
    while True:
        # print(f'This is our available spaces: ')
        # # print(lot.self.spaces)
        user = input("What would you like to do? Park/Leave/neither: ")
        
        if user.lower() == 'park':
            lot.takeTicket()
            lot.payForParking()
            
        elif user.lower() == 'leave':
          lot.leaveGarage()  
        elif user.lower() == 'neither':
            break
        else:
            print("Let me know")
            
    
run(chicagoLot)
