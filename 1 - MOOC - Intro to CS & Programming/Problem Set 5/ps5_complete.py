import string

# Initialize valid words.

WORDLIST_FILENAME = 'words.txt'

# This file contains three classes in the following order:

# 1) - Message
# 2) - Plaintext Message
# 3) - Ciphertext Message

# The file also tests to see if functions are operational, and then decodes the story file in this directory

# ------------------------------------------------------------------------------------------------------------------

# The Message class contains methods that could be used to apply a cipher to a string, either to encrypt
# or to decrypt a message (since for Caesar codes this is the same action).

class Message(object):

    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text


    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        # Create an empty dictionary
        shifted_dict = {}

        # Create four lists of letters - non shifted and shifted for upper and lower case
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        shifted_lowercase = lowercase[shift:] + lowercase[:shift]
        shifted_uppercase = uppercase[shift:] + uppercase[:shift]

        # Add elements to the shifted_dict that map the two sets together
        for i in range(26):
            shifted_dict[lowercase[i]] = shifted_lowercase[i]
            shifted_dict[uppercase[i]] = shifted_uppercase[i]
        return shifted_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        # Create a copy of the input message
        message = self.get_message_text()

        # Intitialize final string and custom dictionaries

        final = ''
        custom_dict = self.build_shift_dict(shift)

        # For each letter, find the associated letter in the custom dictionary and append it to the final string
        for n in message:
            if n in custom_dict:
                n = custom_dict[n]
            final += n

        return final

# ------------------------------------------------------------------------------------------------------

# PlaintextMessage is a subclass of Message and has methods to encode a string using a specified shift value.
# This class will always create an encoded version of the message, and will have methods for changing the encoding.


class PlaintextMessage(Message):


    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)



    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''

        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.message_text_encrypted



    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        # Defines object shift variable
        self.shift = shift

        # Creates encrypted dictionary based on shift value
        self.encrypting_dict = self.build_shift_dict(self.shift)

        # Creates the encrypted message
        self.message_text_encrypted = self.apply_shift(self.shift)
        return

# -------------------------------------------------------------------------------------------------------------

# Subclass of message to decode a string based upon the classic Caesar Cypher

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        # Initializes setup variables

        final = ()
        current_max = 0

        # For all possible shifts, do the following:
        for s in range(26):

            # Set a new variable to keep track of the max in the loop iteration
            round_max = 0

            # Create a new variable x, which is the current output with the ith shift
            x = self.apply_shift(26-s)

            # Create a variable test which is a list containing all of the words appropritely seperated
            test = x.split()

            # For each word do the following:
            for i in range(len(test)):

                # If the word is valid, increase the round_max variable indicating that the current shift applied
                # has another correct word

                if is_word(self.valid_words,test[i]) == True:
                    round_max += 1

            # Check to see if the tested shift is the best iteration so far. If it is, set the current_max
            # and create a final string

            if round_max > current_max:
                    final = (26 - s,x)
                    current_max = round_max
                    if s == 26:
                        final = (s,x)

        # Return the final message with the "at least" best version, scored upon number of correct words

        return final


# Helper functions shown below

# -------------------------------------------------------------------------


def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


def decrypt_story():
    story_encrypted = CiphertextMessage(get_story_string())

    return story_encrypted.decrypt_message()

# ----------------------------------------------------------------------------------------------------------

# Example test case (PlaintextMessage)


plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
print()


# Example test case (CiphertextMessage)


ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
print()

# Example Decrypted Story
print(decrypt_story())