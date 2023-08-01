def info_usuario():
    while True:   
        try:
            print("Informe seu nome completo:")
            nome = input()
            print("Informe sua data de nascimento:")
            nasci = int(input())
            print("ano atual")
            anoAtual = 2022
            if(nasci <= 1922) and (nasci >= 2001):
                  raise ValueError("data inválida, insira uma data entre 1922 e 2001")
            idade = anoAtual - nasci
            print("meu nome é:",nome ,"eu nasci em",nasci ,"minha idade é",idade) 
            return True
        except ValueError as e:
            print(e)
            print("tente novamente.")
        except:
            print("algo deu errado. Finalizando.")
            return False  

info_usuario() 