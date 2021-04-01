who_cares = int(input())
while who_cares > 0:
    date = input().split()
    day = int(date[0])
    month = date[1]
    if month == 'Dec':
        if day < 22:
            print("Sagittarius")
        else:
            print("Capricorn")
    elif month == 'Nov':
        if day < 23:
            print("Scorpio")
        else:
            print("Sagittarius")
    elif month == 'Oct':
        if day < 23:
            print("Libra")
        else:
            print("Scorpio")
    elif month == 'Sep':
        if day < 22:
            print("Virgo")
        else:
            print("Libra")
    elif month == 'Aug':
        if day < 23:
            print("Leo")
        else:
            print("Virgo")
    elif month == 'Jul':
        if day < 23:
            print("Cancer")
        else:
            print("Leo")
    elif month == 'Jun':
        if day < 22:
            print("Gemini")
        else:
            print("Cancer")
    elif month == 'May':
        if day < 21:
            print("Taurus")
        else:
            print("Gemini")
    elif month == 'Apr':
        if day < 21:
            print("Aries")
        else:
            print("Taurus")
    elif month == 'Mar':
        if day < 21:
            print("Pisces")
        else:
            print("Aries")
    elif month == 'Feb':
        if day < 20:
            print("Aquarius")
        else:
            print("Pisces")
    elif month == 'Jan':
        if day < 21:
            print("Capricorn")
        else:
            print("Aquarius")
    else:
        print("Please enter a valid date!")

    who_cares = who_cares - 1