Passo a passo para executar o programa.

Lado servidor:
1 - Inicie a aplicação do servidor.
2 - Selecione o modo de operação do servidor:
    * Se selecionar o modo automático, o servidor fara requisições a uma API do chatGPT de maneira automática 
    para responder a pergunta do cliente.
    * Caso selecione o  modo controlado, o servidor vai perguntar quem deve responder a pergunta, 
    humano ou máquina. Caso selecionar humano, você deve responder a pergunta do cliente. Caso selecionar máquina,
    uma rquisição a API do chatGPT será feita para responder a pergunta do cliente.
3 - Diga o tempo em segundos que o servidor deve esperar antes de enviar uma resposta ao cliente.

Lado cliente: 
4 - Inicie, em outra janela da sua IDE, a aplicação cliente (A conecção com o servidor será feita automaticamente).
5 - Diga seu nome para fins de registros.
6 - Faça uma pergunta.

Lado servidor: 
7 - Caso o modo controlado tiver sido escolhido, você deve informar quem deve responder a pergunta.

Lado cliente:
Ao receber a resposta, deve informar quem acredita que respondeu a pergunta, um humano ou uma máquina.

Faça quantas perguntas quiser.
Para encerrar a conecção com o servidor, digite a palavra "bye" no campo de realizar pergunta.
Ao finalizar a conecção, o resgistro de perguntas e resposta e o ranking de acertos serão atualizados.


