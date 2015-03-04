def check_connection(friends,p1,p2):

  for conn in friends:
    pair = conn.split('-')
    other = ''

    if p1 == pair[0] :
      other  = pair[1]
    if p1 == pair[1] :
      other = pair[0]

    if other != '':
      if p2 == other :
        return True
      else :
        return check_connection(friends, other, p2)
  
  return found


print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3")