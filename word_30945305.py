"""

Name - Gayatri Aniruddha
Student ID - 30945305
Start Date - 07/10/2019
Last Modified Date - 18/10/2019

This task accepts a clean text in the method - analyse_words.
It then calculates the occurrences for each of the words in the text.
This value is updated in the instance variable - word_counts which is a dictionary.
It then, calculates the frequency of each of the word in the method - get_word_frequency.
It stores the frequencies of each word in a dictionary and returns this dictionary when the get_word_frequency method is called.

"""

class WordAnalyser:

    # This constructor defines an instance variable word_counts which is a dictionary
    def __init__(self):
        self.word_counts = dict()

    # This method displays the occurrences of each word
    # This returns a formatted string
    def __str__(self):
        return str(self.word_counts)

    # This method accepts the cleaned book text
    # It then counts the occurrences for each of the words
    # The word count is updated in the instance variable - word_counts
    def analyse_words(self, book_text):

        for word in book_text.split():

            # Checks if the word is present in the keys of word_count dictionary
            if word in self.word_counts.keys():
                # If word exists, increment the value of the word
                self.word_counts[word] += 1

            else:
                # If word does not exist, create a new kay value
                self.word_counts[word] = 1

    # This method returns the frequency of the words in word_counts
    def get_word_frequency(self):

        # Dictionary to store the frequencies of each word
        word_freq_dict = dict()

        # Calculates the total number of items
        total = 0
        for item in self.word_counts.keys():
            total += self.word_counts[item]

        # This calculates the frequency of every word
        for item in self.word_counts.keys():
            freq = (self.word_counts[item])/total

            word_freq_dict[item] = freq

        # Returns a dictionary which has frequency of the words
        return word_freq_dict


