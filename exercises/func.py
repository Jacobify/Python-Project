
def crypted (sentnece):
  encryption = ""
  for letter in sentnece:
    if letter in "Aa":
      encryption =encryption+"1"
    elif letter in "Bb":
        encryption =encryption+"2"
    elif letter in "Cc":
        encryption =encryption+"3"
    elif letter in "Dd":
        encryption =encryption+"4"
    elif letter in "Ee":
        encryption =encryption+"5"
    elif letter in "Ff":
        encryption =encryption+"6"
    elif letter in "Gg":
        encryption =encryption+"7"
  return encryption


print(crypted("gsaadbskjdbaskdbagb"))

