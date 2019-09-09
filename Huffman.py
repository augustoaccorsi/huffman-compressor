import sys
import heapq
import os
from HeapNode import HeapNode
from HuffmanDecompressor import HuffmanDecompressor
from HuffmanCompressor import HuffmanCompressor

class Huffman:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}

#input file path
path = sys.argv[1]

hc = HuffmanCompressor(path)
output_path = hc.compress()

hd = HuffmanDecompressor(hc)
hd.decompress(output_path)
