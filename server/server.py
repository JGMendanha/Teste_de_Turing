import socket, sys
from threading import Thread
import api
from time import sleep

HOST = '127.0.0.1' 
PORT = 20000        
BUFFER_SIZE = 1024  

def on_new_client(clientsocket,addr, timer, option):
    info_client = clientsocket.recv(BUFFER_SIZE)
    info_client = info_client.decode('utf-8')
    questions = []
    answers = []
    test_turing = []
    turing = []
    with open("registros.txt", 'a') as file: 
        with open("ranking.txt", 'w') as file2: 
            while True:
                try:
                    data = clientsocket.recv(BUFFER_SIZE)
                    if not data:
                        break
                    text_received = data.decode('utf-8')

                    if (text_received == 'bye'):
                        file.write("=======================================================================================================================\n")
                        file.write(f"NOME DO CLIENTE: {info_client}\n")
                        for i in range(len(questions)):
                            file.write("-------------------------------------------------------------------------------------------------------------------\n")
                            file.write(f"PERGUNTA: {questions[i]}\nRESPOSTA: {answers[i]}\nTESTE DE TURING: {test_turing[i]}\nQUEM RESPONDEU: {turing[i]}\n")
                        file.write("=======================================================================================================================\n")
                        print(f"O CLIENTE {info_client} ENCERROU A CONECÇÃO")
                        
                        clientsocket.close() 
                        return
                    
                    questions.append(text_received)
                    
                    print("\n======================================================================================================================\n")
                    if option == 1: 
                        answer = api.question(text_received)
                        turing.append("maquina")
                    else: 
                        print(f"PERGUNTA DO CLIENTE: {text_received}")
                        who_answer = int(input("QUEM DEVE RESPONDER ESSA PERGUNTA ? (1 PARA HUMANO / 2 PARA MÁQUINA) "))
                        if who_answer == 1:
                            answer = str(input("DIGITE A RESPOSTA: "))
                            turing.append("humano")
                        else:
                            answer = api.question(text_received) 
                            turing.append("maquina")

                    answers.append(answer)

                    sleep(timer)

                    clientsocket.send(answer.encode()) 
                    
                    test = clientsocket.recv(BUFFER_SIZE)
                    test = test.decode('utf-8')
                    test_turing.append(test)

                except Exception as error:
                    print("Erro na conexão com o cliente!!")
                    file.write("=======================================================================================================================\n")
                    file.write(f"NOME DO CLIENTE: {info_client}\n")
                    for i in range(len(questions)):
                        file.write("-------------------------------------------------------------------------------------------------------------------\n")
                        file.write(f"PERGUNTA: {questions[i]}\nRESPOSTA: {answers[i]}\nTESTE DE TURING: {test_turing[i]}\nQUEM RESPONDEU: {turing[i]}\n")
                    file.write("=======================================================================================================================\n")
                    return

def main(args):
    option = int(input("BEM VINDO A APLICAÇÃO DO LADO SERVIDOR\nPARA COMEÇAR DIGA QUAL MODO DESEJA QUE SEJA EXECUTADO\nDIGITE 1 PARA MODO AUTOMATICO E 2 PARA MODO CONTROLADO "))
    timer = int(input("PARA FINALIZAR, DIGITE O TEMPO EM SEGUNDOS QUE A APLICAÇÃO DEVE ESPERAR PARA ENVIAR A RESPOSTA AO CLIENTE "))
    timer = timer * 100
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            print("Server started")
            while True:
                server_socket.listen()
                clientsocket, addr = server_socket.accept()
                print('Conectado ao cliente no endereço:', addr)
                t = Thread(target=on_new_client, args=(clientsocket,addr, timer, option))
                t.start()                
    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)  
          
if __name__ == "__main__":   
    main(sys.argv[1:])
