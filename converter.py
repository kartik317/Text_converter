import base64
from flask import flash

class BinaryConverter:
    @staticmethod
    def text_to_binary(text):
        try:
            binary_result = ' '.join(format(ord(char), '08b') for char in text)
            return binary_result
        except Exception as e:
            flash("Something went wrong in text to binary!")

    @staticmethod
    def binary_to_text(binary_text):
        try:
            binary_values = binary_text.split(' ')
            ascii_characters = [chr(int(b, 2)) for b in binary_values]
            return ''.join(ascii_characters)
        except Exception as e:
            flash("Something went wrong in binary to text!")
            

class Base64Converter:
    @staticmethod
    def text_to_base64(text):
        try:
            base64_bytes = base64.b64encode(text.encode('utf-8'))
            return base64_bytes.decode('utf-8')
        except Exception as e:
            flash("Something went wrong in text to base64!")

    @staticmethod
    def base64_to_text(base64_text):
        try:
            text_bytes = base64.b64decode(base64_text.encode('utf-8'))
            return text_bytes.decode('utf-8')
        except Exception as e:
            flash("Something went wrong in base64 to text!")
            
	   	
class HexadecimalConverter:
	@staticmethod	
	def text_to_hex(text):
	   try:
	   	return text.encode('utf-8').hex()
	   except Exception as e:
	   	flash("something went wrong text to hex!")
	
	@staticmethod  
	def hex_to_text(hex_string):
	   try:
	   	return bytes.fromhex(hex_string).decode('utf-8')
	   except Exception as e:
	   	flash("something went wrong hex to text!")
	   	
	   	
class OctalConverter:
	
	@staticmethod
	def text_to_octal(text):
	    try:
		    octal_string = ""
		    for char in text:
		        octal_char = oct(ord(char))[2:]
		        octal_string += octal_char + " "
		    return octal_string.strip()
	    except Exception as e:
	    	flash("something went wrong text to octal!")
	
	@staticmethod
	def octal_to_text(octal_string):
	    try:
		    text = ""
		    octal_values = octal_string.split()
		    for octal_char in octal_values:
		        char = chr(int(octal_char, 8))
		        text += char
		    return text
	    except Exception as e:
	    	flash("something went wrong octal to text!")
	   

class ConversionHelper:
	
	@staticmethod		
	def convert_text(text, format):
		match format:
			case "Convert to":
				return BinaryConverter.text_to_binary(text)
				
			case "Text To Binary":
				return BinaryConverter.text_to_binary(text)
				
			case "Binary To Text":
				return BinaryConverter.binary_to_text(text)
				
			case "Text To Hexadecimal":
				return HexadecimalConverter.text_to_hex(text)
				
			case "Hexadecimal To Text":
				return HexadecimalConverter.hex_to_text(text)
				
			case "Text To Octal":
				return OctalConverter.text_to_octal(text)
				
			case "Octal To Text":
				return OctalConverter.octal_to_text(text)
				
			case "Text To Base64":
				return Base64Converter.text_to_base64(text)
				
			case "Base64 To Text":
				return Base64Converter.base64_to_text(text)				