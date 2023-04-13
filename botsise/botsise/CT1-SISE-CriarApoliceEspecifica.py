from botcity.core import DesktopBot
import time
import pyautogui
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        #self.execute(r'C:\SISE\SISE.exe')
        
        if not self.find( "clicarMenuAdministracao", matching=0.97, waiting_time=10000):
            self.not_found("clicarMenuAdministracao")
        self.click()
        
        if not self.find( "clicarApoliceEspecifica", matching=0.97, waiting_time=10000):
            self.not_found("clicarApoliceEspecifica")
        self.click()
        
        if not self.find( "clicarEstipulante", matching=0.97, waiting_time=10000):
            self.not_found("clicarEstipulante")
        self.click()
        
        #if not self.find( "clicarFolhaBranca", matching=0.97, waiting_time=10000):
         #   self.not_found("clicarFolhaBranca")
        #self.click()
        
        if not self.find( "folhabranca", matching=0.97, waiting_time=10000):
            self.not_found("folhabranca")
        self.click()
        

        if not self.find( "digitarNomeDoEstipulante", matching=0.97, waiting_time=10000):
            self.not_found("digitarNomeDoEstipulante")
        time.sleep(6)
        self.double_click_relative(137, 7)
        self.paste('Teste')
        
        if not self.find( "digitarNomeDeFantansia", matching=0.97, waiting_time=10000):
            self.not_found("digitarNomeDeFantansia")
        self.double_click_relative(137, 9)
        self.paste('Teste')
        
        if not self.find( "digitarRazaoSocialNaoAbreviada", matching=0.97, waiting_time=10000):
            self.not_found("digitarRazaoSocialNaoAbreviada")
        self.double_click_relative(185, 5)
        self.paste('Teste')
        
        if not self.find( "clicarBotaoNovo", matching=0.97, waiting_time=10000):
            self.not_found("clicarBotaoNovo")
        self.click()
        
        if not self.find( "clicarTipoDocumento", matching=0.97, waiting_time=10000):
            self.not_found("clicarTipoDocumento")
        self.click_relative(139, 12)
        
        if not self.find( "selecionarCNPJ", matching=0.97, waiting_time=10000):
            self.not_found("selecionarCNPJ")
        self.click()

        cnpj = "87123555000109"
        
        if not self.find( "digitarNumeroDocumento", matching=0.97, waiting_time=10000):
            self.not_found("digitarNumeroDocumento")
        self.click_relative(129, 9)
        pyautogui.write(cnpj)
    
        if not self.find( "clicarBotaoConfirmar", matching=0.97, waiting_time=10000):
            self.not_found("clicarBotaoConfirmar")
        self.click()

        if not self.find( "clicarBotaoEndereco", matching=0.97, waiting_time=10000):
            self.not_found("clicarBotaoEndereco")
        self.click()

        if not self.find( "clicarBotaoNovo", matching=0.97, waiting_time=10000):
            self.not_found("clicarBotaoNovo")
        self.click()
        
        if not self.find( "digitarEndereco", matching=0.97, waiting_time=10000):
            self.not_found("digitarEndereco")
        self.click_relative(83, 11)
        self.paste('Rua Teste')
        
        if not self.find( "digitarComplemento", matching=0.97, waiting_time=10000):
            self.not_found("digitarComplemento")
        self.click_relative(105, 9)
        self.paste('Apto 1')
        
        if not self.find( "digitarBairro", matching=0.97, waiting_time=10000):
            self.not_found("digitarBairro")
        self.click_relative(86, 8)
        self.paste('Teste')
        

        cep = "70722500"

        if not self.find( "digitarCep", matching=0.97, waiting_time=10000):
            self.not_found("digitarCep")
        self.click_relative(63, 14)
        pyautogui.write(cep)
        
        if not self.find( "digitarCidade", matching=0.97, waiting_time=10000):
            self.not_found("digitarCidade")
        self.click_relative(74, 7)
        self.paste('BRASILIA')
        
        if not self.find( "expandirUf", matching=0.97, waiting_time=10000):
            self.not_found("expandirUf")
        self.click_relative(76, 8)

        if not self.find( "selecionarUfDistritoFederal", matching=0.97, waiting_time=10000):
            self.not_found("selecionarUfDistritoFederal")
        self.click()
        
        if not self.find( "expandirTipoEndereco", matching=0.97, waiting_time=10000):
            self.not_found("expandirTipoEndereco")
        self.click_relative(150, 6)
        
        if not self.find( "selecionarCorrespondencia", matching=0.97, waiting_time=10000):
            self.not_found("selecionarCorrespondencia")
        self.click()
        
        

        if not self.find( "clicarBotaoConfirmar", matching=0.97, waiting_time=10000):
            self.not_found("clicarBotaoConfirmar")
        self.click()
      
        if not self.find( "clicarBotaoSalvar", matching=0.97, waiting_time=10000):
            self.not_found("clicarBotaoSalvar")
        self.click()
        time.sleep(6)
        
        
        
        
        
        
    
        
        
        
        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()


