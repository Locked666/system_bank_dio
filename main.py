import time 
import os

LIMITE_SAQUE_QUANTIDADE = 3
LIMITE_SAQUE_VALOR = 500
INIT_SALDO = 100



transacoes_realizadas =  []
atual_limite_saque_quantidade = int(LIMITE_SAQUE_QUANTIDADE)
atual_limite_saque_valor = float(LIMITE_SAQUE_VALOR)
saldo_inicial =  float(INIT_SALDO)

menu_principal = f"""
     _____________________________
    |                             |
    | Bem vindo ao Banco Virtual! |
    |_____________________________|
    
    Escolha a opção necessária : 
    
    [1] - Realizar Depósito
    [2] - Realizar Saque.
    [3] - Emitir Extrato.
    [4] - Sair do Program.

"""

text_final_transacao = """

    Deseja  realizar outra operação?
    
    [1] -  Sim 
    [2] -  Não
"""

text_exit_program = """

    #### Obrigado  por usar o nosso sistema! ####
    
    ##############################
    ##    SAINDO DO PROGRAMA    ##
    ##############################
    
"""



while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    selecao = input(menu_principal)
    try: 
        if  int(selecao) == 1: #Depositar
            
                os.system('cls' if os.name == 'nt' else 'clear')
                valor = float(input("Informe o Valor que deseja Depositar: R$ "))
                
                if valor > 0 :
                    saldo_inicial += valor
                    transacao = {
                        "tipo" : "deposito",
                        "valor": valor,
                        "data" : time.strftime('%d/%m/%Y %H:%M:%S')
                    }
                    transacoes_realizadas.append(transacao)
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Deposito realizado no valor de R$ {valor:.2f}.")
                    time.sleep(1)
                    
                    final_operacao = input(text_final_transacao)
                    
                    if int(final_operacao) == 2:
                        break
                    else:
                        
                        continue
                else:
                    print("Valor do depósito não pode ser negativo:")
                    print(input("Pressione 'Enter' para continuar.").strip())
                    continue

                
                
        
        elif int(selecao) == 2 : # Saque
            os.system('cls' if os.name == 'nt' else 'clear')
            valor_saque = float(input("Informe o valor do saque: R$ "))
            
            
            if valor_saque < 0 :
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Valor  inválido para saque.\n Valor do saque não pode ser negativo")
                print(input("Pressione 'Enter' para continuar.").strip())
                continue
            
            
            if valor_saque > atual_limite_saque_valor:
                print(f"Valor do Saque maior do o limite permitido\n *** Limite de Saque {LIMITE_SAQUE_VALOR} ")
                print(input("Pressione 'Enter' para continuar.").strip())
                continue
            
            
            if atual_limite_saque_quantidade == 0 : 
                print(f"Quantidade diária de saque foi excedida\n *** Quantidade diária de Saque {LIMITE_SAQUE_QUANTIDADE} ")
                print(input("Pressione 'Enter' para continuar.").strip())
                continue
            
            
            if valor_saque > saldo_inicial :
                print(f"Saldo atual insuficiente para saque.")
                print(input("Pressione 'Enter' para continuar.").strip())
                continue 
            
                
            atual_limite_saque_quantidade -=1
            saldo_inicial -= valor_saque
            transacao = {
                "tipo" : "saque",
                "valor": valor_saque,
                "data" : time.strftime('%d/%m/%Y %H:%M:%S')
            }
            transacoes_realizadas.append(transacao)
            
            print(f"Saque realizado com sucesso!")
                    
            final_operacao = input(text_final_transacao)
            if int(final_operacao) == 2:
                break
            else:
                continue
            
            
                
        elif int(selecao) == 3 :  # Extrato
            total_depositos = 0 
            total_saques = 0 
            print(len(transacoes_realizadas))
            
            if len(transacoes_realizadas) != 0 : 
                
                for transacao in transacoes_realizadas:
                    if transacao['tipo'] == 'deposito':
                        total_depositos += transacao['valor']
                    elif transacao['tipo'] == 'saque':
                        total_saques += transacao['valor']
                        
                extrato_transacoes =  ""
                for  transacao in transacoes_realizadas:
                    tipo = transacao['tipo']
                    valor = transacao['valor']
                    data = transacao['data']
                    trasac = f"""
.    Tipo: {tipo.upper()}
.    Valor: R$ {float(valor):.2f}
.    Data: {data}
."""
                    extrato_transacoes +=trasac

                extrato = f"""
.    __________________________
.   |                          |
.   |    Extrato bancário      |
.   |__________________________|
.   Transações Realizadas:                                      
.     {extrato_transacoes}                               
.                                                                 
.                                                        
.   Saldo Inicial do dia: R$ {INIT_SALDO:.2f}.             
.   Total de Depositos: R$ {float(total_depositos):.2f}. 
.   Total de Saques: R$ {float(total_saques):.2f}.       
.              
.   Saldo Final = R$ {float(saldo_inicial):.2f}                                                    
..........................................................

extrato emitido em: {time.strftime('%d/%m/%Y %H:%M:%S')}  
 """   
                print(extrato)
                final_operacao = input(text_final_transacao)
                if int(final_operacao) == 2:
                    break
                else:
                    continue 
                
                    
            else:
                write_transacoes = f"""
                
.........................................................            
.     __________________________
.    |                          |
.    |    Extrato bancário      |
.    |__________________________|
.    
.    ##### NÃO FORAM REALIZADA MOVIMENTAÇÕES ####
.    
.    Saldo Atual: R$ {float(saldo_inicial):.2f}.
.    
............................................................
    extrato emitido em: {time.strftime('%d/%m/%Y %H:%M:%S')} 
"""
                print(write_transacoes)
                final_operacao = input(text_final_transacao)
                if int(final_operacao) == 2:
                    break
                else:
                    continue
        
        elif int(selecao) == 4: # Sair do Programa
            print(text_exit_program)
            
            for i in range(5):
                print('.',end=" ")
                time.sleep(1)
            break    
            
        else:
            print("Opção inválida")
            print(input("Pressione 'Enter' para continuar.").strip())
            continue
    except:
        print("informado uma entrada invalida\n Tente novamente Except")
        print(input("Pressione 'Enter' para continuar.").strip())
        continue        