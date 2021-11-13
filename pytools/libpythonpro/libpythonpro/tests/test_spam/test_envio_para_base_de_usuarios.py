from unittest.mock import Mock

import pytest

from pytools.libpythonpro.libpythonpro.spam.main import EnviadorDeSpam
from pytools.libpythonpro.libpythonpro.spam.modelos import Usuario


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luizibrahim@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Luiz", email="luizibrahim@yahoo.com.br")
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'carlos@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.enviar.asser_called_once_with(
        'carlos@yahoo.com.br',
        'luizibrahim@yahoo.com.br'
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
