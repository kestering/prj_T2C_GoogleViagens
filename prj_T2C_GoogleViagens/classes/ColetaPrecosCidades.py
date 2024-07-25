from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException

from clicknium import clicknium as cc, locator, ui 
from pywinauto.keyboard import send_keys 
import time

class TravelExplore:
    """
    Classe responsável por pesquisar valores e cidades no Travel Explore.

    Parâmetros:
    
    Retorna:
    """
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro):
        """
        Inicializa a classe TravelExplore.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.

        Retorna:

        Raises:
        """
        self.var_dictConfig = arg_dictConfig
        self.var_clssMaestro = arg_clssMaestro       

    def pesquisar_viagem(self, arg_listViagem:list, arg_strCidadeOrigem:str, arg_strCidadeDirecao:str, arg_strDataPartida:str, arg_strDataVolta:str):
        """ 
        Inicializa a classe ExtrairDadosMundiais.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.

        Retorna:

        Raises:
        """        
        try:
            var_tabNavegador = cc.edge.open(self.var_dictConfig['UrlSiteGoogleTravel'])

            var_tabNavegador.find_element(locator.Edge.cbx_de).click()

            cc.send_text(arg_strCidadeOrigem)

            send_keys('{ENTER}')

            time.sleep(2)

            var_tabNavegador.find_element(locator.Edge.cbx_para).double_click()

            time.sleep(2)

            cc.send_text(arg_strCidadeDirecao)

            time.sleep(2)

            var_dictLocatorDinamico = {"paisdestino": arg_strCidadeDirecao}

            var_tabNavegador.find_element(locator.Edge.img_terra, var_dictLocatorDinamico).click()

            var_tabNavegador.find_element(locator.Edge.field_calendar).click()

            time.sleep(5)

            var_tabNavegador.find_element(locator.Edge.field_datas).click()

            time.sleep(2)

            var_tabNavegador.find_element(locator.Edge.field_data_inicial).set_text(arg_strDataPartida)

            send_keys('{TAB}')

            time.sleep(2)

            var_tabNavegador.find_element(locator.Edge.field_data_final).set_text(arg_strDataVolta)

            time.sleep(2)

            var_tabNavegador.find_element(locator.Edge.field_data_final).click()

            send_keys('{TAB}')
            send_keys('{TAB}')

            time.sleep(7)



            try:
                for i in range(1, 100):
                    var_strCidade = var_tabNavegador.find_element_by_xpath(f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{i}]/div/div[2]/div[1]/h3').get_text()
                    var_strValorViagem = var_tabNavegador.find_element_by_xpath(f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{i}]/div/div[2]/div[2]/div[1]/div[1]/span').get_text()    
                    var_dictDadosViagem = {
                    'cidade': var_strCidade,
                    'valorviagem': var_strValorViagem.replace('\xa0', '')
                    }
                    arg_listViagem.append(var_dictDadosViagem)

            except Exception as exception:
                
                var_tabNavegador.close()

                return arg_listViagem
        except Exception as exception:
            raise Exception(f"Houve um erro ao processar o metodo 'pesquisar_viagem' da classe 'TravelExplore' : {exception}")
