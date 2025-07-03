
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/transacao/status/<int:cliente_id>')
def status(cliente_id):
    status_map = {
        1: "Aprovada",
        2: "Recusada",
        3: "Nenhuma"
    }
    return jsonify({"cliente_id": cliente_id, "status": status_map.get(cliente_id, "Desconhecido")})

app.run(debug=True, port=5000)
