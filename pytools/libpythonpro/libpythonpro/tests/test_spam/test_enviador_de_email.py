from pytools.libpythonpro.libpythonpro.spam.test_enviador_de_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


# @pytest.mark.parametrize(
#     'remetente',
#     ['luizibrahim@yahoo.com.br', 'foo@bar.com.br']
# )
# def test_remetente(remetente):
#     enviador = Enviador()
#     resultado = enviador.enviar(
#         remetente,
#         'lu1zibrahim94@gmail.com',
#         'Cursos Python Pro',
#         'Turma'
#     )
#     assert remetente in resultado
#

@pytest.mark.parametrize(
    'remetente',
    ['', 'foo.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'lu1zibrahim94@gmail.com',
            'Cursos Python Pro',
            'Turma'
        )
