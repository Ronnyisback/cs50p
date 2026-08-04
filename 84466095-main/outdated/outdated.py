months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    date=input("Date: ").strip()
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month, day, year = int(month), int(day), int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
        except ValueError:
            pass
    elif "," in date:
        try:
            date = date.replace(",", "")
            month_name, day, year = date.split()
            day, year = int(day), int(year)
            if month_name in months:
                month = months.index(month_name) + 1
                if 1<=month<=12 and 1 <=day<=31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
        except ValueError:
            pass
