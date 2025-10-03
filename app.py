# app.py
from flask import Flask, render_template, request
from decisor_leilao import simular_imovel

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        endereco = request.form.get("endereco")
        valor_mercado = float(request.form.get("valor_mercado", 0))
        valor_leilao = float(request.form.get("valor_leilao", 0))
        oferta = float(request.form.get("oferta", 0))
        aluguel = float(request.form.get("aluguel", 0))

        resultado = simular_imovel(valor_mercado, valor_leilao, oferta, aluguel)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
