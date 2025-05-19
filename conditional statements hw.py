mylevel=int(input("my level:"))
brolevel=int(input("brother's level:"))
momlevel=int(input("mom's level:"))
if momlevel>mylevel:
    print("mom's level is greater than me.")
else:
    print("mom's level is smaller than me.")
if brolevel>momlevel:
    print("my bro's level is greater than my mom.")
else:
    print("my mom's level is greater than my bro.")