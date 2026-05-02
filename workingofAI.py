import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.CYAN}  Welcome to sentiment spy! {Style.RESET_ALL}")
user_name= input(f"{Fore.MAGENTA} Please enter your name:, user_input:")
if not user_name:
    user_name= "Mistery Agent"
print(f"\n{Fore.CYAN}Hello agent! {user_name}")
print(f"Type your sentence and i wil analyze your sentence with the TextBlob and I will give you the sentence")
print(f"Type{Fore.YELLOW} reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}")
f"or {Fore.YELLOW}exit{Fore.CYAN}to quit.\n"
user_input= input(f"{Fore.GREEN}>>").strip()

polarity= TextBlob(user_input).sentiment.polarity
if polarity > 0.25:
    sentiment_type= "positive"
    color= Fore.GREEN
    emoji="😊"
elif polarity< -0.25:
    sentiment_type= "negative"
    color= Fore.RED
    emoji="😒"
else:
    sentiment_type="Neutral"
    color= Fore.YELLOW
    emoji="👍"

print(f"{color}{emoji} {sentiment_type} sentiment detected !"
f"polarity:{polarity:.2f}")