dictionary={"India":"0091", "Australia":"0025", "nepal":"00977"}
print("counrty code for india.")
print(dictionary.get("India","not found"))
print("country code for japan.")
print(dictionary.get("japan","not found"))
dictionary["mycountry"]="0091"
print(dictionary)
result={}
for key,value in dictionary.items():
    if value not in result.values():
        result[key]=value
print(result)