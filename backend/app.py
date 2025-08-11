from flask import Flask, request, jsonify
import os
import pandas as pd
import random

app = Flask(__name__)

# Carregar dados da Lotofácil (se precisar para estratégia)
dados = pd.read_csv("dados_lotofacil.csv")

@app.route("/gerar-combinacoes", methods=["POST"])
def gerar_combinacoes():
    data = request.json
    quantidade = int(data.get("quantidade", 5))
    dezenas = int(data.get("dezenas", 15))
    excluir = data.get("excluir", [])
    estrategia = data.get("estrategia", None)

    numeros = [n for n in range(1, 26) if n not in excluir]

    jogos = []
    for _ in range(quantidade):
        jogo = sorted(random.sample(numeros, dezenas))
        jogos.append(jogo)

    return jsonify(jogos)

@app.route("/")
def home():
    return "Backend Lotofácil IA rodando ✅"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
