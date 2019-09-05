from Huffman import Huffman

#input file path
path = "alice.txt"

h = Huffman(path)

output_path = h.compress()
h.decompress(output_path)