import os
from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the frequency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
        
    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return type(other) == HuffmanNode and self.char == other.char and self.freq == other.freq and self.left == other.left and self.right == other.right

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            if self.char < other.char:
                return True
        return False

def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    lst = 256 * [0]
    lst_string = ''
    file = open(filename, 'r')

    for line in file:
        lst_string += line
    lst_chars = list(lst_string)
    for c in lst_chars:
        num = ord(c)
        lst[num] += 1
    file.close()
    return lst

def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''

    # ordered list of individual trees
    ordered_lst_trees = OrderedList()
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            node = HuffmanNode(i, char_freq[i])
            ordered_lst_trees.add(node)
    print(ordered_lst_trees.python_list())

    # if no entries
    if ordered_lst_trees.is_empty():
        return None

    # building actual tree
    while ordered_lst_trees.size() != 1:
        node1 = ordered_lst_trees.pop(0)
        node2 = ordered_lst_trees.pop(0)
        combined_freq = node1.freq + node2.freq
        if node1.char < node2.char:
            parent = HuffmanNode(node1.char, combined_freq)
        else:
            parent = HuffmanNode(node2.char, combined_freq)
        parent.left = node1
        parent.right = node2
        ordered_lst_trees.add(parent)
    return ordered_lst_trees.pop(0)

def create_code_helper(node, array, code):
    if node.left is None and node.right is None:
        array[node.char] = code
    else:
        create_code_helper(node.left, array, code + str(0))
        create_code_helper(node.right, array, code + str(1))
    return array

def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the array, with the resulting Huffman code for that character stored at that location'''
    array = 256 * ['']
    code = ''
    if node is not None:
        return create_code_helper(node, array, code)
    return array

def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list associated with "aaabbbbcc", would return “97 3 98 4 99 2”'''
    header = ''
    for i in range(len(freqs)):
        if freqs[i] != 0:
            header += str(i) + ' ' + str(freqs[i]) + ' '
    return header.rstrip()

def huffman_encode_helper(freq, file):
    file = open(file, 'r')
    node = create_huff_tree(freq)
    code = create_code(node)
    encoded = ''
    lst_string = ''
    for line in file:
        lst_string += line
    file.close()
    lst = list(lst_string)
    for x in lst:
        encoded += code[ord(x)]
    return encoded

def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take note of special cases - empty file and file with only one unique character'''
    try:
        file = open(in_file, 'r')
        file.close()
    except FileNotFoundError as error:
        raise FileNotFoundError
    else:
        freq = cnt_freq(in_file)
        header = create_header(freq)
        code = huffman_encode_helper(freq, in_file)
        file_out = open(out_file, 'w')
        file_out.write(header + '\n')
        if code != '':
            file_out.write(code)
        file_out.close()

        # create compressed filename
        compressed_lst = out_file.split('.')
        compressed_lst.insert(1, '_compressed')
        compressed_lst.insert(2, '.')
        compressed_str = ''.join(compressed_lst)

        # create compressed file with header and bits
        new_compressed = HuffmanBitWriter(compressed_str)
        new_compressed.write_str(header + '\n')
        if code != '':
            new_compressed.write_code(code)
        new_compressed.close()

def huffman_decode(encoded_file, decode_file):
    '''Reads an encoded text file and writes the decoded text into an output
    text file using the Huffman Tree produced by the header information. If the
    encoded_file does not exist, your program should raise the FileNotFoundError
    exception. If the specified output file already exists, its old contents will
    be overwritten'''
    try:
        file = HuffmanBitReader(encoded_file)
        file.close()
    except FileNotFoundError as error:
        raise FileNotFoundError
    else:
        compressed = HuffmanBitReader(encoded_file)
        header = compressed.read_str()
        freq = parse_header(header)
        tot_char = sum(freq)
        huff_tree = create_huff_tree(freq)
        curr = huff_tree
        # if empty
        if curr is None:
            file_out = open(decode_file, 'w')
            file_out.close()
        elif curr is not None and curr.right is None and curr.left is None:
            file_out = open(decode_file, 'w')
            file_out.write(curr.freq * chr(curr.char))
            file_out.close()
        else:
            file_out = open(decode_file, 'w')
            counter = 0
            while counter < tot_char:
                if not compressed.read_bit():
                    curr = curr.left
                else:
                    curr = curr.right
                if curr.right is None and curr.left is None:
                    file_out.write(chr(curr.char))
                    counter += 1
                    curr = huff_tree
            file_out.close()
            compressed.close()

def parse_header(header_string):
    '''Takes a string input parameter and returns a list of frequencies.
    The list of frequencies should be in the same format that cnt_freq()
    returned in the first part of this assignment'''

    lst = 256 * [0]
    stripped = header_string.strip()
    # if empty
    if stripped == '':
        return lst
    header_lst = stripped.split()
    for i in range(len(header_lst)):
        if i % 2 == 0:
            pos = int(header_lst[i])
            lst[pos] = int(header_lst[i + 1])
    return lst