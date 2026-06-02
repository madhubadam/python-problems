def vowel_or_consonent(ch):
    if ch.lower() in "aeiou":
        return ('given character is vowel')
    else:
        return ('constonent')
ch=input('enter the character:')
print(vowel_or_consonent(ch))