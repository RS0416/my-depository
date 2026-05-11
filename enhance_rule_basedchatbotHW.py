import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
"beaches": ["Bali", "Maldives", "Phuket"],
"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
"cities": ["Tokyo", "Paris", "New York"]
}
jokes= {"Why don't programmers like nature? Too many bugs!",
"Why did the computer go to the doctor? Because it had a virus!",
"Why do travelers always feel warm? Because of all their hot spots!"   
}
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "Travelbot: Beaches, Mountains, or cities?")
    preference= input(Fore.YELLOW +"You:")
    preference= normalize_input(preference)
    if preference in destinations:
        suggestion= random.choice(destinations[preference])
        print(Fore.GREEN + f"Travelbot: How about{suggestion}?")
        print(Fore.CYAN + f"Travelbot: Do you like it? (yes/no)")
        answer= input(Fore.YELLOW + "You: ").lower()
        if answer=="yes":
            print(Fore.GREEN + f"Travelbot: Awsome, Enjoy!{suggestion}!")
        elif answer=="no":
            print(Fore.RED + f"Travelbot: Lets try another")
            recommend()
        else:
            print(Fore.RED + f"Travelbot: Sorry! I don't have that type of destination.")
            recommend()
    def packing_tips():
        print(Fore.CYAN + f"Travelbot:Where to?")
        location= normalize_input(Fore.YELLOW + "You: ")
        print(Fore.GREEN + f"Travelbot: Packing tips for {days} days in {location}")
        print(Fore.GREEN + "-- Pack versatile clothes .")
        print(Fore.GREEN + "--Bring chargers or adapters.")
        print(Fore.GREEN + "--Check for the weather forcast.")
    def tell_joke():
        print(Fore.YELLOW + f"Travelbot: {random.choice(jokes)}")
    def show_help():
        print(Fore.MAGENTA + "\nI can")
        print(Fore.GREEN + "-- Suggest travelspots (say recommendations)")
        print(Fore.GREEN + "-- Offer packing tips (say 'packing')")
        print(Fore.GREEN + "--Tell a joke (say 'joke')")
        print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")
    
    def chat():
        print(Fore.CYAN + "Hello, I'm a Travelbot.")
        name= input(Fore.CYAN + "Your name?")
        print(Fore.GREEN + f"Nice to meet you, {name}!")

        show_help()

        while True:
            user_input= input(Fore.YELLOW + f"{name}:")
            user_input= normalize_input(user_input)

            if "recommend" in user_input or "suggest" in user_input:
                recommend()
            elif "pack" in user_input or "packing " in user_input:
                packing_tips()
            elif "joke" in user_input or "funny" in user_input:
                tell_joke()
            elif "help" in user_input:
                show_help()
            elif "exit" in user_input or "bye" in user_input:
                print(Fore.CYAN + "Travelbot: Good travel, Safe journey")
                break
            else:
                print(Fore.RED + "Travelbot: Could you rephrase.")
            
            if __name__ == "__main__":
                chat()