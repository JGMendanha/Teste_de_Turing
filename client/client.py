import socket, sys

HOST = '127.0.0.1'  
PORT = 20000        
BUFFER_SIZE = 1024 


def main(argv): 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((HOST, PORT))
            print("Servidor executando!")
            name = input("DIGA SEU NOME ")
            s.send(name.encode())

            while(True):      
                print("\n======================================================================================================================\n")
                text = input("FAÇA SUA PERGUNTA (DIGITE bye PARA ENCERRAR O PROGRAMA): ")
                s.send(text.encode()) 
                if (text == 'bye'):
                    print('FINALIZADO')
                    s.close()
                    break
                data = s.recv(BUFFER_SIZE)
                texto_recebido = data.decode('utf-8') 
                print('RESPOSTA: ', texto_recebido)

                test = str(input("O TEXTO RECEBIDO FOI ENVIADO POR UMA MÁQUINA OU UM HUMANO ? (RESPONDA COM: maquina ou humano) "))
                s.send(test.encode())

    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":   
    main(sys.argv[1:])