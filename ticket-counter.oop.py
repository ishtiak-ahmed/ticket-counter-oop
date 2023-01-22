# 1 make class
class Star_Cinema:
    '''Class with a class attribute and staticmethod'''
    hall_list = []
    def __init__(self) -> None:
        pass
    @staticmethod
    def entry_hall(hall):
        Star_Cinema.hall_list.append(hall)

# 2 make hall class and create object
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        # 9, private protected attribute
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)
    # 3 entry_show()
    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        sits_list = []
        for i in range(self.__rows):
            row = [];
            for j in range(self.__cols):
                row.append(False)
            sits_list.append(row)
        self.__seats[id] = sits_list

    # 4 book_seats()
    def book_seats(self, name, phone, id, sits):
        # 8.a. invalid show id
        is_successful = True
        if id not in self.__seats:
            print(f'{"-" * 72}')
            print("Show id is invalid")
            print(f'{"-" * 72}')
            is_successful = False
            return
        for sit in sits:
            # 8.b. invalid sit number
            row, col = [ord(sit[0]) - ord("A"), int(sit[1:])]
            if row > self.__rows or col > self.__cols:
                print(f'{"-" * 72}')
                print("Invalid sit number", sit)
                print(f'{"-" * 72}')
                is_successful = False
                break
            current = self.__seats[id][row][col]
            if(current == False):
                self.__seats[id][row][col] = True
            else:
                # 8.c. already booked
                print(f'{"-" * 72}')
                print(f"Sit {sit} is already booked")
                print(f'{"-" * 72}')
                is_successful = False
                break
        if is_successful:
            show = [tup for tup in self.__show_list if tup[0] == id][0]
            print("\n###  TICKETS BOOKED SUCCESSFULLY!  ###")
            print(f'{"-" * 72}')
            print(f'NAME: {name} ')
            print(f'PHONE: {phone} ')
            print(f'MOVIE: {show[1]} ', end ="\t")
            print(f'TIME: {show[2]}')
            print("TICKETS:", end=" ")
            for ticket in sits:
                print(ticket, end=" ")
            print("\nHALL: ", self.__hall_no)
            print(f'{"-" * 72}\n')

    # 5 view_show_list()
    def view_show_list(self):
        print(f'{"-" * 72}')
        print(f"{' ' * 15} Available shows in '{self.__hall_no}'")
        print(f'{"-" * 72}')
        for show in self.__show_list:
            print(f'Show id: {show[0]}, Movie: {show[1]}, Time: {show[2]}')
        print(f'{"-" * 72}\n')

    # 6 view_available_seats()
    def view_available_seats(self, id):
        if id in self.__seats:
            print(f'{"-" * 52}')
            show = [tup for tup in self.__show_list if tup[0] == id][0]
            print(f"MOVIE NAME: {show[1]}", end="\t")
            print(f"TIME: {show[2]}")
            print("X is already booked")
            print(f'{"-" * 52}')
            for i, row in enumerate(self.__seats[id]):
                for idx, sit in enumerate(row):
                    if sit == False:
                        print(f'{chr(ord("A") + i)}{idx}', end="\t ")
                    else:
                        print("X", end="\t ")
                print()
            print(f'{"-" * 52}')
        else:
            print(f'{"-" * 72}')
            print("Invalid show id")
            print(f'{"-" * 72}\n')

hall1 = Hall(12, 6, "Star Joypurhat")

hall1.entry_show('Noon', 'Harry Potter And The Sorcessor Stone', '1:00PM-4:00pm')
hall1.entry_show('Afternoon', 'Harry Potter And The Chamber Of Secret', '4:00PM-7:00pm')
hall1.entry_show('Evening', 'How to train your dragon', '7:00PM-10:00pm')
hall1.entry_show('Night', 'Around the world in 80 days', '10:00PM-1:00am')

# 7 Replica System
while True:
    print("1. View running show list \n2. View available seats in a show\n3. Book tickets in show\n4. EXIT\n")
    choice = input("Choose an option: ")
    if choice == '1':
        print()
        hall1.view_show_list()
    elif choice == '2':
        print()
        id = input("Enter show id to view available sits: ")
        print()
        hall1.view_available_seats(id)
        print()
    elif choice == '3':
        print()
        name = input("Enter your name: ")
        phone = input("Enter phone number: ")
        show_id = input("Enter show id: ")
        sitCount = int(input("Number of tickets: "))
        while sitCount < 1:
            sitCount = int(input("Please enter valid number:"))
        sits = []
        for i in range(sitCount):
            sitNumber = input("Enter sit number: ")
            sits.append(sitNumber)
        hall1.book_seats(name, phone, show_id, sits)
    elif choice == '4':
        break
    else:
        print("Invalid choice\n")
