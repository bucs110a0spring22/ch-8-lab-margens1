class StringUtility:


  def __init__(self, string):
    '''
    creates string of class self
    args: self and string
    return: nothing
    '''
    self.string = string
  
  def __str__(self):
    '''
    returns self.string
    args: self
    return: returns self.string
    '''
    return self.string
  
  
  def vowels(self):
    '''
    variable accumulates everytime vowel is found in word
    args: self
    return: returns the number of vowels in a word
    '''
    count = 0
    for i in self.string:
      if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count += 1
    if count >= 5:
      output = "many"
    else:
      output = str(count)
    return output
        
  def bothEnds(self):
     '''
    finds and joins the last and first two letters of the word
    args: self
    return: returns the last and first two letters of the word
    '''
     if len(self.string)<=2:
       return""
     else:
       return self.string[0:2]+self.string[-2:]

  def fixStart(self):
    '''
    takes the first letter of a word and returns a string with a stars at the occurance of that word again
    args: self
    return: a string with starts in where first letter is repeated
    '''
    if len(self.string)<=1:
      return""
    else:
      return self.string[0]+self.string[1:].replace(self.string[0],'*')

  def asciiSum(self):
   '''
   sums the ascii values of the string
   args: self
   return: the sum of the ascii values of the string
   '''
   ascii_sum=0
   for i in self.string:
     ascii_sum+=(ord(i))
   return ascii_sum
    

  def cipher(self):
    '''
    goes through each letter of the string shifts the letter value 3 down the alphabet
    args: self
    return: returns an encrypted string
    '''
    encryption = ""
    shift = len(self.string)
    for character in self.string:
      if character.isupper():
        character_index = ord(character) - ord('A')
        character_shifted = (character_index + shift) % 26 + ord('A')
        character_new = chr(character_shifted)
        encryption += character_new
      elif character.islower():
        character_index = ord(character) - ord('a')
        character_shifted = (character_index + shift) % 26 + ord('a')
        character_new = chr(character_shifted)
        encryption += str(character_new)
      else:
        encryption += character
    return encryption
