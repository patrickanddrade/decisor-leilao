# decisor_leilao.py

def calcular_rendimento(valor, tempo, tipo):
    """
    Função que calcula o rendimento do investimento
    :param valor: valor investido
    :param tempo: tempo em meses
    :param tipo: tipo de investimento (string)
    :return: valor final com rendimento
    """
    if tipo == "Tesouro Selic":
        taxa = 0.008  # 0,8% ao mês
    elif tipo == "Tesouro Prefixado":
        taxa = 0.010
    elif tipo == "Tesouro IPCA+":
        taxa = 0.007 + 0.003
    elif tipo == "Poupança":
        taxa = 0.005
    elif tipo == "CDB":
        taxa = 0.009
    elif tipo == "Conta Bancária":
        taxa = 0.0
    else:
        return "Tipo de investimento inválido!"

    valor_final = valor * ((1 + taxa) ** tempo)
    return round(valor_final, 2)


# ------------------------------
# Função de exemplo para imóveis
# ------------------------------

def simular_imovel(valor_mercado, valor_leilao, oferta, aluguel=0):
    """
    Função para simular decisão de imóvel em leilão.
    Retorna um dicionário com resultados e justificativas simples.
    """
    custos_extras = valor_leilao * 0.05  # 5% de custos extras
    max_oferta = valor_mercado * 0.8 - custos_extras  # oferta aceitável = 80% do mercado - custos

    recomendacao = "Investigar mais"
    justificativas = []

    if max_oferta >= oferta:
        recomendacao = "Comprar"
        justificativas.append(f"Máx. oferta aceitável ({max_oferta:.2f}) >= oferta planejada ({oferta:.2f})")
    else:
        justificativas.append(f"Máx. oferta aceitável ({max_oferta:.2f}) < oferta planejada ({oferta:.2f})")

    retorno_anual_percent = (aluguel * 12 / valor_leilao * 100) if aluguel else None

    return {
        "recomendacao": recomendacao,
        "max_oferta_calculada": max_oferta,
        "debitos_total": 0,
        "extras_total": custos_extras,
        "retorno_anual_percent": retorno_anual_percent,
        "justificativas": justificativas
    }
