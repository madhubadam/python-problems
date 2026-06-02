#def alphabet_checking(ch):
 #   if ch.isalpha():
  #      return 'is a alphabet'
   # else:
      #  return 'not a alphabet'
#ch='7'
#print(alphabet_checking(ch))



#method 2
def alphabet_checking(ch):
    if 65<=ord(ch)>=90 or 97<=ord(ch)>=122:
        return 'is a alphabet'
    else:
        return 'not a alphabet'
ch='4'
print(alphabet_checking(ch))