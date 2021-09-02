from random import randint
comandos = ["olhar", "inventario", "norte", "sul", "leste", "oeste", "abrir", "falar","andar para o norte","andar para o sul","andar para o leste","andar para o oeste", "atacar", "defender"]
#Serve para indicar a fase: 1 para casa, 2 para labirinto, 3 para cidade abandonada, 4 para acampamento, 5 para cidade, 6 para castelo
espadaMagica = False
flores = False
inventario = ["espada", "escudo"]
def casa():
    while True:
        texto = input(">").lower()
        if texto not in comandos:
            print("Não entendi o que quis dizer. Tente outro comando.")
            print("Digite uma direção para olhar(norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção")
            print("Aqui você pode olhar em volta ou abrir a caixa. Para abrir digite 'abrir'")
            print(comandos)
        elif texto == "inventario":
            print("Este é o seu inventário atual:")
            print(inventario)
        elif texto == "sul" :
            print(" Ao sul há somente sua casa.")
        elif texto =="norte" :
            print("No norte há um caminho que leva até os mais diversos lugares.")
        elif texto == "oeste" :
            print("Existe uma grande floresta nessa direção. Não é recomendado entrar lá.")
        elif texto == "leste" :
            print("Nessa direção só é possível avistar uma antiga cidade abandonada no horizonte.")
        elif texto == "olhar":
            print("É uma bela vista das montanhas no horizonte.")
        elif "andar" in texto:
            print("Não é possivel andar agora.")
        elif "atacar" in texto or "defender" in texto:
            print("Você não pode fazer isso aqui.") 
        elif texto == "abrir" or texto == carta :
            print("A carta diz: Olá nobre cavaleiro, sou o Rei deste belo pais de Valor.")
            print("Ouvi grandes historias sobre seu passado como herói. Por causa disso, venho por meio desta lhe pedir um grande favor.")
            print(" Em breve, ocorrerá uma grande festa em meu castelo, com o objetivo de unir as casas de Anansi e Alland porém, uma de minhas ")
            print("filhas, a princesa Lyana foi capturada durante a noite por inimigos do reino. Eu preciso que voce a resgate para que a ")
            print("festa possa acontecer da maneira prevista. é possivel que essa aventura não seja fácil, então se prepare. Para chegar a")
            print(" meu castelo basta seguir o caminho ate a cidade de Battlerhill e de lá podera avistá-lo.")
            carta()
            print(f"Olá {nome}, para onde você quer ir?(norte,sul,leste,oeste)")
            while True:
                texto = input(">").lower()
                if texto not in comandos:
                    print("Não entendi o que quis dizer. Tente outro comando.")
                    print("Digite \"andar para o sul\"(por exemplo),para andar nessa direção")
                elif texto == "inventario":
                    print("Este é o seu inventário atual:")
                    print(inventario)
                elif texto == "andar para o norte":
                    norte(1)
                elif texto == "andar para o sul":
                    sul(1)
                elif texto == "andar para o leste":
                    leste(1)
                elif texto =="andar para o oeste":
                    oeste(1)
        else:
            return texto        
