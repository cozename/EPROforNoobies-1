days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

Day = int(input("Day: "))
Month = int(input("Month: "))


if Month < 1 or Month > 12:
    print("nonsensical date!")
elif Day < 1 or Day > days_per_month[Month-1]:
    print("nonsensical date!")
else:
    print("issa date!")