#Nome: JOSÉ GUILHERME NETO
#Curso: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

# Importanto biblioteca random
import random
import time

#Tela inicial
#Desenho de zumbi que criei
print ("\33[1;32m      ______________________ \n|    /.:::::::: :::|||   ::..\ \n|  /::::::::#:\:    :::  : ::.\  \n| | ____       \________:::::::|  ______________________________________________ \n| ||o   |      |     o   | ::|||  Devore cérebros. Não leve um tiro na cabeça. \n|  |\___/ * *    \_______/|||||   Nome: José Guilherme Neto \n|  ''''\/''''W''''\  :::  ''/     Professor:  Galbas Milleo Filho \n|       __M_____/\/:  ::'/        ''''''''''''''''''''''''''''''''''''''''''''''  \n|       \_________''''/ \33[1;32m")
print("|")

regras = input ("Quer ler as regras? [ sim / nao ] ")

if regras == 'sim':
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Olá jogador!, vamos ver as regras antes de caçar cérebros?   \n  - O jogo necessita de pelo menos 2 jogadores;  \n  - A cada rodada será jogado três dados virtuais que podem cair C / P / T; \n  - C = Cérebros / P = Passos / T = Tiros; \n  - Você precisa pegar 13 cérebros para vencer; \n  - Passos significa que sua presa fugiu; \n  - Tiros significa que revidaram, 3 tiros e nem você sobrevive \n  - Você pode jogar de novo quantas vezes quiser, mas \n terá que jogar de novo os dados que estão em passos, e sempre deverá jogar 3 dados (Contanto com os Passos;")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Check para ter no mínimo 2 jogadores
numberPlayers = int(input("Numero de players   "))
while numberPlayers < 2:
    print("Não podemos começar a caçada com menos de dois ZuMbIs!!")
    numberPlayers = int(input("Numero de players   "))

# Chave para ENTRADA de jogadores:
entrada_de_jogadores = 0
while entrada_de_jogadores == 0:
        print("QUE COMECE A CAÇADA!!!")
        listPlayers = []

# Rotina para receber qualquer quantia de jogadores
        for ind in range(0, numberPlayers):
            nome = input("Nome do Zumbi:\n")
            cerebros = 0
            tiros = 0
            passos = 0
            #Para contabilizar pontos
            player = [nome, cerebros, tiros]
            listPlayers.append(player)
            # Chave para fechar seleção de jogadores
            entrada_de_jogadores = 1

# Desenho de Zumbi
print ("\33[1;32m      ______________________ \n|    /.:::::::: :::|||   ::..\ \n|  /::::::::#:\:    :::  : ::.\  \n| | ____       \________:::::::|  ______________________________________________ \n| ||o   |      |     o   | ::|||  Devore cérebros. Não leve um tiro na cabeça. \n|  |\___/ * *    \_______/|||||   BOA SORTE JOGADOR! \n|  ''''\/''''W''''\  :::  ''/      \n|       __M_____/\/:  ::'/        ''''''''''''''''''''''''''''''''''''''''''''''  \n|       \_________''''/ \33[1;32m")

# Criando copo para conter dados
copo = ["CPCTPC", "CPCTPC", "CPCTPC", "CPCTPC", "CPCTPC", "CPCTPC", "TPCTPC", "TPCTPC", "TPCTPC", "TPCTPC", 'TPTCPT', 'TPTCPT', 'TPTCPT']

# Chave de ativação do laço de repetição
chave_de_ativacao = False


# Ficar rodando os players
for player in listPlayers:
    chave_de_ativacao = False

    # Laço para jogar os dados de todos os jogadores, 1 por 1
    while not chave_de_ativacao:
        print(f"É a vez do zumbi {player}")
        time.sleep(2)
        print("Se preparando para jogar os dados... \n \n")

        # pegando os 3 dados
        for i in range(0,3):
            time.sleep(1)
            dados = random.choice(copo)
            copo.remove(dados)

            #Escolhendo a face e mostrando ao jogador
            face = random.choice(dados)
            if face == "C":
                print("|VOCÊ DEVOROU UM CERÉBRO")
                cerebros = cerebros + 1

            elif face == "P":
                print("|EXISTE MAIS UM SOBREVIVENTE... DROGA, ESCAPOU")
                passos = passos + 1

            elif face == "T":
                print("|VOCÊ LEVOU UM TIRO!!!")
                tiros = tiros + 1

                # mostrando mais especifico
            print(f"|Seu dado foi { dados }, e caiu: { face } \n")
            time.sleep(2)
        decisao = input("Tem coragem de arriscar de novo? [ s / n ]:  ")
        print(f"\33[1;32m      ______________________ \n|    /.:::::::: :::|||   ::..\ \n|  /::::::::#:\:    :::  : ::.\  \n| | ____       \________:::::::|  ______________________________________________ \n| ||o   |      |     o   | ::|||  QUE CAÇADA!! Você comeu {cerebros} CEREBROS  \n|  |\___/ * *    \_______/|||||   ÉÉé... {passos} pessoas fugiram, vai tentar pegar?! \n|  ''''\/''''W''''\  :::  ''/     UI! levou {tiros} tiros \n|       __M_____/\/:  ::'/        ''''''''''''''''''''''''''''''''''''''''''''''  \n|       \_________''''/ ")
        if decisao == "n":
            
            # chava para fechar o laço
            chave_de_ativacao = True

