import heapq
import os
import sys

class HuffmanDecompressor:
	def __init__(self, compressor):
		self.path = compressor.get_path()
		self.reverse_mapping = compressor.get_reverse_mapping()
		self.crc = compressor.get_crc()
	
	def validate_crc(self, crc_from_input):
		if(self.crc != crc_from_input):
			sys.exit("File with error")

	def remove_padding(self, padded_encoded_text):
		padded_info = padded_encoded_text[len(self.crc):len(self.crc)+8]
		
		self.validate_crc(padded_encoded_text[:len(self.crc)])

		extra_padding = int(padded_info, 2)

		padded_encoded_text = padded_encoded_text[8:] 
		encoded_text = padded_encoded_text[:-1*extra_padding]

		return encoded_text

	def decode_text(self, encoded_text):
		current_code = ""
		decoded_text = ""

		for bit in encoded_text:
			current_code += bit
			if(current_code in self.reverse_mapping):
				character = self.reverse_mapping[current_code]
				decoded_text += character
				current_code = ""

		return decoded_text


	def decompress(self, input_path):
		filename = os.path.splitext(self.path)
		output_path = filename[0] + "_decompressed" + ".txt"

		with open(input_path, 'rb') as file, open(output_path, 'w') as output:
			bit_string = ""

			byte = file.read(1)
			while(len(byte) > 0):
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = file.read(1)

			encoded_text = self.remove_padding(bit_string)

			decompressed_text = self.decode_text(encoded_text)
			
			output.write(decompressed_text)

		print("Decompressed")
		return output_path