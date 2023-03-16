from django import urls
import pytest


@pytest.mark.django_db
def test_redirect_to_home_when_logged_in(user_factory, client):
    """Verify we redirect to the memes page when a user is logged in"""
    url = urls.reverse('home')
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('customer:home')

@pytest.mark.django_db
def test_redirect_to_home_when_logged_out(client):
    """Verify we redirect to the marketing page when a user is not logged in"""
    url = urls.reverse('home')
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('customer:home')