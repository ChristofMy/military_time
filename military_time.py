import re

times = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety', 0: 'zero'}

def printing_individual(to_word):
    try:
        print(times[int(to_word[0])*10], times[int(to_word[1])], end=' ')
    except KeyError:
        print(f"invalid format")
        exit()
        
def printing(to_word):
    try:
        if int(to_word) < 10:
            print(times[0], end = ' ')
        print(times[int(to_word)], end=' ')
    except KeyError:
        printing_individual(to_word)

def convert_to_military(hours, minutes):
    hours_int = int(hours)
    print("Formatted time: ",end='')
    # Do not consider 0:00AM as that would be incorrect format
    if hours_int == 12 and prefix == "AM":
        print(times[0], end = ' ')
    else:
        printing(hours)

    if int(minutes) == 0:
        print("hundred hours")
    else:
        printing(minutes)
        
        
if __name__ == "__main__":
    time = input("Time to be formatted: ")
    prefix = time[-2:]
    if not (prefix == "AM" or prefix == "PM"):
        print("Incorrect format, needs AM or PM")
        exit()

    
    if re.fullmatch("(\d{1,2}:\d{1,2})", time[:-2]):
        hours, minutes = time[:-2].split(":")
        
    elif re.fullmatch("(\d{2})", time[:-2]):
        hours = time[:-2]
        minutes = "00"
        
    elif re.fullmatch("(\d{1})", time[:-3]):
        hours = time[:1]
        minutes = "00"
    else:
        print("invalid format")
        exit()
        
    if int(hours) > 12:
        print(hours)
        print("Hours need to be at most 12")
        exit()
    
    if int(hours) <= 0:
        print("Hours start at 1")
        exit()

    if int(minutes) >= 60 or int(minutes) < 0:
        print("Minutes must lie between 0 and 59")
        exit()
    
    
    if prefix == "PM":
        hours = str(int(hours) + 12)
        if int(hours) == 24:
            print("Cannot have 24 as an hour")
            exit()
        
    convert_to_military(hours, minutes) 