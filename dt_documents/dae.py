class Move_files_done:
    destinations = {
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

    def __init__(self, source_dir, adto=False):
        self.source_dir = 'C:\\DOCUMENTOS ROTINA'
        self.destinations = self.destinations if not adto else self.destinations_adto

    def moving(self):
        for filename in os.listdir(self.source_dir):
            keyword = filename.split("-")

            if keyword[2] in ["Guia", "GRF"]:
                keyword = keyword[2]
            else:
                keyword = keyword[1]

            if keyword in self.destinations:
                shutil.move(os.path.join(self.source_dir, filename), os.path.join(self.destinations[keyword], filename))


