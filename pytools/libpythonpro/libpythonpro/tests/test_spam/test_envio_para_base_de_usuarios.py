import pytest

from pytools.libpythonpro.libpythonpro.spam.main import EnviadorDeSpam
from pytools.libpythonpro.libpythonpro.spam.modelos import Usuario
from pytools.libpythonpro.libpythonpro.spam.test_enviador_de_email import Enviador


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome="Luiz", email="luizibrahim@yahoo.com.br"),
            Usuario(nome="Carlos", email="luizibrahim@yahoo.com.br")
        ],
        [
            Usuario(nome="Luiz", email="luizibrahim@yahoo.com.br")
        ]
    ]
)
def test_qte_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luizibrahim@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados
