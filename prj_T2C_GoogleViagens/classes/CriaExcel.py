from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException

import pandas as pd 

class TratarExcel:
    """
    Classe responsável pelo processamento dos dados no Excel.

    Parâmetros:
    
    Retorna:
    """
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro):
        """
        Inicializa a classe TratarExcel.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.

        Retorna:

        Raises:
        """
        self.var_dictConfig = arg_dictConfig
        self.var_clssMaestro = arg_clssMaestro


    def inserir_e_tratar_excel(self, arg_listViagem:list):
        
        try:
            df = pd.DataFrame(arg_listViagem)
            df.to_excel('dados_viagens.xlsx', index=False, sheet_name="Todos")
            print(df)

            # Ordena pelo valor da viagem e procura os 10 destinos mais baratos
            df_ordenado = df.sort_values(by='valorviagem').head(10)

            # Exporta um arquivo Excel com duas abas
            with pd.ExcelWriter('dados_viagens.xlsx') as writer:
                df.to_excel(writer, index=False, sheet_name='Todos')
                df_ordenado.to_excel(writer, index=False, sheet_name='Baratos')

            # Exibir os DataFrames
            print("Todos:")
            print(df)
            print("\nOs Mais baratos:")
            print(df_ordenado)
            
        except Exception as exception:
            raise Exception(f"Houve um erro ao processar o metodo 'inserir_e_tratar_excel' na classe 'TratarExcel' : {exception}")