"""

Name - Gayatri Aniruddha
Student ID - 30945305
Start Date - 11/10/2019
Last Modified Date - 18/10/2019

This task takes the following inputs -
1) term - string value whose IDF we want to calculate
2) documents - dataframe, which has all the word frequencies stored.
Then, it calculates the IDF and the maximum TF value to get the maximum TF IDF value.
It then returs the document which has the maximum TF - IDF value.
Thus, we know the most suitable document for a given term.

Have imported math for calculating the idf value.

"""

import math

# This method returns the document with the highest TF -IDF value
# term - is a string whose TF-IDF value we want to calculate
# documents - idf object i.e a dataframe
def choice(term,documents):

    # Calculating idf value of the term

    # D - Total number of documents
    D = len(documents.index)

    # N - Number of documents containing the term
    N = documents[str(term)].count()

    idf_value = 1+math.log(D / (1 + N))
    print(idf_value)

    # Calculating tf value
    tf_value = documents[term].max()

    # Calculating tf idf value
    tf_idf = (idf_value * tf_value)

    # To determine the document with the largest tf_idf value
    suitable_book_1 = documents[term].idxmax()
    suitable_book_2 = str(suitable_book_1) + ".txt"

    # This returns the name of the document which has the highest TF-IDF score
    return suitable_book_2


