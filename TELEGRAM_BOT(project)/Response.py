from datetime import datetime
from email import message

command_list = """ 

Lista dos Comandos Programados
/help - obtenha a lista dos comandos
/clientes - obtenha os dados de todos os clientes 
/cliente <cliente_id> - obtenha o dados de um cliente

"""

def search_sample(input_text):

   user_message = str(input_text) 
   #tentando fazer uma resposta super basica.. de um forma burra.
   if user_message  in ("39550"):  
    return """ 
    |Pedido Nº313

    |Valor: R$17,001|
    |Item | Quantidade | valor|
    +--------------------------------------------+
    |Toddynho | 5 | R$7,0         |
    |Fandangos| 2 | R$10,00   |
    +--------------------------------------------+
        """

   if user_message  in ("21856"):  
    return """ 
    |Pedido Nº001

    |Valor: R$9999,00|
    |Item | Quantidade | valor|
    +--------------------------------------------+
    |Cana da Cantina | 99 | R$7,0         |
    |Jedi Chips| 99 | R$10,00   |
    +--------------------------------------------+
        """   

   if user_message  in ("49400"):  
    return """ 
    |Pedido Nº510

    |Valor: R$5900,00|

    |Item | Quantidade | valor|
    +--------------------------------------------+
    |Antartica | 55 | R$7,0         |
    |Torcida Presunto| 36 | R$10,00   |
    +--------------------------------------------+
        """    
   if user_message  in ("44993"):  
    return """ 
    |Pedido Nº666

    |Valor: R$950,00|

    |Item | Quantidade | valor|
    +--------------------------------------------+
    |Fluido de Junta | 55 | R$7,0         |
    |Trakinas Morango| 36 | R$10,00   |
    +--------------------------------------------+
        """
    #mesmo com brincadeirinhas eu ainda deixei os valores estaticos dentro dos preços p/unidade
   if user_message in ("Comandos", "comandos", "comando", "Comando"): #uma forma alternativa para receber a listagem de comandos

    return(command_list) 

   if user_message  in ("ok", "Ok", "Certo", "certo"): #bobeirinha
    return "Tudo certinho!" 

   return "Não entendi" 
