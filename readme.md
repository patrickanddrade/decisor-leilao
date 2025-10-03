# 🏠✨ Decisor de Imóveis em Leilão

## 🚀 Introdução
Bem-vindo ao **Decisor de Imóveis em Leilão**! 😃  
Este projeto ajuda você a **decidir se vale a pena arrematar um imóvel em leilão** com base em:

- 💰 **Valor de mercado**  
- 🏷️ **Valor do leilão**  
- 📊 **Custos extras e débitos**  
- 🏘️ **Retorno estimado via aluguel**  

Tudo isso é calculado automaticamente e exibido de forma clara no navegador! 🌐

---

## 📋 Descrição do Projeto
O sistema combina **Python**, **Flask**, **HTML/CSS** e cálculos financeiros simples para fornecer:

- 🖥️ **Front-end interativo** com formulário  
- ⚙️ **Back-end em Python** para cálculo de máxima oferta aceitável  
- 🎨 **Estilo CSS** para tornar a interface agradável e fácil de usar  

---

---

## 🗂️ Estrutura de Pastas
O projeto segue a seguinte organização:

decisor-leilao/
│
├─ app.py # Arquivo principal do Flask
├─ decisor_leilao.py # Código Python com funções de cálculo
├─ requirements.txt # Dependências do projeto
├─ templates/
│ └─ index.html # Página HTML com o formulário e resultados
├─ static/
│ └─ style.css


## 🐍 Código Python – `decisor_leilao.py`

Este arquivo contém a função principal que calcula o rendimento de investimentos ou imóveis em leilão:

```python
def calcular_rendimento(valor, tempo, tipo):
    """
    Função que calcula o rendimento do investimento
    :param valor: valor investido
    :param tempo: tempo em meses
    :param tipo: tipo de investimento (string)
    :return: valor final com rendimento
    """
    if tipo == "Tesouro Selic":
        taxa = 0.008
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
```

##🔹 Código Flask – app.py

Responsável por receber os dados do formulário e exibir o resultado:
```python
from flask import Flask, render_template, request
from decisor_leilao import calcular_rendimento

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        valor = float(request.form["valor_mercado"])
        tempo = int(request.form.get("tempo", 12))  # tempo padrão 12 meses
        tipo = request.form.get("tipo", "Tesouro Selic")

        resultado = calcular_rendimento(valor, tempo, tipo)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
```

## 🌐 Front-end – `index.html`

Este arquivo cria a interface do usuário com o formulário para inserir os dados do imóvel:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Decisor de Imóveis em Leilão 🏠</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <div class="container">
    <h1>🏠 Decisor de Imóveis em Leilão</h1>
    <form method="POST">
      <label>Endereço do imóvel:</label>
      <input type="text" name="endereco" required><br>

      <label>Valor de mercado (R$):</label>
      <input type="number" name="valor_mercado" step="0.01" required><br>

      <label>Valor de leilão (R$):</label>
      <input type="number" name="valor_leilao" step="0.01" required><br>

      <label>Oferta planejada (R$):</label>
      <input type="number" name="oferta" step="0.01" required><br>

      <label>Aluguel estimado (R$/mês):</label>
      <input type="number" name="aluguel" step="0.01"><br>

      <button type="submit">Simular</button>
    </form>

    {% if resultado %}
      <div class="resultado">
        <h2>Resultado da análise:</h2>
        <p><strong>Recomendação:</strong> {{ resultado.recomendacao }}</p>
        <p><strong>Máx. oferta aceitável:</strong> R$ {{ "%.2f"|format(resultado.max_oferta_calculada) }}</p>
        <p><strong>Total de débitos:</strong> R$ {{ "%.2f"|format(resultado.debitos_total) }}</p>
        <p><strong>Custos extras:</strong> R$ {{ "%.2f"|format(resultado.extras_total) }}</p>
        {% if resultado.retorno_anual_percent %}
          <p><strong>Retorno anual via aluguel:</strong> {{ "%.2f"|format(resultado.retorno_anual_percent*100) }}%</p>
        {% endif %}
        <h3>Justificativas:</h3>
        <ul>
          {% for j in resultado.justificativas %}
            <li>{{ j }}</li>
          {% endfor %}
        </ul>
      </div>
    {% endif %}
  </div>
