import os
import shutil


class Move_files:
    destinations_normal = {
        'ProgramaçãodeFérias': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias',
        'ExtratoMensal': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos',
        'RecibodePagamento': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites',
        'RelatóriodeLíquidos': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos',
        'AV': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\AvisosdeVencimento',
        'DAE': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\DAE',
        'IRRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\IRRF',
        'GRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\FGTS',
        'Guia': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\INSS',
    }

    destinations_adto = {
        'ExtratoMensal': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA',
        'RecibodePagamento': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA',
        'RelatóriodeLíquidos': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA',
        'AV': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\AvisosdeVencimento',
        'DAE': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\DAE',
        'IRRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\IRRF',
        'GRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\FGTS',
        'Guia': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\INSS',
    }

    def __init__(self, adto=False):
        self.source_dir = 'C:\\DOCUMENTOS ROTINA'
        self.destinations = self.destinations_adto if adto else self.destinations_normal

    def moving(self):
        for filename in os.listdir(self.source_dir):
            keyword = filename.split("-")

            if keyword[2] in ["Guia", "GRF"]:
                keyword = keyword[2]
            else:
                keyword = keyword[1]

            if keyword in self.destinations:
                shutil.move(os.path.join(self.source_dir, filename), self.destinations[keyword[2]] + '\\' + filename)


class Move_files_done:
    # Define the source and destination directories
    source_dir_normal = {
        'ProgramaçãodeFérias': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias',
        'ExtratoMensal': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos',
        'RecibodePagamento': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites',
        'RelatóriodeLíquidos': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos',
        'AV': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\AvisosdeVencimento',
        'DAE': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\DAE',
        'IRRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\IRRF',
        'GRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\FGTS',
        'Guia': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\INSS',
    }

    source_dir_adto = {
        'ExtratoMensal': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA',
        'RecibodePagamento': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA',
        'RelatóriodeLíquidos': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA',
        'AV': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\AvisosdeVencimento',
        'DAE': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\DAE',
        'IRRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\IRRF',
        'GRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\FGTS',
        'Guia': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\INSS',
    }
    destinations_normal = {
        'ProgramaçãodeFérias': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Ferias',
        'ExtratoMensal': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Extratos',
        'RecibodePagamento': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Holerites',
        'RelatóriodeLíquidos': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Liquidos',
        'AV': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\AvisosdeVencimento',
        'DAE': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\DAE',
        'IRRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\IRRF',
        'GRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\FGTS',
        'Guia': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\INSS',
    }

    destinations_adto = {
        'ExtratoMensal': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\ExtratosA',
        'RecibodePagamento': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\HoleritesA',
        'RelatóriodeLíquidos': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\LiquidosA',
        'AV': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\AvisosdeVencimento',
        'DAE': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\DAE',
        'IRRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\IRRF',
        'GRF': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\FGTS',
        'Guia': 'C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\INSS',
    }

    def __init__(self, adto=False):
        self.source_dir = self.source_dir_adto if adto else self.source_dir_normal
        self.destinations = self.destinations_adto if adto else self.destinations_normal

    def moving(self):
        for keyword in self.source_dir:
            source = self.source_dir[keyword]
            destination = self.destinations[keyword]
            files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
            for file in files:
                shutil.move(os.path.join(source, file), destination)


Move_files()
