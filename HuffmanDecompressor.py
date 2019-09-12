import heapq
import os
import sys

class HuffmanDecompressor:
	def __init__(self, compressor):
		self.path = compressor.get_path()
		self.reverse_mapping = compressor.get_reverse_mapping()
		self.crc = compressor.get_crc()
		self.file_type = compressor.get_file_type()
	
	def validate_crc(self, crc_from_input):
		if(self.crc != crc_from_input):
			sys.exit("File with error")

	def remove_padding(self, padded_encoded_text):
		padded_info = padded_encoded_text[:8]
		extra_padding = int(padded_info, 2)
		padded_encoded_text = padded_encoded_text[8:]
		encoded_text = padded_encoded_text[:-extra_padding]
		return encoded_text

	def decode_text(self, encoded_text):
		current_code = ""
		decoded_text = ""
		decode_file = bytearray()
		for bit in encoded_text:
			current_code += bit
			if(current_code in self.reverse_mapping):
				character = self.reverse_mapping[current_code]
				if(self.file_type != ".txt"):
					decode_file.append(character)
				else:
					decoded_text += str(character)
				current_code = ""
		
		if(self.file_type == ""):
			return decode_file
		return decoded_text

	def remove_crc(self, bit_string):
		self.validate_crc(bit_string[:len(self.crc)])
		return bit_string[len(self.crc):]

	def decompress(self, input_path):
		filename = os.path.splitext(self.path)
		output_path = filename[0] + "_decompressed" + self.file_type

		self.file_type != '.txt'
		if ".txt" in self.path:
			output_type = 'w'
		else:
			output_type = 'wb'	

		with open(input_path, 'rb') as file, open(output_path, output_type) as output:
			bit_string = ""
			count = 0
			a = ""
			b = bytearray()
			byte = file.read(1)
			while(len(byte) > 0):
				b.append(ord(byte))
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = file.read(1)
			
			encoded_text = self.remove_padding(self.remove_crc(bit_string))
			decompressed_text = self.decode_text(encoded_text)

			if(output_type == 'wb'):
				output.write(bytes(decompressed_text))
			else:
				output.write(decompressed_text)

		print("File "+input_path+" decompressed as "+output_path)
		return output_path