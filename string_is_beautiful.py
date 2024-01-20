import string
def isBeautiful(inputString: str)-> bool:
  dict = {}

  for letter in sorted(inputString.lower()):
    # print(letter)
    if letter not in dict:
      dict[letter] = 1
    else:
      dict[letter] += 1

  alphabet = list(string.ascii_lowercase)

  prv_cnt = None

  for letter in alphabet:
    val_cnt = dict.get(letter, 0)

    if prv_cnt is None:
      prv_cnt = val_cnt
    else:
      if val_cnt > prv_cnt:
        return False

      prv_cnt = val_cnt

  return True
