from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None  # hash table for stop words
        self.concordance_table = None  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            file = open(filename, 'r')
            file.close()
        except FileNotFoundError as error:
            raise FileNotFoundError
        else:
            self.stop_table = HashTable(191)
            file = open(filename, 'r')
            for line in file:
                self.stop_table.insert(line.strip())
            file.close()

    def load_concordance_table(self, filename):
        ''' Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError'''
        try:
            file = open(filename, 'r')
            file.close()
        except FileNotFoundError as error:
            raise FileNotFoundError
        else:
            self.concordance_table = HashTable(191)

            words = set()
            num = 0
            file = open(filename, 'r')

            for line in file:  # one line at a time
                num += 1

                line = line.replace("'", '')  # remove all occurrences of the apostrophe char

                for p in string.punctuation:  # convert all punctuation to spaces
                    line = line.replace(p, ' ')

                line = line.lower()
                x = line.split()  # split into tokens
                x = set(x)  # get rid of duplicates within line
                for tok in x:
                    if tok.isalpha() and not self.stop_table.in_table(tok):
                        words.add(tok)
                        if not self.concordance_table.in_table(tok):
                            self.concordance_table.insert(tok, [num])
                        else:
                            val = self.concordance_table.get_value(tok)
                            val.append(num)
                            self.concordance_table.insert(tok, val)

            file.close()

    def write_concordance(self, filename):
        ''' Write the concordance entries to the output file(filename)
        See sample output files for format.'''
        all_keys = self.concordance_table.get_all_keys()
        all_keys.sort() # create list of sorted keys
        file_out = open(filename, 'w')
        for k in all_keys:
            file_out.write(k + ':')
            lines = self.concordance_table.get_value(k) # get line numbers
            for n in lines:
                file_out.write(' ' + str(n))
            file_out.write('\n') # move on to next key
        file_out.close()