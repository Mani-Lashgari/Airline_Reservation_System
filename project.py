from sys import exit
import pyttsx3
from re import search

engine = pyttsx3.init()
text_to_speak = False
airlines = []
info = []
passengers = {
    "Delta": [],
    "American": [],
    "Turkish": [],
    "Indiana": [],
    "Emirates": [],
    "Lufthansa": [],
    "Air France": [],
    "Qantas": [],
    "Singapore": [],
    "British Airways": []
}


def red_print(text): return "\033[91m{}\033[00m".format(text)


def green_print(text): return "\033[92m{}\033[00m".format(text)


def yellow_print(text): return "\033[93m{}\033[00m".format(text)


def l_purple_print(text): return "\033[94m{}\033[00m".format(text)


def purple_print(text): return "\033[95m{}\033[00m".format(text)


def cyan_print(text): return "\033[96m{}\033[00m".format(text)


def l_gray_print(text): return "\033[97m{}\033[00m".format(text)


def check_route(airline, origin, destination):
    countries = {
        "Emirates": 0,
        "America": 1,
        "Germany": 2,
        "Canada": 3
    }

    if airline == "Delta":
        delta = [[0, 0, 1, 0],
                 [1, 0, 1, 1],
                 [0, 1, 0, 1],
                 [1, 1, 0, 0]]
        if delta[countries[origin]][countries[destination]]:
            return True
    elif airline == "American":
        american = [[0, 1, 0, 0],
                    [1, 0, 1, 0],
                    [0, 1, 0, 1],
                    [0, 0, 1, 0]]
        if american[countries[origin]][countries[destination]]:
            return True
    elif airline == "Turkish":
        turkish = [[0, 1, 0, 1],
                   [1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 0, 1, 0]]
        if turkish[countries[origin]][countries[destination]]:
            return True
    elif airline == "Indiana":
        indiana = [[0, 1, 0, 0],
                   [1, 0, 1, 1],
                   [0, 1, 0, 0],
                   [0, 1, 0, 0]]
        if indiana[countries[origin]][countries[destination]]:
            return True
    elif airline == "Emirates":
        emirates = [[0, 1, 1, 1],
                    [1, 0, 1, 0],
                    [1, 1, 0, 1],
                    [1, 0, 1, 0]]
        if emirates[countries[origin]][countries[destination]]:
            return True
    elif airline == "Lufthansa":
        lufthansa = [[0, 1, 0, 1],
                     [1, 0, 0, 1],
                     [0, 0, 0, 0],
                     [1, 1, 0, 0]]
        if lufthansa[countries[origin]][countries[destination]]:
            return True
    elif airline == "Air France":
        air_france = [[0, 1, 0, 0],
                      [1, 0, 0, 1],
                      [0, 0, 0, 1],
                      [0, 1, 1, 0]]
        if air_france[countries[origin]][countries[destination]]:
            return True
    elif airline == "Qantas":
        qantas = [[0, 1, 0, 0],
                  [1, 0, 0, 0],
                  [0, 0, 0, 1],
                  [0, 0, 1, 0]]
        if qantas[countries[origin]][countries[destination]]:
            return True
    elif airline == "Singapore":
        singapore = [[0, 1, 1, 0],
                     [1, 0, 0, 1],
                     [1, 0, 0, 0],
                     [0, 1, 0, 0]]
        if singapore[countries[origin]][countries[destination]]:
            return True
    elif airline == "British Airways":
        british_airways = [[0, 1, 0, 0],
                           [1, 0, 1, 1],
                           [0, 1, 0, 1],
                           [0, 1, 1, 0]]
        if british_airways[countries[origin]][countries[destination]]:
            return True


def read_file():
    global airlines
    file = open("Airlines.txt", "r")
    file.readline()
    for row in file:
        new_row = row.replace("\n", "").split(",")
        airlines.append(new_row)


def speak(text):
    if text_to_speak:
        engine.setProperty('rate', 250)
        engine.say(text)
        engine.runAndWait()


def find_duplicate_psg(info_, airline_):
    for psg in passengers[airline_]:
        if info_[:-2] == psg[:-2]:
            del psg
            return True
    if len(passengers[airline_]) >= 1:
        del psg
    return False


