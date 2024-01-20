def isBeautiful(inputString, char='a') -> bool:
  if char == 'z':
    return True

  val_cnt = inputString.count(char)
  next_value = chr(ord(char) + 1)
  next_cnt = inputString.count(next_value)

  if val_cnt < next_cnt:
    return False
  else:
    return isBeautiful(inputString, char=next_value)
