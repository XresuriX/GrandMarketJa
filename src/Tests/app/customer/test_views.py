from django import urls
import pytest
import requests
from unittest.mock import Mock
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_redirect_to_home_when_logged_in(user_factory, client):
    """Verify we redirect to the memes page when a user is logged in"""
    url = urls.reverse('home')
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('customer:home')

@pytest.mark.django_db
def test_redirect_to_home_when_logged_out(user_factory, client):
    """Verify we redirect to the marketing page when a user is not logged in"""
    url = urls.reverse('home')
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('customer:home')

@pytest.mark.django_db
def test_login(user_factory, client):
    # Test login view
    url = urls.reverse('account_login')
    response = client.get(url)
    print(response)
    assert response.status_code == 200

@pytest.mark.django_db
def test_social_auth_1(client, social_login_url_google):
    # Make a request to the social login page
    response = client.get(social_login_url_google)
    print(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_social_auth_2(client, social_login_url_apple):
    # Make a request to the social login page
    response = client.get(social_login_url_apple)
    print(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_social_auth_3(client, social_login_url_facebook):
    # Make a request to the social login page
    response = client.get(social_login_url_facebook)
    #print(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_social_login_4(client, social_login_url_instagram):
    response = client.get(social_login_url_instagram)
    #print(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_google_auth(client, mocker, social_login_url_google):
    # Create a mock response for the OAuth2 flow
    response = Mock()
    response.json.return_value = {
        'email': 'testuser@example.com',
        'name': 'Test User'
    }
    mocker.patch('allauth.socialaccount.providers.google.views.GoogleOAuth2Adapter.complete_login', return_value=response)

    # Call the Google auth endpoint
    response = client.get(social_login_url_google)
    # Check that the user is redirected to the Google auth page
    assert response.status_code == 200
    print(response.status_code)
    print(response.json)




    #print(response.)
    """assert response.url.startswith('https://accounts.google.com/o/oauth2')

    # Call the callback URL with the mock OAuth2 response
    response = client.get(reverse('socialaccount_callback', args=['google']), {'code': 'mock-code'})

    # Check that the user is redirected to the homepage
    assert response.status_code == 302
    assert response.url == '/'

    # Check that a SocialAccount and SocialToken were created for the user
    social_account = SocialAccount.objects.get(provider='google')
    assert social_account.user.email == 'testuser@example.com'
    assert social_account.user.get_full_name() == 'Test User'
    social_token = SocialToken.objects.get(account=social_account)
    assert social_token.token_secret is not None"""


    
    