def labirinto(j):
    if j == 0:   
        print("Antes de seguir aventura, você pega seus equipamentos: sua fiel espada, um escudo usado e sua mochila de viagem. ")
        print("Seguindo o caminho que lhe foi indicado pelo Rei, você percorre por durante 2 dias a estrada ate encontrar o grande labirinto de Moormaze.")
        print("Na entrada deste enorme labirinto há um guarda.")
        while True:
            print("Você pode olhar ao redor usando as direcoes, andar, olhar o labirinto ou falar com o guarda.")
            print("Para olhar o labirinto digite 'olhar' e para falar com o guarda 'falar'.")
            texto = input(">").lower()
            if texto not in comandos:
                print("Não entendi o que quis dizer. Tente outro comando.")
                print("Digite a direção desejada para olhar (norte,sul,leste,oeste) ou \"andar para o sul\",por exemplo,para andar nessa direção")
                print(comandos)
            elif texto == "inventario":
                print("Este é o seu inventario atual:")
                print(inventario)
            elif "falar" in texto:
                if genero == "m":
                    print("'Olá aventureiro. Se busca passagem pelo labirinto lamento lhe informar, mas é muito perigoso." )
                elif genero == "f":
                    print("'Olá aventureira. Se busca passagem pelo labirinto lamento lhe informar, mas é muito perigoso." )
                print("Nele habita um monstro um terço homem, um terço touro e um terço orc. Agora, como essa mistura ocorreu não sei responder.")
                print("Além disso, a chave do portão foi roubada por um grupo de ladrões.")
                print("Se não me engano eles foram para uma cidade abandonada a leste daqui.")
            elif "olhar" in texto:
                print("Há uma placa nas paredes que diz:")
                print("'Esse labrint e o gra de Mo nmaze, const  ido milen s atr s pelo Rei Dan'zard par guard r um per goso monstr'")
                print("A placa parece bem desgastada.")
            elif "atacar" in texto or "defender" in texto:
                print("Você não pode fazer isso aqui.") 
            elif texto == "norte":
                print("Só é possivel ver o labrinto.")
            elif texto == "sul" :
                print("Esse é o caminho de que você veio.")
            elif texto =="leste" :
                print("Na distancia, se pode avistar a tal cidade fantasma.")
            elif texto == "oeste" :
                print("A floresta densa ainda está ao seu oeste, não é recomendado entrar lá.")
            elif texto == "andar para o norte":
                norte(2)
            elif texto == "andar para o sul":
                sul(2)
            elif texto == "andar para o leste":
                leste(2)
            elif texto =="andar para o oeste":
                oeste(2)
            else:
                return texto
    if j == 1: #Segunda parte do labirinto
        print("De volta a entrada do labirinto, o guarda o vê e pergunta:")
        print("'Então a princesa realmente foi raptada, ainda bem que veio a resgatar. Eu nem sabia disso.")
        print("Vejo que conseguiu a chave! Vou guadar a entrada, para que ninguem mais entre por aqui e atrapalhe o resgate.")
        print("A porta foi aberta e você adentrou o labirinto. Está muito escuro e difícil de enxergar")
        print("Digite uma direção para olhar ao redor(norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção")
        #sala 1 - caminho para o norte e leste
        while True:
            sala1()
def sala1():
    while True:
        texto = input(">").lower()
        if texto not in comandos:
            print("Não entendi o que quis dizer. Tente outro comando.")
            print("Digite uma direção para olhar  ao redor (norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção")
            print(comandos)
        elif texto == "inventario":
                print("Este é o seu inventário atual:")
                print(inventario)
        elif "atacar" in texto or "defender" in texto:
            print("Você não pode fazer isso aqui.") 
        elif texto == "sul" :
            print("Atrás tem a entrada do Moormaze")
        elif texto =="norte" :
            print("Há um corredor nessa direção")
        elif texto == "oeste" :
            print("Somente uma parede")
        elif texto == "leste" :
            print("Uma parede.Porém ha um desenho estranho nessa parede:")
            print("      |")
            print("    _ _")
            print("   |_")
            print("     |")     
        elif texto == "andar para o norte":
            sala2()
        elif texto == "andar para o sul":
            print("Não é possível voltar agora.")
        elif texto == "andar para o leste" or texto =="andar para o oeste":
            print("Tem uma parede nessa direção")          
        else:
            return texto
def sala2():
    print("Você chegou ao final do corredor.")
    while True:
        texto = input(">").lower()
        if texto not in comandos:
            print("Não entendi o que quis dizer. Tente outro comando.")
            print("Digite uma direção para olhar  ao redor (norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção.")
            print(comandos)
        elif texto == "inventario":
            print("Este é o seu inventário atual:")
            print(inventario)
        elif "atacar" in texto or "defender" in texto:
            print("Você não pode fazer isso aqui.") 
        if texto == "sul" :
            print("Para trás tem o corredor de onde você veio.")
        elif texto =="norte" or texto == "leste" :
            print("Há uma parede.")
        elif texto == "oeste" : #sala 3
            print("O corredor continua por aqui.")
        elif texto == "andar para o norte" or texto =="andar para o leste":
            print("Tem uma parede nessa direção.")
        elif texto == "andar para o oeste":
            sala3()
        elif texto == "andar para o sul":
            sala1()
        else:
            return texto
