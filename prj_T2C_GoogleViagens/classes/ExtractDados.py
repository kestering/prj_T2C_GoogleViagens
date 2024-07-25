from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException

from clicknium import clicknium as cc, locator, ui

class ExtrairDadosMundiais:
    """
    Classe responsável pelo processamento principal.

    Parâmetros:
    
    Retorna:
    """
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro):
        """
        Inicializa a classe ExtrairDadosMundiais.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.

        Retorna:

        Raises:
        """
        self.var_dictConfig = arg_dictConfig
        self.var_clssMaestro = arg_clssMaestro
            
    def execute(self):
        try:
            var_listCountries = []
            var_tabNav = cc.edge.open(self.var_dictConfig['UrlSiteDadosMundiais'])

            for i in range(2, 5):
                var_strNomePais = var_tabNav.find_element_by_xpath(f'//*[@id="main"]/div[3]/div[2]/table/tbody/tr[{i}]/td[2]/a').get_text()
                var_listCountries.append(var_strNomePais)

            var_tabNav.close()    

            return var_listCountries
        
        except Exception as exception:
            raise Exception(f"Houve um erro ao processar o metodo 'execute' da classe 'ExtrairDadosMundiais' : {exception}")
