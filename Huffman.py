import sys
import heapq
import os
from HeapNode import HeapNode
from HuffmanDecompressor import HuffmanDecompressor
from HuffmanCompressor import HuffmanCompressor
import zlib

def calculate_crc(fileName):
    prev = 0
    for eachLine in open(fileName,"rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)

path = sys.argv[1]

hc = HuffmanCompressor(path)
output_path = hc.compress()

print(calculate_crc(output_path))

hd = HuffmanDecompressor(hc)
hd.decompress(output_path)


