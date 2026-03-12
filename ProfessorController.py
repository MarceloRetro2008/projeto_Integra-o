from flask import render_template, request, jsonify
from database.database import conectar


class ProfessorController:

    # =========================
    # PÁGINAS
    # =========================

    # INDEX - Página de listagem
    def index(self):
        return render_template("professores/index.html")


    # CREATE - Formulário de cadastro
    def create(self):
        return render_template("professores/create.html")


    # SHOW - Detalhes do professor
    def show(self, id):
        return render_template("professores/show.html", id=id)


    # EDIT - Formulário de edição
    def edit(self, id):
        return render_template("professores/edit.html", id=id)


    # =========================
    # CRUD
    # =========================

    # STORE - Criar professor
    def store(self):
        dados = request.get_json()

        if not dados:
            return jsonify({"erro": "Dados não enviados"}), 400

        try:
            banco = conectar()
            cursor = banco.cursor()

            sql = """
                INSERT INTO professor
                (nome, especialidade, email, telefone)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(sql, (
                dados.get("nome"),
                dados.get("especialidade"),
                dados.get("email"),
                dados.get("telefone")
            ))

            banco.commit()

            return jsonify({
                "status": "sucesso",
                "mensagem": "Professor cadastrado com sucesso"
            }), 201

        except Exception as erro:
            banco.rollback()
            return jsonify({"erro": str(erro)}), 500

        finally:
            cursor.close()
            banco.close()


    # UPDATE - Atualizar professor
    def update(self, id):
        dados = request.get_json()

        if not dados:
            return jsonify({"erro": "Dados não enviados"}), 400

        try:
            banco = conectar()
            cursor = banco.cursor()

            sql = """
                UPDATE professor
                SET nome=%s,
                    especialidade=%s,
                    email=%s,
                    telefone=%s
                WHERE id=%s
            """

            cursor.execute(sql, (
                dados.get("nome"),
                dados.get("especialidade"),
                dados.get("email"),
                dados.get("telefone"),
                id
            ))

            banco.commit()

            return jsonify({
                "status": "sucesso",
                "mensagem": "Professor atualizado com sucesso"
            })

        except Exception as erro:
            banco.rollback()
            return jsonify({"erro": str(erro)}), 500

        finally:
            cursor.close()
            banco.close()


    # DESTROY - Deletar professor
    def destroy(self, id):
        try:
            banco = conectar()
            cursor = banco.cursor()

            cursor.execute("DELETE FROM professor WHERE id=%s", (id,))
            banco.commit()

            return jsonify({
                "status": "sucesso",
                "mensagem": "Professor removido com sucesso"
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

    # API - Listar todos professores
    def listar(self):
        try:
            banco = conectar()
            cursor = banco.cursor(dictionary=True)

            cursor.execute("SELECT * FROM professor")
            professores = cursor.fetchall()

            return jsonify(professores)

        except Exception as erro:
            return jsonify({"erro": str(erro)}), 500

        finally:
            cursor.close()
            banco.close()


    # API - Buscar professor por ID
    def buscar(self, id):
        try:
            banco = conectar()
            cursor = banco.cursor(dictionary=True)

            cursor.execute("SELECT * FROM professor WHERE id=%s", (id,))
            professor = cursor.fetchone()

            if not professor:
                return jsonify({"mensagem": "Professor não encontrado"}), 404

            return jsonify(professor)

        except Exception as erro:
            return jsonify({"erro": str(erro)}), 500

        finally:
            cursor.close()
            banco.close()
