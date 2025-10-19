"""
Observe o código no editor. Vamos analisar:

linhas 3 a 8: peça ao usuário o nome do arquivo a ser copiado e tente abri-lo para ler; encerrar a execução do programa se a abertura falhar; nota: use a exit()função para interromper a execução do programa e passar o código de conclusão para o sistema operacional; qualquer código de conclusão que não 0diga que o programa encontrou alguns problemas; use o errnovalor para especificar a natureza do problema;
linhas 9 a 15: repita quase a mesma ação, mas desta vez para o arquivo de saída;
linha 17: preparar um pedaço de memória para transferir dados do arquivo de origem para o arquivo de destino; essa área de transferência é freqüentemente chamada de buffer, daí o nome da variável; o tamanho do buffer é arbitrário - neste caso, decidimos usar 64 kilobytes; tecnicamente, um buffer maior é mais rápido para copiar itens, pois um buffer maior significa menos operações de E / S; na verdade, há sempre um limite, cuja ultrapassagem não traz melhorias adicionais; teste você mesmo, se quiser.
linha 18: contar os bytes copiados - este é o contador e seu valor inicial;
linha 20: tente preencher o buffer pela primeira vez;
linha 21: contanto que você obtenha um número diferente de zero de bytes, repita as mesmas ações;
linha 22: escreva o conteúdo do buffer no arquivo de saída (nota: usamos uma fatia para limitar o número de bytes sendo gravados, pois write()sempre preferimos escrever o buffer inteiro)
linha 23: atualiza o contador;
linha 24: lê a próxima parte do arquivo;
linhas 29 a 31: alguma limpeza final - o trabalho está feito.

"""


from os import strerror

srcname = input("Source file name?: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)	
dstname = input("Destination file name?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create destination file: ", strerr(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create destination file: ", strerr(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()