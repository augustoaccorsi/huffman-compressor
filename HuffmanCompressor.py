import heapq
import os
import zlib
from HeapNode import HeapNode

class HuffmanCompressor:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}
		self.crc = 0

	def calculate_crc(self, fileName):
		prev = 0
		for eachLine in open(fileName,"rb"):
			prev = zlib.crc32(eachLine, prev)
		return "{0:b}".format(int("%X"%(prev & 0xFFFFFFFF), 16))

	def get_path(self):
		return self.path
		
	def get_crc(self):
		return self.crc
	
	def get_file_type(self):
		if ".txt" in self.path:
			return ".txt"
		else:
			return ""
	
	def get_reverse_mapping(self):
		return self.reverse_mapping

	def make_frequency_dict(self, text):
		frequency = {}
		for character in text:
			if not character in frequency:
				frequency[character] = 0
			frequency[character] += 1
		return frequency

	def make_heap(self, frequency):
		for key in frequency:
			node = HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)

	def merge_nodes(self):
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged = HeapNode(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged)

	def make_codes_helper(self, root, current_code):
		if(root == None):
			return

		if(root.char != None):
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char
			return

		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")

	def make_codes(self):
		root = heapq.heappop(self.heap)
		current_code = ""
		self.make_codes_helper(root, current_code)


	def get_encoded_text(self, text):
		encoded_text = ""
		for character in text:
			encoded_text += self.codes[character]
		return encoded_text


	def pad_encoded_text(self, encoded_text):
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text


	def get_byte_array(self, padded_encoded_text):
		if(len(padded_encoded_text) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)

		b = bytearray()	

		if(len(self.crc) < 32):
			for i in range(32-len(self.crc)):
				self.crc = "0" + str(self.crc)
		
		for i in range(0, len(self.crc), 8):
			byte = self.crc[i:i+8]
			b.append(int(byte, 2))

		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b

	def compress(self):
		filename = os.path.splitext(self.path)
		output_path = filename[0] + ".bin"

		self.crc = self.calculate_crc(self.path)
	
		file_type = ''
		if ".txt" in self.path:
			file_type = 'r+'
		else:
			file_type = 'r+b'

		with open(self.path, file_type) as file, open(output_path, 'wb') as output:
			text = file.read()
			text = text.rstrip()

			frequency = self.make_frequency_dict(text)
			self.make_heap(frequency)
			self.merge_nodes()
			self.make_codes()

			encoded_text = self.get_encoded_text(text)
			padded_encoded_text = self.pad_encoded_text(encoded_text)

			b = self.get_byte_array(padded_encoded_text)
			output.write(bytes(b))

		print("File "+self.path+" compressed as "+output_path)
		return output_path	
