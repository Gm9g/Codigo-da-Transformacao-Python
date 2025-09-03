from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/soma/<int:a>/<int:b>', methods=['GET'])
def soma_api(a, b):
    return jsonify({"resultado": a + b})

@app.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide_api(a, b):
    if b == 0:
        return jsonify({"erro": "Não é possível dividir por zero."}), 400
    return jsonify({"resultado": a / b})

if __name__ == '__main__':
    app.run(debug=True)
