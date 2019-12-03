def make_banner(text):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # ordered list of the letters of the alphabet, with a corresponding index
    file = open("banner_letters.txt", "r")
    # opens the txt file in reading mode
    content = file.readlines()
    # returns a list of the lines (in the form of strings ending with \n)
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""
    line_5 = ""
    line_6 = ""
    line_7 = ""
    # defines a string for each of the 7 lines of the banner
    for letter in text.lower(): # lowercase letters only
        if letter not in alphabet: # anything not in a, ..., z
            raise ValueError("All characters in text must be alphabetic.")
        else: # if all letters in text are valid
            order = alphabet.index(letter)
            # returns the index at which the letter is found in alphabet
            start_index = order * 7
            # first index for the lines in content corresponding to the letter
            line_1 += content[start_index].rstrip("\n") + " "
            line_2 += content[start_index + 1].rstrip("\n") + " "
            line_3 += content[start_index + 2].rstrip("\n") + " "
            line_4 += content[start_index + 3].rstrip("\n") + " "
            line_5 += content[start_index + 4].rstrip("\n") + " "
            line_6 += content[start_index + 5].rstrip("\n") + " "
            line_7 += content[start_index + 6].rstrip("\n") + " "
            # strips the \n on the right of each line in content
            # adds a space before the next line for the next letter is added
            # returns 7 strings representing the 7 lines of the banner
    file.close() # closes the file
    
    banner = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + "\n" + line_5 + "\n" + line_6 + "\n" + line_7
    # adds each string line_1, ..., line_7 with lines between them
    # banner is one single string concatenated from those strings
    return banner