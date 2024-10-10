# In the code below, fill in the blanks (____). IN the blanks you cannot use any
# ";" symbols. You also cannot use comprehensions or any other syntax that we
# have not learned in the first 9 lectures.


words = sorted(set(open("GE.txt", "r", encoding="utf-8").read().split()))
 # This line reads GE.txt, and creates a sorted list of all of the
             # unique words in this file (both English and German). 
             # There's an entry for ":" in words (ie: >>> assert ":" in words).
             # Hypenated words are words (ie: >>> assert "cross-talk" in words).
             # Hint: The file data type has a method called "read".
             # Hint: The string data type has useful methods.

#token = {word: i for i, word in enumerate(words)} 
token = dict(zip(words, range(len(words)))) # This creates a dictionary, where the keys are the words, and
             # and the values are the numbers from 0 to 88527.

ge, eg = {}, {}
             # This line simultaneously creates two empty dictionaries named
             # "ge" and "eg". After running the code below, "ge" will be a
             # German-to-English dictionary, and "eg" will be English-to-German.

f=open("GE.txt")
while True:
   l=tuple(map(lambda x: token[x], f.readline().split())) # This line creates a token list for each line of the input,
                   # one-by-one. So, for example, the first time this line runs
                   # the line "aal : eel" will be read, and you will get
                   # assert l = (3, 0, 20294). And that result is due to this:
                   # assert (3,0,20294)==(token['aal'],token[':'],token['eel'])
                   # Hint: lambda
   if l == (): break #Catches the case where the file has been fully read.
   ge[l[ : l.index(0)]] = l[l.index(0)+1 : ] # ge uses the tuple of german tokens as the key + the tuple 
   eg[l[l.index(0)+1 : ]] = l[ : l.index(0)] # of english tokens as the value. eq is the opposite.
                   # Note: These are tuples because GE.txt does contain phrases.
                   # Note: A value of 0 (ie, token[":"]==0) is the delimiter.

def translate(word,ToEnglish=False):
   """Takes a word in English or German and translates it.
       Default is English-to-Geman, but flip it by passing in ToEnglish=True."""
   if not ToEnglish and tuple(token[word] for word in word.split()) in eg or ToEnglish and tuple(token[word] for word in word.split()) in ge:
      print("The " + (ToEnglish and "German" or "English") + " word \"" + word + "\" " + 
            (len(tuple(token[word] for word in word.split())) > 1 and str(tuple(token[word] for word in word.split())) or "(" + str(tuple(token[word] for word in word.split())[0])  + ")") +
            " translates to \"" + ''.join(words[key] for key in (ToEnglish and ge[tuple(token[word] for word in word.split())] or eg[tuple(token[word] for word in word.split())])) + "\" " + 
            (ToEnglish and len(ge[tuple(token[word] for word in word.split())]) > 1 and (ToEnglish and ge[tuple(token[word] for word in word.split())] or eg[tuple(token[word] for word in word.split())]) or 
            ("(" + (ToEnglish and str(ge[tuple(token[word] for word in word.split())][0]) or str(eg[tuple(token[word] for word in word.split())][0])) + ")")) + "."
            ) # Translated output must match the provided demo file.
   else:
      print("\"" + word.capitalize() + "\" is not in the " + (ToEnglish and "German" or "English") + " dictionary.")

   #if ToEnglish:
      #print("The German word \"" + word + "\" " + 
            #(str(tuple(token[word] for word in word.split())) if len(tuple(token[word] for word in word.split())) > 1 else "(" + str(tuple(token[word] for word in word.split())[0]) + ")") + 
            #" translates to \"" + ''.join(words[key] for key in ge[tuple(token[word] for word in word.split())]) + "\" " + 
            #(str(ge[tuple(token[word] for word in word.split())]) if len(ge[tuple(token[word] for word in word.split())]) > 1 else ("(" + str(ge[tuple(token[word] for word in word.split())][0]) + ")")) + 
            #"." if tuple(token[word] for word in word.split()) in ge else "\"" + word.capitalize() + "\" is not in the German dictionary.") # Translated output must match the provided demo file.
   #else:
      #print("The English word \"" + word + "\" " + 
            #(str(tuple(token[word] for word in word.split())) if len(tuple(token[word] for word in word.split())) > 1 else "(" + str(tuple(token[word] for word in word.split())[0]) + ")") + 
            #" translates to \"" + ''.join(words[key] for key in eg[tuple(token[word] for word in word.split())]) + "\" " + 
            #(str(ge[tuple(token[word] for word in word.split())]) if len(eg[tuple(token[word] for word in word.split())]) > 1 else ("(" + str(eg[tuple(token[word] for word in word.split())][0]) + ")")) + 
            #"." if tuple(token[word] for word in word.split()) in eg else "\"" + word.capitalize() + "\" is not in the English dictionary.") # Error message must match the provided demo file.


if __name__ == "__main__":  # This test to see if this is not being run via importing.
           # That is to say: that it was run by: python3 GEdictionary.py
           # Hint: __main__.
   translate("eel")
   translate("aal")
   translate("aal",ToEnglish=True)
   translate("eel",ToEnglish=True)