def sala3():
    print("Há um caminho para o norte e para o oeste.")
    while True:
        texto = input(">").lower()
        if texto not in comandos:
            print("Não entendi o que quis dizer. Tente outro comando.")
            print("Digite uma direção para olhar  ao redor (norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção.")
            print(comandos)
        elif texto == "inventario":
            print("Este é o seu inventário atual:")
            print(inventario)
        elif "atacar" in texto or "defender" in texto:
            print("Você não pode fazer isso aqui.") 
        if texto == "sul" :
            print("Parede.")
        elif texto =="norte":
            print("Há um corredor ao norte.")
        elif texto == "oeste" : #sala 3
            print("Outro corredor continua por aqui.") 
        elif texto == "andar para o norte"  :
            print("Você continuou ao norte.")
            sala4()
        elif  texto =="andar para o leste":
            print("Você voltou uma sala.")
            sala2()
        elif texto == "andar para o oeste":
            print("Porém, você se perdeu no labirinto e ficou preso para sempre.")
            print("FIM DE JOGO")
            print("O jogo vai recomecar da entrada do labirinto.")
            labirinto(1)
        elif texto == "andar para o sul":
            print("Tem uma parede.")
        else:
            return texto
def sala4():
    print("Dois corredores surgem aqui, um para o norte e outro para o leste.")
    while True:
        texto = input(">").lower()
        if texto not in comandos:
            print("Não entendi o que quis dizer. Tente outro comando.")
            print("Digite uma direção para olhar  ao redor (norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção.")
            print(comandos)
        elif texto == "inventario":
            print("Este é o seu inventário atual:")
            print(inventario)
        elif "atacar" in texto or "defender" in texto:
            print("Você não pode fazer isso aqui.") 
        if texto == "sul" :
            print("O corredor de onde você veio é nessa direção.")
        elif texto =="norte":
            print("Há um corredor ao norte.")
        elif texto == "oeste" : #sala 3
            print("Somente uma parede.") 
        elif texto == "leste":
            print("Há um outro corredor para o leste.")
        elif texto == "andar para o norte"  :
            print("Você continuou ao norte.")
            print("Porém, você se perdeu no labirinto e ficou preso para sempre.")
            print("FIM DE JOGO")
            print("O jogo vai recomecar da entrada do labirinto.")
            labirinto(1)
        elif  texto =="andar para o leste":
            print("Você continuou pelos corredores, até encontrar uma luz  em uma curva para o norte")
            print("Ao chegar na luz, vc avista a sala onde o monstro do labirinto vive e também vê a princesa, capturada pelos piratas")
            print(" acorrentada. Quando ela te vê grita por ajuda, acordando o monstro. Agora para salvá-la, você deve derrotar o monstro!!")
            combate(4, 6, 2, 6)
        elif texto == "andar para o oeste":
            print("Porém, você se perdeu no labirinto e ficou preso para sempre.")
            print("FIM DE JOGO")
            print("O jogo vai recomecar da entrada do labirinto.")
            labirinto(1)
        elif texto == "andar para o sul":
            sala1()
        else:
            return texto
def cidadeFantasma():
    print("Após alguns minutos, você chega a cidade abandonada de Nightthunder.")
    while True:
        texto = input(">").lower()
        if texto not in comandos:
            print("Não entendi o que quis dizer. Tente outro comando.")
            print(comandos)
        elif texto == "inventario":
            print("Este é o seu inventário atual:")
            print(inventario)
        elif "andar" in texto:
            print("Não é seguro andar por aqui. Olhe ao seu redor primeiro.")
        elif "atacar" in texto or "defender" in texto:
            print("Você não pode fazer isso aqui.") 
        elif texto == "norte":
            print("As casas da cidade estão completamente detruidas e abandonadas. Ninguém mora aqui há anos.")
        elif texto == "sul":
            print("Um dia houve um mercado nessa direção.")
        elif  texto =="leste":
            print("A área vazia a sua frente parece ter sido uma praça")
        elif texto == "oeste":
            print("Parece haver um movimento no beco dessa direção. Você vai investigar")
            print("Ao chegar no beco você ve uma gangue de piratas, que te cercam!")
            if genero == "m":
                print("Pirata1: 'Ah sim, você deve ser o herói que veio resgatar a princesa do reino, não é mesmo? ")
            if genero == "f":
                print("Pirata1: 'Ah sim, você deve ser a heroína que veio resgatar a princesa do reino, não é mesmo? ")
            print("Eu sou Tomad Green, o lider da gangue dos piratas!!'")
            print("Pirata2: 'Sim, fomos nós que a raptamos e entregamos ao minotauro dentro do labirinto HAHAHAHA'")
            if genero == "m":
                print("Tomad Green: ' Fique quieto novato! Não conte os planos para ele, vamos derrotá-lo agora!")
            if genero == "f":
                 print("Tomad Green: ' Fique quieto novato! Não conte os planos para ela, vamos derrotá-la agora!")
            combate(3, 3, 1, 8)

        
