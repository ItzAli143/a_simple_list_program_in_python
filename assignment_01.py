li = ["Islamabad", "Lahore", "Multan", "Gujranwala", "Rawalpindi"]

while True:
    a = input("Enter the name of your city (or type 'exit' to stop): ")
    if a.lower() == 'exit':
        break
    if a in li:
        print("Your city is included in the list of most cleaned cities.")
    else:
        print("Your city is not a part of cleaned cities of Pakistan.")
