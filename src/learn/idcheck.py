#! /usr/bin/env python
# _*_coding:utf-8_*_
"'标识符号"
import string

alphals = string.letters + '_'
number = string.digits
alphalsnumber=alphals + number
def main():
	print 'The indentifier Checker v1.0'
	indentifier = raw_input('Indentifier to test?')
	if len(indentifier) > 1:
		if indentifier[0] not in alphals:
			print'"invaid: the first symbol must be alphabetic."'
		else:
			for o_char in indentifier[1:]:
				if o_char not in alphalsnumber:
					print'" invaid: the symbol of indentifier must be alphanumeric. "'
					break
			else:
				print "okay!"
if __name__ == '__main__':
	main()


