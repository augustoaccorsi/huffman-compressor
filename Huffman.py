import sys
import heapq
import os
import filecmp
from HeapNode import HeapNode
from HuffmanDecompressor import HuffmanDecompressor
from HuffmanCompressor import HuffmanCompressor

def compress(path):
    hc = HuffmanCompressor(path)
    output_path = hc.compress()
    hd = HuffmanDecompressor(hc)
    return hd.decompress(output_path)

def are_identical(input_file, output_file):    
    if(filecmp.cmp(input_file, output_file)):
        print("Files are identical")
    else:
        print("Files not identical")

print()

if(len(sys.argv) > 1):
    for i in range(len(sys.argv)-1):
        print(len(sys.argv))
        are_identical(sys.argv[i+1], compress(sys.argv[i+1]))
        print()
else:
    are_identical("files\\alice29.txt", compress("files\\alice29.txt"))
    print()
    are_identical("files\\sum", compress("files\\sum"))



