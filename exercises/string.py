password = "theycallme\"crazy\"91"

def get_length(string1):
  length = 0
  for letter in string1:
    length = length + 1
  return length



print(get_length("test"))



def letter_check(word,letter):
  for character in word:
    if character == letter:
      return True
  return False

print(letter_check("strawberry", "a"))


def contains(big_string,little_string):
  if little_string in big_string:
    return True
  else:
    return False

print(contains("watermelon", "melon"))

def common_letters(string_one,string_two):
  common = []
  for letter in string_one:
    if letter in string_two and not letter in common:
      common.append(letter)
  return common

print(common_letters("hello", "apple"))

def username_generator(first_name,last_name):
  if len(first_name) < 3:
    return first_name+last_name[:4]
  elif len(last_name) <4:
    return first_name[:3]+last_name
  elif len(first_name) < 3 and len(last_name) <4:
    return first_name+last_name
  else:
    return first_name[:3]+last_name[:4]


print(username_generator("Abe","Simpson"))

def password_generator(username):
  password = ''
  print(username[0])
  for index in range(len(username)):
    print(index)
    password = password + username[index-1]
  return password

print(password_generator("AbeSimp"))