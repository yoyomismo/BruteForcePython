from ftplib import FTP
import sys

def conectar(usuario,password):
	try:
		ftp=FTP("127.0.0.1")
		ftp.login(usuario,password,"")
		ftp.quit()
		return True
	except:
		return False

fusuarios = open("usuarios.txt","r")
usuarios = fusuarios.readlines()
fpassword = open("passwords.txt","r")
passwords = fpassword.readlines()
for usuario in usuarios:
	for password in passwords:
		luser = usuario.rstrip('\r\n')
                lpassw = password.rstrip('\r\n')
		if conectar(luser,lpassw) == True:
			print "Login correcto (",luser," y ",lpassw,")"
			exit()
		else:
			print "Error al iniciar sesion"
