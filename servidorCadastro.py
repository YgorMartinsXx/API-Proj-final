from flask import Flask, request, jsonify
import os
import modelCadastros as model

app = Flask(__name__)

@app.route("/fornecedores", methods=["GET"])
def consulta_fornecedores():
    try:
        fornecedores = model.todosFornecedores()
        return jsonify(fornecedores), 200
    except model.NadaCadastrado:
        return jsonify({"ERRO": "Não há nada cadastrado"}), 404

@app.route("/usuarios", methods=["GET"])
def consulta_usuarios():
    try:
        usuarios = model.todosUsuarios()
        return jsonify(usuarios), 200
    except model.NadaCadastrado:
        return jsonify({"ERRO": "Não há nada cadastrado"}), 404

@app.route("/usuarios/login", methods=["POST"])
def login_usuario():
    try:
        dados = request.json  # Obtém o JSON do corpo da requisição
        login = dados.get("login")
        senha = dados.get("senha")

        if not login or not senha:
            return jsonify({"ERRO": "Login e senha são obrigatórios"}), 400

        if model.loginUsuario(login, senha):
            return jsonify({"mensagem": "Login válido"}), 200
        else:
            return jsonify({"mensagem": "Login ou senha inválidos"}), 401
    except Exception as e:
        return jsonify({"ERRO": f"Erro no servidor: {str(e)}"}), 500
    

@app.route("/fornecedores/login", methods=["POST"])
def login_fornecedores():
    try:
        dados = request.json  # Obtém o JSON do corpo da requisição
        login = dados.get("login")
        senha = dados.get("senha")

        if not login or not senha:
            return jsonify({"ERRO": "Login e senha são obrigatórios"}), 400

        if model.loginFornecedor(login, senha):
            return jsonify({"mensagem": "Login válido"}), 200
        else:
            return jsonify({"mensagem": "Login ou senha inválidos"}), 401
    except Exception as e:
        return jsonify({"ERRO": f"Erro no servidor: {str(e)}"}), 500







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000 )))