import pytest
from django.urls import reverse
from pytest_factoryboy import register
from Tests.factories import PartnersFactory, UserFactory, ProductFactory, CategoryFactory, OptionFactory

register(UserFactory)
#register(AttributeOptionFactory)
#register(ProductAttributeFactory)
#register(ProductAttributeValueFactory)
register(ProductFactory)
register(PartnersFactory)
#register(ProductCategoryFactory)
#register(ProductClassFactory)
#register(ProductImageFactory)
#register(ProductRecommendationFactory)
#register(AttributeOptionGroupFactory)
register(CategoryFactory)
register(OptionFactory)

"""@pytest.fixture
def social_login_url():
    return '/auth_accounts/login/'

@pytest.fixture
def social_login_url():
    return reverse('socialaccount_login', args=['google'])"""

@pytest.fixture
def social_login_url_google():
    provider = 'google'  # Change this to the social login provider you want to test
    return f'/auth_accounts/{provider}/login/'

@pytest.fixture
def social_login_url_facebook():
    provider = 'facebook'  # Change this to the social login provider you want to test
    return f'/auth_accounts/{provider}/login/'

@pytest.fixture
def social_login_url_apple():
    provider = 'apple'  # Change this to the social login provider you want to test
    return f'/auth_accounts/{provider}/login/'

@pytest.fixture
def social_login_url_instagram():
    provider = 'instagram'  # Change this to the social login provider you want to test
    return f'/auth_accounts/{provider}/login/'


@pytest.mark.django_db
@pytest.fixture()
def new_user_1(db, user_factory):
    user = user_factory.create()
    return user

@pytest.mark.django_db
def new_partner_1(db, partners_factory):
    partner = partners_factory.create()
    print(partner.name)
    return partner

@pytest.mark.django_db
@pytest.fixture()
def pass_data():
    return {'first_name': 'Test', 'last_name': 'User', 'role': 'limited'}

@pytest.mark.django_db
@pytest.fixture()
def fail_data():
    return {'first_name': '', 'last_name': 'User', 'role': 'none'}