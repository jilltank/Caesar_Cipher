def encipher(S, n):
  """ S is a string of English + n is a whole number with an absolute value <26
      encrypts the English into a code, shifting the letters 'key' amount of spaces
  """
  if S == '':
    return ''
  elif 'A' <= S[0] <= 'Z':
    return upperCrypt(S[0], n) + encipher(S[1:], n)
  elif 'a' <= S[0] <= 'z':
    return lowerCrypt(S[0], n) + encipher(S[1:], n)
  else:
    return S[0] + encipher(S[1:], n)


def upperCrypt(e, n):
  """e is a single letter + n is a numeric value
    shifts e n number of letters, wrapping around after z
  """
  first = ord(e)
  then = first + n
  if then > 90:
    then = then - 26
  if then < 65:
    then = then + 26
  return chr(then)
  
def lowerCrypt(e, n):
  """ e is a single lowercase letter + n is a numeric value
      shifts e n number of letters, wrapping around after z
  """
  first = ord(e)
  then = first + n
  if then > 122:
    then = then - 26
  if then < 97:
    then = then + 26
  return chr(then)



def decrypt(S, n):
  """
  * This is the way to decrypt the code for when you have the key
  S is an encrypted string + n is the encryption key, whole number with an absolute value < 26
  decrypts S to make it into an English word/phrase
  n is changed from +/- because we are shifting letters back to their original state
  """
  n = n * -1
  if S == '':
    return ''
  elif 'A' <= S[0] <= 'Z':
    return upperCrypt(S[0], n) + encipher(S[1:], n)
  elif 'a' <= S[0] <= 'z':
    return lowerCrypt(S[0], n) + encipher(S[1:], n)
  else:
    return S[0] + decrypt(S[1:], n)

print encipher('May the force be with you.', 25)
print decrypt('Lzx sgd enqbd ad vhsg xnt.', 25)