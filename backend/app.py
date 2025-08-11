from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from estatisticas import gerar_combinacoes

app = Flask(__name__)
CORS(app)  # Libera o acesso para qualquer origem

# 🔑 Defina aqui a sua chave de API
API_KEY = "1530"

# Carrega o histórico real da Lotofácil
historico = pd.read_csv('dados_lotofacil.csv')

@app.route('/gerar-combinacoes', methods=['POST'])
def gerar():
    # 📌 Segurança: verifica a chave da API
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        return jsonify({"erro": "Acesso negado. Chave de API inválida."}), 403

    try:
        data = request.json
        jogos = gerar_combinacoes(
            historico=historico,
            qtd=data['quantidade'],
            dezenas=data['dezenas'],
            excluir=data.get('excluir', []),
            estrategia=data.get('estrategia', 'aleatorio')
        )
        return jsonify(jogos)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
