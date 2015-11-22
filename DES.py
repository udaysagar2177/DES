#This program is written by Uday Sagar Shiramshetty, studying 3rd year CSE, at MANIT-Bhopal
#It is written according to the python 3 syntax. Just run this program and follow the instructions 
#for encryption and decryption
#Any comments may be addressed to udaysagar.2177@gmail.com

from DESCommon import DES, generate_keys
from DESUtil import to_binary, add_pads_if_necessary, hex_to_bin, bin_to_hex, bin_to_text

try:
    input = raw_input
except NameError:
    pass

def get_bits(plaintext):
    text_bits = []
    for i in plaintext:
        text_bits.extend(to_binary(ord(i)))
    return text_bits

def encrypt(plaintext, key_text):
	keys = generate_keys(key_text)

	text_bits = get_bits(plaintext)
	text_bits = add_pads_if_necessary(text_bits)

	final_cipher = ''
	for i in range(0, len(text_bits), 64):
		final_cipher += DES(text_bits, i, (i+64), keys)

	# conversion of binary cipher into hex-decimal form
	hex_cipher = ''
	i = 0
	while i < len(final_cipher):
		hex_cipher += bin_to_hex(final_cipher[i:i+4])
		i = i+4
	return hex_cipher

def decrypt(cipher, key_text):
	keys = generate_keys(key_text)

	text_bits = []
	ciphertext = ''
	for i in cipher:
		# conversion of hex-decimal form to binary form
		ciphertext += hex_to_bin(i)
	for i in ciphertext:
		text_bits.append(int(i))

	text_bits = add_pads_if_necessary(text_bits)
	keys.reverse()
	bin_mess = ''
	for i in range(0, len(text_bits), 64):
		bin_mess += DES(text_bits, i, (i+64), keys)

	i = 0
	text_mess = ''
	while i < len(bin_mess):
		text_mess += bin_to_text(bin_mess[i:i+8])
		i = i+8
	return text_mess.rstrip('\x00')

def main():
    print('Enter the choice')
    print('1. ENCRYPT A MESSAGE')
    print('2. DECRYPT A MESSAGE')
    choice = int(input())

    key_text = str(input('Enter the key\n'))

    if(len(key_text) < 8):
    	print('Key must be 8 characters in length. Exiting...')
    	return

    if(choice == 1):
        plaintext = str(input('Enter the message(in Text-form)\n'))
        cipher = encrypt(plaintext, key_text)
        print('the cipher is(in hex-decimal form)')
        print(cipher)

    else:
        cipher = str(input('Enter the message(in hex-decimal form)\n'))
        plaintext = decrypt(cipher, key_text)
        print('the original text is')
        print(plaintext)

    print('exiting...')
    return

if __name__ == "__main__":
    main()
