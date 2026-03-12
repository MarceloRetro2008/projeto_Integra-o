# Arquivo principal da aplicação 
from flask import Flask

# =========================
# REGISTRAR ROTAS
# =========================

def registrar_rotas(app):

 
    from controllers.aluno_controller import AlunoController
    from controllers.professor_controller import ProfessorController
    from controllers.escola_controller import EscolaController

    aluno = AlunoController()
    professor = ProfessorController()
    escola = EscolaController()

    # =========================
    # ROTAS DE ALUNOS
    # =========================

    app.add_url_rule('/alunos', view_func=aluno.index, methods=['GET'])
    app.add_url_rule('/alunos/create', view_func=aluno.create, methods=['GET'])
    app.add_url_rule('/alunos/store', view_func=aluno.store, methods=['POST'])
    app.add_url_rule('/alunos/<int:id>', view_func=aluno.show, methods=['GET'])
    app.add_url_rule('/alunos/<int:id>/edit', view_func=aluno.edit, methods=['GET'])
    app.add_url_rule('/alunos/<int:id>/update', view_func=aluno.update, methods=['PUT'])
    app.add_url_rule('/alunos/<int:id>/delete', view_func=aluno.destroy, methods=['DELETE'])

    app.add_url_rule('/api/alunos', view_func=aluno.listar, methods=['GET'])
    app.add_url_rule('/api/alunos/<int:id>', view_func=aluno.buscar, methods=['GET'])

    # =========================
    # ROTAS DE PROFESSORES
    # =========================

    app.add_url_rule('/professores', view_func=professor.index, methods=['GET'])
    app.add_url_rule('/professores/create', view_func=professor.create, methods=['GET'])
    app.add_url_rule('/professores/store', view_func=professor.store, methods=['POST'])
    app.add_url_rule('/professores/<int:id>', view_func=professor.show, methods=['GET'])
    app.add_url_rule('/professores/<int:id>/edit', view_func=professor.edit, methods=['GET'])
    app.add_url_rule('/professores/<int:id>/update', view_func=professor.update, methods=['PUT'])
    app.add_url_rule('/professores/<int:id>/delete', view_func=professor.destroy, methods=['DELETE'])

    app.add_url_rule('/api/professores', view_func=professor.listar, methods=['GET'])
    app.add_url_rule('/api/professores/<int:id>', view_func=professor.buscar, methods=['GET'])

    # =========================
    # ROTAS DE ESCOLAS
    # =========================

    app.add_url_rule('/escolas', view_func=escola.index, methods=['GET'])
    app.add_url_rule('/escolas/create', view_func=escola.create, methods=['GET'])
    app.add_url_rule('/escolas/store', view_func=escola.store, methods=['POST'])
    app.add_url_rule('/escolas/<int:id>', view_func=escola.show, methods=['GET'])
    app.add_url_rule('/escolas/<int:id>/edit', view_func=escola.edit, methods=['GET'])
    app.add_url_rule('/escolas/<int:id>/update', view_func=escola.update, methods=['PUT'])
    app.add_url_rule('/escolas/<int:id>/delete', view_func=escola.destroy, methods=['DELETE'])

    app.add_url_rule('/api/escolas', view_func=escola.listar, methods=['GET'])
    app.add_url_rule('/api/escolas/<int:id>', view_func=escola.buscar, methods=['GET'])


# =========================
# CRIAR A APLICAÇÃO
# =========================

def create_app():

    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['JSON_SORT_KEYS'] = False

    registrar_rotas(app)

    return app


# =========================
# INICIAR SERVIDOR
# =========================

app = create_app()

if __name__ == "__main__":
    app.run()
