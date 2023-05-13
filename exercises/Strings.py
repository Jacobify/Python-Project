first_name = "Rodrigo"
last_name = "Villanueva"

new_account =last_name[:5]
print(new_account)

temp_password = last_name[2:6]

print(temp_password)


def account_generator(first_name,last_name):
  return first_name[:3]+last_name[:3]

first_name = "Julie"
last_name = "Blevins"
print(first_name[:3]+last_name[:3])
new_account = account_generator(first_name,last_name)



first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name,last_name):
  return first_name[len(first_name)-3:]+last_name[len(last_name)-3:]

temp_password = password_generator(first_name,last_name)