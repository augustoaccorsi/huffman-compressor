import sys
import heapq
import os
import filecmp
from HeapNode import HeapNode
from HuffmanDecompressor import HuffmanDecompressor
from HuffmanCompressor import HuffmanCompressor

path = sys.argv[1]

hc = HuffmanCompressor(path)
output_path = hc.compress()

hd = HuffmanDecompressor(hc)
decompressed_path = hd.decompress(output_path)

if(filecmp.cmp(path, decompressed_path)):
    print("Files are identical")
else:
    print("Files not identical")


