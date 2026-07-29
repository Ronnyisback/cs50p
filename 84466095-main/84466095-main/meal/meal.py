def main():
    time=input("What time is it?")
    final_time = convert(time)
    if 7<=final_time<=8:
        print("breakfast time")
    elif 12<=final_time<=13:
        print("lunch time")
    elif 18<=final_time<=19:
        print("dinner time")


def convert(time):
    hours, minutes=time.split(":")
    hours=float(hours)
    minutes=float(minutes)
    total_time=hours+(minutes/60)
    return total_time
if __name__ == "__main__":
    main()
