from flask import render_template, request, jsonify
from database.database import conectar


class EscolaController:

    # =========================
    # PÁGINAS
    # =========================

    # INDEX - Página de listagem
    def index(self):
        return render_template("escolas/index.html")


    # CREATE - Formulário de cadastro
    def create(self):
        return render_template("escolas/create.html")


    # SHOW - Página de detalhes
    def show(self, id):
        return render_template("escolas/show.html", id=id)


    # EDIT - Formulário de edição
    def edit(self, id):
        return render_template("escolas/edit.html", id=id)


    # =========================
    # CRUD
    # =========================

    # STORE - Salvar escola
    def store(self):
        dados = request.get_json()

        if not dados:
            return jsonify({"erro": "Dados não enviados"}), 400

        try:
            banco = conectar()
            cursor = banco.cursor()

            sql = """
                INSERT INTO escola
                (nome, endereco, cidade, pais, telefone, email)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (
                dados.get("nome"),
                dados.get("endereco"),
                dados.get("cidade"),
                dados.get("pais"),
                dados.get("telefone"),
                dados.get("email")
            )

            cursor.execute(sql, valores)
            banco.commit()

            return jsonify({
                "status": "sucesso",
                "mensagem": "Escola cadastrada com sucesso"
            }), 201

        except Exception as erro:
            banco.rollback()
            return jsonify({"erro": str(erro)}), 500

        finally:
            cursor.close()
            banco.close()


    # UPDATE - Atualizar escola
    def update(self, id):
        dados = request.get_json()

        if not dados:
            return jsonify({"erro": "Dados não enviados"}), 400

        try:
            banco = conectar()
            cursor = banco.cursor()

            sql = """
                UPDATE escola
                SET nome=%s,
                    endereco=%s,
                    cidade=%s,
                    pais=%s,
                    telefone=%s,
                    email=%s
                WHERE id=%s
            """

            valores = (
                dados.get("nome"),
                dados.get("endereco"),
                dados.get("cidade"),
                dados.get("pais"),
                dados.get("telefone"),
                dados.get("email"),
                id
            )

            cursor.execute(sql, valores)
            banco.commit()

            return jsonify({
                "status": "sucesso",
                "mensagem": "Escola atualizada com sucesso"
            })

        except Exception as erro:
            banco.rollback()
            return jsonify({"erro": str(erro)}), 500

        finally:
            cursor.close()
            banco.close()


    # DESTROY - Deletar escola
    def destroy(self, id):
        try:
            banco = conectar()
            cursor = banco.cursor()

            cursor.execute("DELETE FROM escola WHERE id=%s", (id,))
            banco.commit()

            return jsonify({
                "status": "sucesso",
                "mensagem": "Escola removida com sucesso"
            })

        except Exception as erro:
            banco.rollback()
            return jsonify({"erro": str(erro)}), 500

        finally:
            cursor.close()
            banco.close()


    # =========================
    # API
    # =========================

    # LISTAR - Todas escolas
    def listar(self):
        try:
            banco = conectar()
            cursor = banco.cursor(dictionary=True)

            cursor.execute("SELECT * FROM escola")
            escolas = cursor.fetchall()

            return jsonify