def menu():
    while True:
        print(yellow_print("Menu:"))
        print(cyan_print("I would be happy to know what I can do for you?"))
        print(cyan_print('''    1. Add passenger                                
    2. Remove passenger                             
    3. Search                                       
    4. Sort                                         
    5. Exit    
    6. Setting                
        '''))
        speak("I would be happy to know what I can do for you? ")
        speak("number one")
        speak("Add passenger")
        speak("number two")
        speak("Remove passenger")
        speak("number three")
        speak("search")
        speak("number four")
        speak("Sort")
        speak("number five")
        speak("Exit")
        speak("number six")
        speak("Setting")
        speak("Pleas enter your choice")
        option_selection = input(yellow_print("Enter your choice: "))
        if option_selection == "1":
            add_psg()
        elif option_selection == "2":
            remove_psg()
        elif option_selection == "3":
            search_()
        elif option_selection == "4":
            sort_()
        elif option_selection == "5":
            while True:
                e = input(yellow_print("Are you sure about your choice?(yes/no): ")).lower()
                if e == "yes":
                    speak("the program has finished.")
                    exit("The program has finished.")
                elif e == "no":
                    break
                else:
                    print(red_print("Your input was incorrect. Please only enter \"yes\" or \"no\"."))
        elif option_selection == "6":
            setting()
        else:
            print(red_print("Please choose from the menu."))


def setting():
    print(cyan_print('''    1. Turn off speak mode\n\t2. Turn on speak mode\n\t3. Back to menu'''))
    setting_option_selection = input(yellow_print("Please enter your choice:"))
    global text_to_speak
    if setting_option_selection == "1":
        text_to_speak = False
        print(red_print("Speak mode is disabled"))
    elif setting_option_selection == "2":
        text_to_speak = True
        speak("Speak mode is enabled")
        print(green_print("Speak mode is enabled"))
    elif setting_option_selection == "3":
        menu()


def add_psg():
    global passengers
    while True:
        speak("In which airline do you want to register the passenger")
        airline = input(yellow_print("In which airline do you want to register the passenger? ")).capitalize()
        if airline not in passengers:
            print(red_print("Please enter correct airline."))
            speak("Pleas enter correct airline name")
        else:
            break

    speak("Sure, please complete the following information about the passenger")
    print(green_print("Sure, please complete the following information about the passenger:"))

    while True:
        full_name = input(yellow_print("Full Name: ")).capitalize()
        if search("^[a-zA-Z]+ [a-zA-Z]+$", full_name):
            info.append(full_name)
            break
        else:
            print(red_print("Invalid Full Name!"))
            speak("You can enter only string")
    while True:
        sex = input(yellow_print("Sex: ")).lower()
        if sex == "male" or sex == "female":
            info.append(sex)
            break
        else:
            print(red_print("Please enter \"male\" or \"female\"."))
            speak("Pleas enter male or female")
    while True:
        age = input(yellow_print("Age: "))
        if age.isdigit():
            info.append(age)
            break
        else:
            print(red_print("You can only enter numbers."))
            speak("you can only enter numbers")

    while True:
        marriage = input(yellow_print("Marriage: ")).lower()
        if marriage == "single" or marriage == "married":
            info.append(marriage)
            break
        else:
            print(red_print("Please enter \"single\" or \"married\"."))
            speak("Pleas enter single or married.")
    while True:
        origin = input(yellow_print("Origin: ")).capitalize()
        if origin.isalpha():
            if origin in ["Emirates", "America", "Germany", "Canada"]:
                info.append(origin)
                break
            else:
                print(red_print("Please enter correct country!\n"
                                "(choose between Emirates, America, Germany and Canada)"))
                speak("choose the country between Emirates or America or Germany or Canada")
        else:
            print(red_print("You can enter only string."))
            speak("You can enter only string")
    while True:
        destination = input(yellow_print("Destination: ")).capitalize()
        if destination.isalpha():
            if destination in ["Emirates", "America", "Germany", "Canada"]:
                info.append(destination)
                break
            else:
                print(red_print("Please enter correct country!\n"
                                "(choose between Emirates, America, Germany and Canada)"))
                speak("Choose the country between Emirates or America or Germany or Canada")
        else:
            print(red_print("You can enter only string."))
            speak("You can enter only string.")
    if check_route(airline, origin, destination) and not find_duplicate_psg(info, airline):
        passengers[airline].append(info)
        print(green_print(f"The passenger \"{full_name}\" has been successfully added to the airline \"{airline}\"."))
        speak(f"The passenger \"{full_name}\" has been successfully added to the airline \"{airline}\".")
    else:
        if not check_route(airline, origin, destination):
            print(red_print(f"In the airline \"{airline}\" there is no route from \"{origin}\" to \"{destination}\"!"))
            speak(f"In the airline \"{airline}\" there is no route from \"{origin}\" to \"{destination}\"!")
        if find_duplicate_psg(info, airline):
            print(red_print("The entered passenger is already in the airline!"))


def find_index(list_, v):
    for i, x in enumerate(list_):
        if v in x:
            return i


