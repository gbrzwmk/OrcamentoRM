import csv
from Imoveis import Apartamento, Casa, Estudio

def obter_sim_ou_nao(pergunta):
    """Função auxiliar para obter S/N do usuário."""
    while True:
        resposta = input(f"{pergunta} (S/N): ").strip().upper()
        if resposta == 'S':
            return True
        if resposta == 'N':
            return False
        print("Opção inválida. Digite 'S' para Sim ou 'N' para Não.")

def obter_numero(pergunta, min_val=0):
    """Função auxiliar para obter um número inteiro."""
    while True:
        try:
            valor = int(input(f"{pergunta}: ").strip())
            if valor >= min_val:
                return valor
            else:
                print(f"Valor inválido. Digite um número maior ou igual a {min_val}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def gerar_orcamento_apartamento():
    print("\n--- Orçamento: Apartamento ---")
    quartos = obter_numero("Quantos quartos (1 ou 2)", min_val=1)
    if quartos > 2: quartos = 2 # Limita a 2 conforme a regra
    if quartos == 1: print("Considerando 1 quarto.")
        
    garagem = obter_sim_ou_nao("Deseja incluir vaga de garagem? (+ R$ 300,00)")
    criancas = obter_sim_ou_nao("Possui crianças? (Perde desconto de 5%)")
    
    # Cria o objeto Apartamento
    apt = Apartamento(num_quartos=quartos, tem_garagem=garagem, tem_criancas=criancas)
    return apt

def gerar_orcamento_casa():
    print("\n--- Orçamento: Casa ---")
    quartos = obter_numero("Quantos quartos (1 ou 2)", min_val=1)
    if quartos > 2: quartos = 2
    if quartos == 1: print("Considerando 1 quarto.")

    garagem = obter_sim_ou_nao("Deseja incluir vaga de garagem? (+ R$ 300,00)")
    
    # Cria o objeto Casa
    casa = Casa(num_quartos=quartos, tem_garagem=garagem)
    return casa

def gerar_orcamento_estudio():
    print("\n--- Orçamento: Estúdio ---")
    pacote_vagas = obter_sim_ou_nao("Deseja o pacote de 2 vagas? (+ R$ 250,00)")
    vagas_extras = 0
    if pacote_vagas:
        vagas_extras = obter_numero("Quantas vagas ADICIONAIS deseja? (+ R$ 60,00 cada)", min_val=0)
        
    # Cria o objeto Estudio
    estudio = Estudio(quer_pacote_vagas=pacote_vagas, vagas_adicionais=vagas_extras)
    return estudio

def exibir_resultado(imovel):
    """Exibe o orçamento final e pergunta sobre o CSV."""
    orcamento = imovel.get_orcamento_final()
    valor_mensal = orcamento["aluguel_mensal"]
    taxa_contrato = orcamento["taxa_contrato"]

    print("\n--- RESULTADO DO ORÇAMENTO ---")
    print(f"Valor do Aluguel Mensal: R$ {valor_mensal:.2f}")  # 
    print(f"Taxa de Contrato: R$ {taxa_contrato:.2f} (pode ser parcelada em até 5x)")  # 
    
    # Gerar CSV
    if obter_sim_ou_nao("\nDeseja gerar um arquivo '.csv' com as 12 parcelas do orçamento?"):
        gerar_csv(valor_mensal)

def gerar_csv(valor_mensal):
    """Gera um arquivo CSV com 12 parcelas (meses)."""
    try:
        with open('orcamento_anual.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Mes', 'Valor Mensal'])  # Cabeçalho
            for mes in range(1, 13):
                writer.writerow([mes, f'R$ {valor_mensal:.2f}'])
        print("\nArquivo 'orcamento_anual.csv' gerado com sucesso!")
    except Exception as e:
        print(f"\nErro ao gerar CSV: {e}")

def menu_principal():
    """Loop principal da aplicação."""
    print("===========================================")
    print("  Bem-vindo à Calculadora de Aluguel R.M  ")
    print("===========================================")
    
    while True:
        print("\nQual tipo de imóvel você deseja orçar?")
        print("1: Apartamento")
        print("2: Casa")
        print("3: Estúdio")
        print("0: Sair")
        
        opcao = input("Digite a opção desejada: ").strip()
        
        imovel_orcado = None
        
        if opcao == '1':
            imovel_orcado = gerar_orcamento_apartamento()
        elif opcao == '2':
            imovel_orcado = gerar_orcamento_casa()
        elif opcao == '3':
            imovel_orcado = gerar_orcamento_estudio()
        elif opcao == '0':
            print("\nObrigado por usar a calculadora R.M!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            
        if imovel_orcado:
            exibir_resultado(imovel_orcado)
            input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    menu_principal()