def norte(n):
    if n == 1: #significa que esta em casa
        labirinto(0)
    if n == 2:
        print("Nessa direção está o labirinto.")
    if n == 3:
        print("Você e a princesa Lyana seguiram viagem para o castelo, onde o Rei De Valor a espera.")
        print("Ao chegar no castelo, todos ficam aliviados com a princesa estar a salvo e o parabenizam pelo seu ato heróico.")
        print(f"Rei: Muito obrigado jovem {nome}, por resgatar a minha filha. Como consideração, você receberá uma condecoração de herói do reino.")
        print("E se ela quiser, ofereço a mão da minha filha Lyana a você")
        if flores:
            print("As flores que você pegou podem te ajudar, e você as oferece para a dama, que fica lisonjeada e aceita.")
            print("Lyana:Eu gostaria sim pai. Foi ele que me salvou daquele minotauro estranho!")
            print("FIM")
            print("Você resgatou a princesa e conseguiu a mão dela parabéns!")
        if flores == False:
            if genero == "m":
                print("Lyana:Infelizmente não gostaria pai. Eu sempre gostei mais de meninas. Mas como Foi ele me salvou daquele minotauro estranho")
                print("ele poderia ganhar um posto de cavaleiro para me proteger de novo!")
                print("FIM")
                print("Você resgatou a princesa mas não conseguiu a mão dela. De qualquer forma, parabéns!")
            elif genero == "f":
                print("Lyana:Infelizmente não gostaria pai. Eu sempre gostei mais de meninos. Mas como Foi ela me salvou daquele minotauro estranho")
                print("ela poderia ganhar um posto de cavaleira para me proteger de novo!")
                print("FIM")
                print("Você resgatou a princesa mas não conseguiu a mão dela. De qualquer forma, parabéns!")
def sul(n):
    if n == 1:
        print("Você deve seguir o caminho para resgatar a princesa, ao norte daqui")
        norte(1)
    if n == 2: #significa que esta no labirinto
        print("É preciso continuar sua jornada. Deseja mesmo retornar a sua casa e desistir da viagem?")
    if n == 3:
        print("Não é possivel voltar agora.")
def leste(n):
    if n == 1:
        print("Você deve seguir o caminho para resgatar a princesa, ao norte daqui")
        norte(1)
    if n == 2:
        cidadeFantasma()
    if n == 3:
        print("Nos campos de flores você pode pegar algumas. Elas podem servir para alguma coisa.")
        global flores
        flores = True
        inventario.append("flores")
def oeste(n):
    if n == 1:
        print("Você deve seguir o caminho para resgatar a princesa, ao norte daqui")
        norte(1)
    if n == 2:#significa que esta no labirinto
        print("Parabéns pela exploração! Você encontrou um báu velho no meio da floresta. Nele repousa uma espada mágica. Ela pode ajudar na sua jornada.")
        print("Você escuta alguns barulhos amedrontadores na floresta. É melhor sair dái agora.")
        print("Você está de volta a frente do labirinto.")
        global espadaMagica
        espadaMagica = True
        inventario.append("espada mágica")
    if n == 3:
        print("Para essa direção há somente um campo aberto. Não ha nada lá.")
