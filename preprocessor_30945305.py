"""

Name - Gayatri Aniruddha
Student ID - 30945305
Start Date - 07/10/2019
Last Modified Date - 18/10/2019

This program reads an input file using the method read_text method.
It then performs "clean" operation on it's content using the clean method.
While cleaning, it removes anything which is not a letter, alphabet or a number from the text.

Have imported codecs for opening the file which is in UTF-encoding.

"""

import codecs

class Preprocessor:

    # Constructor for creating instances of this class
    def __init__(self):
        # string called book_content which will hold the book's text
        self.book_content = ""

    # This method display's the content of book_content
    def __str__(self):
        return str(self.book_content)

    # This method removes undesirable characters present in book_content
    def clean(self):

        # Checks if the book_content has text
        if len(self.book_content)!= 0:

            # Creating an empty string for the clean text
            book_content_2 = " "

            # This loop checks if the characters are either a letter, number or whitespace
            # And if yes, copies the text character by character into book_content_2
            for item in self.book_content:
                if item == '_' or item == '-':
                    item = ' '
                    book_content_2 = book_content_2 + item
                elif str(item).isalnum() or item == " ":
                    book_content_2 = book_content_2 + item

            # Adding the text back to the book content
            self.book_content = book_content_2

            # Since, book_content had text, this method returns None
            return None

        # If no text present in book_content, the function returns 1
        else:
            return 1

    # This function reads the content of the file into book_content
    # Assumption - text is in UTF-8 encoding
    def read_text(self, text_name):

        # Opening the file
        file_pointer = codecs.open(text_name,'r',encoding='UTF-8')

        # Reading it's content into book_content
        self.book_content = file_pointer.read().lower().replace("\n"," ")

        # Closing the file
        file_pointer.close()







