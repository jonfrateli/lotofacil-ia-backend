from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pandas as pd
import random

app = Flask(__name__)
CORS(app)

CSV_FILE = os.path.join(os.path.dirname(__file__), "dados_lotofacil.csv")

if os.path.exists(CSV_FILE):
    try:
        dados = pd.read_csv(CSV_FILE)
    except Exception as e:
        print(f"Erro ao carregar {CSV_FILE}: {e}")
        dados = pd.DataFrame()
else:
    print(f"Arquivo {CSV_FILE} não encontrado!")
    dados = pd.DataFrame()

@app.route("/gerar-combinacoes", methods=["POST"])
def gerar_combinacoes():
    try:
        data = request.json
        quantidade = int(data.get("quantidade", 5))
        dezenas = int(data.get("dezenas", 15))
        excluir = data.get("excluir", [])
        
        numeros = [n for n in range(1, 26) if n not in excluir]

        if len(numeros) < dezenas:
            return jsonify({"erro": "Poucos números disponíveis"}), 400

        jogos = [sorted(random.sample(numeros, dezenas)) for _ in range(quantidade)]

        return jsonify(jogos)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/")
def home():
    return "✅ Backend Lotofácil IA rodando no Render"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
