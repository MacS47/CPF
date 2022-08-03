# ==============================================================================

    # Dígitos verificadores garantem a validade de um cpf
    # sendo que a regra é a seguinte:

    # Para descobrir o dígito verificador 1:
    # n1 = [10,9,8,7,6,5,4,3,2]
    # verificador = (cpf[0] * n[0]) + (cpf[1]*n[1]) + ... + (cpf[8]*n[8])
    # se (verificador % 11 < 2 ):
    #   dígito1 = 0
    # senao:
    #   dígito1 = (11 - (verificador % 11))

    # Para descobrir o dígito verificador 2:
    # n2 = [11,10,9,8,7,6,5,4,3,2]
    # verificador = (cpf[0] * n[0]) + (cpf[1]*n[1]) + ... + (cpf[9]*n[9])
    # se (verificador % 11 < 2 ):
    #   dígito2 = 0
    # senao:
    #   dígito2 = (11 - (verificador % 11))

# ==============================================================================

import random

def validar_cpf(cpf):

    # Lista que receberá os 9 dígitos informados pelo usuário
    # concatenando com os dígitos verificadores calculados dentro da própria função
    temp_cpf = []

    # Declarando e incializando string que receberá itens 
    # de temp_cpf concatenados, para posterior comparação
    mcpf = ''

    # Variáveis auxiliadoras
    y = 1
    z = 0

# ========================== PRIMEIRO DÍGITO VERIFICADOR ==========================

    # O loop garante um iteração de cpf[0] até cpf[8]
    # como cpf é informado ao chamar a função assume-se que este possui 11 dígitos
    # Para identificar o primeiro dígito verificador, precisamos realizar o cálculo
    # assinalado acima
    for i in cpf[-11:-2]:
        temp_cpf.append(int(i))
        z = z + (int(i)*int(len(cpf)-y))
        
        # Verificando se é a última iteração em cpf       
        if(int(i) == int(cpf[8]) and y == 9):

            # Verificando o resto da divisão de z sobre 11
            # Se for menor que 2, o primeiro dígito assume 0 
            if(z % 11 < 2):
                temp_cpf.append(0)
            # Senão recebe o resultado de 11: - (resto da divisão de z sobre 11)
            else:
                temp_cpf.append(11-(z % 11))

# ========================== SEGUNDO DÍGITO VERIFICADOR ===========================

            # Atribuindo novos valores às variáveis auxiliadoras
            y = 0
            z = 0

            # O loop abaixo realiza uma iteração de cpf[0] até cpf[9]
            # Para identificar o segundo dígito verificador,
            for i in temp_cpf:
                z = z + (int(i)*int(len(temp_cpf) + 1 - y))

                # Verificando se é a última iteração em temp_cpf
                if(int(i) == int(cpf[9]) and y == 9):

                    # Verificando o resto da divisão de z sobre 11
                    # Se for menor que 2, o segundo dígito assume 0
                    if(z % 11 < 2):
                        temp_cpf.append(0)
                    # Senão recebe o resultado de: 11 - (resto da divisão de z sobre 11)
                    else:
                        temp_cpf.append(11-(z % 11))
                    
                    # Inserindo em mcpf items da lista temp_cpf
                    for i in temp_cpf:
                        mcpf = str(mcpf) + str(i)

                        # Verificando se mcpf possuir 11 dígitos
                        if(len(mcpf) == 11):

                            # Verificando se os caracteres em mcpf são iguais a cpf
                            if(str(mcpf) == str(cpf)):
                                print(f"\nCPF válido!") 
                            else:
                                print(f"\nCPF inválido!")

                # Incrementando y do loop em temp_cpf
                y = y + 1

        # Icrementando y do loop em cpf
        y = y + 1


# ---------------

def gerar_cpf():

    # Declaração e atribuição de valores às variáveis
    cpf = ""
    list_a = []
    list_v = []
    x = 11
    y = 0
    z = 0

# ========================== PRIMEIRO DÍGITO VERIFICADOR ==========================

    # Loop criado para determinar o primeiro dígito verificador
    while x > 2:
        list_a.append(random.randint(0,9))
        list_v.append(x-1)
        z = z + (int(list_a[y]) * int(list_v[y]))
        
        # Verificando se é a última iteração do while
        if(x == 3):
            
            # Verificando o resto da divisão de z sobre 11
            # Se for menor que 2, o primeiro dígito assume 0
            if(z % 11 < 2):
                list_a.append(0)

            # Senão recebe o resultado de: 11 - (resto da divisão de z sobre 11)
            else:
                list_a.append(11-(z % 11))

# ========================== SEGUNDO DÍGITO VERIFICADOR ===========================

            # Preparando as variáveis para nova iteração 
            x = 12
            y = 0
            z = 0
            list_v = []

            # Loop criado para determinar o segundo dígito verificador
            while x > 2:
                list_v.append(x-1)
                z = z + (int(list_a[y]) * int(list_v[y]))

                # Verificando se é a última iteração do while
                if(x == 3):
                    
                    # Verificando o resto da divisão de z sobre 11
                    # Se for menor que 2, o segundo dígito assume 0
                    if(z % 11 < 2):
                        list_a.append(0)

                    # Senão recebe o resultado de: 11 - (resto da divisão de z sobre 11)
                    else:
                        list_a.append(11-(z % 11))
            
                    # Inserindo em cpf items da lista list_a
                    for item in list_a:
                        cpf = cpf+str(item)
                
                # Incrementos do loop para determinar o segundo dígito verificador
                y = y + 1
                x = x - 1
        
        # Incrementos do loop para determinar o primeiro dígito verificador
        y = y + 1
        x = x - 1
   
    # Retornando à chamada da função um CPF válido
    return cpf