class Imovel:
    TAXA_CONTRATO = 2000.00  # 

    def __init__(self, aluguel_base):
        self._aluguel_base = aluguel_base
        self.valor_mensal_final = 0.0

    def calcular_aluguel(self):
        raise NotImplementedError("Subclasse deve implementar este método")

    def get_orcamento_final(self):
        """Retorna o valor mensal final e a taxa de contrato."""
        return {
            "aluguel_mensal": self.valor_mensal_final,
            "taxa_contrato": self.TAXA_CONTRATO
        }


class Apartamento(Imovel):
    """Calcula o aluguel de um Apartamento."""
    def __init__(self, num_quartos, tem_garagem, tem_criancas):
        super().__init__(aluguel_base=700.00)  # 
        self.num_quartos = num_quartos
        self.tem_garagem = tem_garagem
        self.tem_criancas = tem_criancas
        self.calcular_aluguel()

    def calcular_aluguel(self):
        valor = self._aluguel_base

        if self.num_quartos == 2:
            valor += 200.00  # 
        
        if self.tem_garagem:
            valor += 300.00  # 
        
        if not self.tem_criancas:
            desconto = valor * 0.05
            valor -= desconto  # 
        
        self.valor_mensal_final = valor


class Casa(Imovel):
    """Calcula o aluguel de uma Casa."""
    def __init__(self, num_quartos, tem_garagem):
        super().__init__(aluguel_base=900.00)  # 
        self.num_quartos = num_quartos
        self.tem_garagem = tem_garagem
        self.calcular_aluguel()

    def calcular_aluguel(self):
        valor = self._aluguel_base

        if self.num_quartos == 2:
            valor += 250.00  # 
        
        if self.tem_garagem:
            valor += 300.00  # 
        
        self.valor_mensal_final = valor


class Estudio(Imovel):
    """Calcula o aluguel de um Estúdio."""
    def __init__(self, quer_pacote_vagas, vagas_adicionais=0):
        super().__init__(aluguel_base=1200.00)  # 
        self.quer_pacote_vagas = quer_pacote_vagas # Pacote base de 2 vagas
        self.vagas_adicionais = vagas_adicionais
        self.calcular_aluguel()

    def calcular_aluguel(self):
        valor = self._aluguel_base

        if self.quer_pacote_vagas:
            
            valor += 250.00  # 
            
            
            if self.vagas_adicionais > 0:
                valor += self.vagas_adicionais * 60.00  # 
        
        self.valor_mensal_final = valor