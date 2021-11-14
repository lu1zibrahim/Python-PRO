from unittest.mock import Mock

import pytest

from pytools.libpythonpro.libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/61382982?v=4'
    resp_mock.json.return_value = {
        'login': 'lu1zibrahim',
        'id': 61382982,
        'node_id': 'MDQ6VXNlcjYxMzgyOTgy',
        'avatar_url': url,
    }
    get_mock = mocker.patch('pytools.libpythonpro.libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('lu1zibrahim')
    assert avatar_url == url


def test_buscar_avatar_integração():
    url = github_api.buscar_avatar('lu1zibrahim')
    assert 'https://avatars.githubusercontent.com/u/61382982?v=4' == url
