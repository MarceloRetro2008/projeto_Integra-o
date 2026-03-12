from flask import render_template, request, jsonify, redirect, url_for
from database.database import conectar


class DisciplinaController:

    def index(self):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM disciplinas")
        disciplinas = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template("disciplinas/index.html", disciplinas=disciplinas)


    def create(self):
        return render_template("disciplinas/create.html")


    def store(self):
        try:
            nome = request.form.get("nome")
            carga_horaria = request.form.get("carga_horaria")
            professor = request.form.get("professor")

            conn = conectar()
            cursor = conn.cursor()

            sql = """
                INSERT INTO disciplinas (nome, carga_horaria, professor)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (nome, carga_horaria, professor))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for("disciplinas.index"))

        except Exception as e:
            return f"Erro ao salvar disciplina: {str(e)}"


    def show(self, id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM disciplinas WHERE id = %s", (id,))
        disciplina = cursor.fetchone()

        cursor.close()
        conn.close()

        return render_template("disciplinas/show.html", disciplina=disciplina)

    def edit(self, id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM disciplinas WHERE id = %s", (id,))
        disciplina = cursor.fetchone()

        cursor.close()
        conn.close()

        return render_template("disciplinas/edit.html", disciplina=disciplina)

    def update(self, id):
        try:
            nome = request.form.get("nome")
            carga_horaria = request.form.get("carga_horaria")
            professor = request.form.get("professor")

            conn = conectar()
            cursor = conn.cursor()

            sql = """
                UPDATE disciplinas
                SET nome=%s, carga_horaria=%s, professor=%s
                WHERE id=%s
            """

            cursor.execute(sql, (nome, carga_horaria, professor, id))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for("disciplinas.index"))

        except Exception as e:
            return f"Erro ao atualizar disciplina: {str(e)}"


    def destroy(self, id):
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM disciplinas WHERE id = %s", (id,))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for("disciplinas.index"))

        except Exception as e:
            return f"Erro ao excluir disciplina: {str(e)}"

    def listar(self):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM disciplinas")
        disciplinas = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(disciplinas)



    def buscar(self, id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM disciplinas WHERE id = %s", (id,))
        disciplina = cursor.fetchone()

        cursor.close()
        conn.close()

        if disciplina:
            return jsonify(disciplina)
        else:
            return jsonify({"erro": "Disciplina não encontrada"}), 404
