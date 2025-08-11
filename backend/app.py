from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import random
import os

app = Flask(__name__)
CORS(app)

# Carrega dados históricos
CSV_FILE = "dados-lotofacil.csv"
if os.path.exists(CSV_FILE):
    dados = pd.read_csv(CSV_FILE, sep=",")
else:
    dados = pd.DataFrame()

@app.route("/", methods=["POST"])
def gerar_combinacoes():
    try:
        data = request.get_json()
        quantidade = int(data.get("quantidade", 5))
        dezenas = int(data.get("dezenas", 15))
        excluir = data.get("excluir", [])
        estrategia = data.get("estrategia", "")

        # Lista de números possíveis
        todos_numeros = list(range(1, 26))
        numeros_disponiveis = [n for n in todos_numeros if n not in excluir]

        if len(numeros_disponiveis) < dezenas:
            return jsonify({"erro": "Poucos números disponíveis para gerar a combinação"}), 400

        jogos = []
        for _ in range(quantidade):
            jogo = random.sample(numeros_disponiveis, dezenas)
            jogo.sort()
            jogos.append(jogo)

        return jsonify(jogos)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