def remove_psg():
    speak("In which airline do you want to remove the passenger? ")
    airline = input(yellow_print("In which airline do you want to remove the passenger? ")).capitalize()
    try:
        if not find_index(airlines, airline) is None:
            speak("Sure, please enter the passenger's name: ")
            remove_passenger = input(yellow_print("Sure, please enter the passenger's name: ")).capitalize()
            del(passengers[airline][find_index(passengers[airline], remove_passenger)])
            print(green_print("The passenger") + " \"" + remove_passenger + "\"",
                  green_print("was successfully removed from"), green_print("\"") + airline + green_print("\"."))
            speak("The passenger" + " \"" + remove_passenger + "\"" +
                  "was successfully removed from" + "\"" + airline + "\".")
        else:
            print(red_print("Airline not found!"))
            speak("Airline not found")
    except TypeError:
        print(red_print("Passenger not found!"))
        speak("Passenger not found")


def search_():
    while True:
        speak("In which section do you want to search?")
        print(cyan_print("""In which section do you want to search?
    1. Airlines
    2. Passengers
    3. Back to menu"""))
        search_menu = input(yellow_print("Enter your choice: "))
        if search_menu == "1":
            try:
                speak("Sure, please enter the name of the airline: ")
                airline = input(yellow_print("Sure, please enter the name of the airline: ")).capitalize()
                print(l_purple_print("Safety:"), airlines[find_index(airlines, airline)][1])
                print(l_purple_print("International:"), airlines[find_index(airlines, airline)][2])
                print(l_purple_print("Satisfaction:"), airlines[find_index(airlines, airline)][3])
                print(l_purple_print("Plane:"),  airlines[find_index(airlines, airline)][4])
                print(l_purple_print("Discount:"), airlines[find_index(airlines, airline)][5])
                print(l_purple_print("First-Class:"), airlines[find_index(airlines, airline)][6])
                print(l_purple_print("Age:"), airlines[find_index(airlines, airline)][7])
                print(l_purple_print("Employee:"), airlines[find_index(airlines, airline)][8])
                print(l_purple_print("Number of passengers:"), len(passengers[airline]))
                speak("These are airline information.")
                break
            except TypeError:
                print(red_print("Airline not found!"))
                speak("Airline not found")
        elif search_menu == "2":
            speak("Please enter the name of passenger")
            name_psg = input(yellow_print("Please enter the name of passenger: ")).capitalize()
            flag = False
            for key in passengers:
                for sub_list in passengers[key]:
                    if sub_list[0] == name_psg:
                        speak("These are passenger information")
                        print(l_purple_print("Airline:"), key)
                        print(l_purple_print("Name:"), sub_list[0])
                        print(l_purple_print("Sex:"), sub_list[1])
                        print(l_purple_print("Age:"), sub_list[2])
                        print(l_purple_print("Marriage:"), sub_list[3])
                        print(l_purple_print("Origin:"), sub_list[4])
                        print(l_purple_print("Destination:"), sub_list[5])
                        flag = True
                if flag:
                    break
            if not flag:
                print(red_print("Passenger not found."))
                speak("Passenger not found.")
            break
        elif search_menu == "3":
            menu()
            break
        else:
            print(red_print("Pleas choose from the menu."))
            speak("Pleas choose from the menu")


def list_to_dict(airlines_):
    d = {}
    for airline in airlines_:
        d[airline[0]] = airline[3]
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


def sort_():
    while True:
        speak("In which section do you want to search?")
        print(cyan_print("In which section do you want to search?\n\t1. Airlines\n\t2. Passengers\n\t3. Back to menu"))
        sort_menu = input(yellow_print("Enter your choice: "))
        print()
        if sort_menu == "1":
            counter = 1
            for key, value in list_to_dict(airlines).items():
                print(l_purple_print(str(counter) + ". " + key + ":"), value)
                counter += 1
            break
        elif sort_menu == "2":
            speak("Sure, please enter the name of the airline")
            airline = input(yellow_print("Sure, please enter the name of the airline: ")).capitalize()
            if not find_index(airlines, airline) is None:
                try:
                    for index, name in enumerate(sorted(list(zip(*passengers[airline]))[0])):
                        print(str(index+1)+".", name)
                        print()
                except IndexError:
                    print(red_print("There is no passenger!"))
                    speak("There is no passenger")
                break
            else:
                print(red_print("Airline not found!"))
                speak("Airline not found")
        elif sort_menu == "3":
            menu()
            break
        else:
            print(red_print("Please choose from the menu."))
            speak("Pleas choose from the menu")


try:
    read_file()
    menu()
except KeyboardInterrupt:
    speak("Your program has finished")
    exit("\n\nYour program has finished!")
except RuntimeError:
    exit("\n\nYour program has finished!")