</body>
</html>
```
## 🎨 CSS – style.css

Arquivo de estilo para deixar a página mais bonita e organizada:
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

input, button {
    padding: 10px;
    margin: 5px 0;
    width: 100%;
}

button {
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #45a049;
}

.resultado {
    margin-top: 20px;
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #e7f3fe;
}
```

## 🚀 Como testar o projeto

Siga este passo a passo para testar a aplicação localmente:

# 1️⃣ Baixar o projeto
Você pode baixar o projeto como ZIP pelo GitHub ou clonar o repositório:

# Clonando via Git
```bash
git clone https://github.com/patrickanddrade/decisor-leilao.git
cd decisor-leilao
```
# 2️⃣ Criar e ativar ambiente virtual (opcional, mas recomendado)
```python
# Windows
python -m venv venv
venv\Scripts\activate
```
# Mac/Linux
```python
python3 -m venv venv
source venv/bin/activate
```
# 3️⃣ Instalar dependências
Não há requirements.txt. Certifique-se de ter o Flask instalado:
```
pip install flask
```
# 4️⃣ Rodar a aplicação
```python
python app.py
```
# 5️⃣ Abrir no navegador
Abra o navegador e acesse:

```
http://127.0.0.1:5000/
```
# 6️⃣ Teste de exemplo
Preencha o formulário com valores fictícios para testar:

Endereço: Rua das Palmeiras, 321 – Centro 🏠
```txt
Valor de mercado (R$): 400000

Valor de leilão (R$): 350000

Oferta planejada (R$): 340000

Aluguel estimado (R$/mês): 2500
```

**Clique em Simular e veja o resultado aparecer na tela! ✅**

## 📊 Como interpretar os resultados

Após preencher o formulário e clicar em **Simular**, você verá a análise do imóvel:

- **Recomendação:** 💡  
  Indica se o imóvel é uma boa compra ou se precisa de mais investigação.

- **Máx. oferta aceitável (R$):** 💰  
  Valor máximo que você deveria oferecer pelo imóvel para que seja um bom negócio.

- **Total de débitos (R$):** 🏦  
  Soma de possíveis débitos ou pendências do imóvel.

- **Custos extras (R$):** ⚙️  
  Custos adicionais como reformas, impostos ou taxas.

- **Retorno anual via aluguel (%):** 📈  
  Percentual de retorno anual caso alugue o imóvel.

- **Justificativas:** 📝  
  Lista detalhada explicando os cálculos e decisões da recomendação.

### Exemplo de resultado:

Recomendação: Comprar
Máx. oferta aceitável: R$ 382500.00
Total de débitos: R$ 0.00
Custos extras: R$ 17500.00
Retorno anual via aluguel: 8.57%
Justificativas:

Máx. oferta aceitável (382500.00) >= oferta planejada (340000.00)


Isso ajuda o usuário a entender **por que a recomendação foi dada** e tomar decisões mais informadas. 

## 🎯 Conclusão

Este projeto 🏠💻 é uma ferramenta prática para ajudar investidores a **tomarem decisões mais seguras em leilões de imóveis**.  
Com ele, você consegue estimar a **máxima oferta aceitável**, analisar débitos e custos extras, e calcular o **retorno via aluguel**.  

Mesmo sendo simples, o projeto fornece **insights valiosos** para quem quer investir com mais segurança e confiança. ✅

---

## 🙌 Créditos

- Desenvolvedor: **Patrick Andrade** 👨‍💻  
- Linguagem: Python 🐍  
- Framework Web: Flask 🌐  
- Front-end: HTML + CSS 🎨  

---

## 💡 Observações finais

- Este projeto é **educacional e experimental**.  
- Os cálculos são **estimativas** e não substituem uma análise completa do imóvel.  
- Fique à vontade para **modificar, testar e melhorar**! 🚀

---

Obrigado por testar o projeto! 😄🏠  
Esperamos que ele ajude você a tomar **melhores decisões em leilões**. 🎉

