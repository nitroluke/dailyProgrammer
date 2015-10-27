def disemvowler(sentence):
    print (sentence)
    voweless = [char for char in sentence.lower() if char not in ["a", "e", "i", "o", "u", " "]]
    print ("".join(voweless))

disemvowler("This is a sentence to remove the vowels and spaces")