def combate(n, inimigo, dano, prob):
    vida = 5
    vidaDoInimigo = 0
    print("Você está em combate. Para atacar seus inimigos, digite 'atacar'. Para evitar um ataque, digite 'defender'. Se você tomar 5 ataques em seguida, tera que recomeçar.")
    vidaDoInimigo = inimigo
    while vida > 0 or vidaDoInimigo > 0:
        texto = input(">").lower()
        x = randint(1,10)
        y = randint(1,10)
        if texto not in comandos:
            print("Digite 'atacar' para atacar e 'defender' para defender")
        if texto == "atacar":
            if espadaMagica == False:
                if x <= prob:
                    vidaDoInimigo -= 1
                    print("Você acertou o inimigo!")
                elif x>prob:
                   print("Você errou o inimigo!") 
            if espadaMagica:
                if x <= prob:
                    vidaDoInimigo -= 2
                    print("Você acertou o inimigo!")
                elif x>prob:
                    print("Você errou o inimigo!") 
        elif y > prob:
            if texto == "atacar":
                vida -= dano
                print("O inimigo te acertou!")
            if texto == "defender":
                print("O inimigo não consegue atacar!")
                return texto
        print(f"A sua vida é {vida} e a vida do inimigo é {vidaDoInimigo}.")
        if vida == 0:
            print("Você perdeu a batalha. Recomece este combate.")
            combate(3)
        elif vidaDoInimigo <= 0:
            if n == 3:
                print("Você ganhou o combate!! Parabéns! Agora com a chave do labrinto em sua posse, você retornou ao labirinto para abri-lo, adentrando suas salas tortuosas.")
                inventario.append("chave")
                labirinto(1)
            if n == 4:
                print("Você ganhou o combate!! Parabéns!")
                final()
def final():
    print("O monstro do labirinto foi derrotado e a princesa salva. Agora só resta seguir viagem atá a cidade do castelo.")
    print("Agora, você so precisa seguir em frente, ja que ja é possível ver o castelo ao norte!")
    print("Você esta na saída do labirinto.")
    print("Digite uma direção para olhar(norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção")
    while True:
        texto = input(">").lower()
        if texto not in comandos:
            print("Não entendi o que quis dizer. Tente outro comando.")
            print("Digite uma direção para olhar(norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção")
            print("Você pode olhar em volta ou abrir a caixa. Para abrir digite 'abrir'")
            print(comandos)
        elif texto == "inventario":
            print("Este é o seu inventário atual:")
            print(inventario)
        elif "atacar" in texto or "defender" in texto:
            print("Você não pode fazer isso aqui.") 
        elif texto == "sul" :
            print("Ao sul há somente o labirinto.")
        elif texto =="norte" :
            print("No norte há um caminho que leva até a cidade do castelo.")
        elif texto == "oeste" :
            print("Existe um campo aberto nessa direção.")
        elif texto == "leste" :
            print("Nessa direção um grande campo de flores percorre ate o horizonte.")
        elif texto == "andar para o norte":
            norte(3)
        elif texto == "andar para o sul":
            sul(3)
        elif texto == "andar para o leste":
            leste(3)
        elif texto =="andar para o oeste":
            oeste(3)
        else:
            return texto

         
def carta():
    global nome
    nome = input("Qual o seu nome?")
    global genero
    genero = input("Qual o seu gênero?(f ou m)")
def start():
    print("Olá, seja bem vindo ao Tales of Valor, a saga épica de um herói em busca de aventuras!! ")
    print("Utilize os comandos verbiais no terminal para guiar o seu herói para um final digno de grandeza.")
    print("Mais um dia nasce, e você acorda em seu castelo e,como sempre, o dia se repete da mesma forma neste seu pacato castelo.")
    print("Porém, ao chegar de sua caminhada matinal, um de seus criados o avisa que há uma carta a sua espera na caixa de correspondências.")
    print("A sua frente se encontra a entrada da casa, junto com a caixa de correspondências.")
    print("Digite uma direção para olhar(norte,sul,leste ou oeste) ou \"andar para o sul\"(por exemplo),para andar nessa direção")
    print("Você pode olhar em volta ou abrir a caixa. Para abrir digite 'abrir'")
    casa()
start()










                           