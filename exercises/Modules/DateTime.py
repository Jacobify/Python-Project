from datetime import datetime

birthday = datetime(1996,9,21,22,21,38)

# print(birthday.year)
# print(birthday.month)
# print(birthday.weekday())

# print(datetime.now())

# print(datetime(2023,1,1)-datetime(2018,1,1))
# print(datetime.now()-datetime(2018,1,1))

parsed_date = datetime.strptime('Sep 21, 1996','%b %d, %Y')

# print(parsed_date.month)

# print(parsed_date.day)

date_string = datetime.strftime(datetime.now(),'%b %d, %Y')
print(date_string)
