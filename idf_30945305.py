"""

Name - Gayatri Aniruddha
Student ID - 30945305
Start Date - 09/10/2019
Last Modified Date - 18/10/2019

This task makes use of Pandas Dataframe.
Here, we make an empty Dataframe called data which will store the word frequencies.
In the load_frequency method, it loads the word frequencies for every file, in the dataframe.
Then, in the get_IDF method, we calculate the IDF value for a given tern in the documents provided.
Thus, higher the IDF value of the term, the more important the term is.
Also, have imported pandas and math.
pandas for creating the dataframe
and math for calculating idf value.

"""

import pandas as pd
import math

class IDFAnalyser:

    # This constructor creates an instance variable called data which is a Dataframe
    def __init__(self):
        self.data = pd.DataFrame()

    # This method loads frequency of the cleaned text into data
    # book_title corresponds to the text the frequency was generated from
    # book_frequency is the dictionary generated in task 2,
    # which has frequencies of every word
    def load_frequency(self, book_frequency, book_title):

        # One row of words and frequencies, along with book title
        df = pd.DataFrame(book_frequency,index=[book_title])

        # Appending this into self.data
        self.data = self.data.append(df, sort=True)

        # Returns the contents of the dataframe
        return self.data

    # Calculates the IDF for the term provided and the documents loaded into data
    def get_IDF(self, term):

        # D - Total number of documents
        D = len(self.data.index)

        # N - Number of documents containing the term
        N = self.data[str(term)].count()

        # Calculating IDF based on the formula
        idfvalue = 1 + math.log(D / (1 + N))

        # Returning the IDF value
        return idfvalue




