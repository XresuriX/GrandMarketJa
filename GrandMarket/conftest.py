import pytest
from pytest_factoryboy import register
from Tests.factories import * 

register(UserFactory)
register(StallFactory)
register(AttributeOptionFactory)
register(ProductAttributeFactory)
register(ProductAttributeValueFactory)
register(ProductFactory)
register(ProductCategoryFactory)
register(ProductClassFactory)
register(ProductImageFactory)
register(ProductRecommendationFactory)
register(AttributeOptionGroupFactory)
register(CategoryFactory)
register(OptionsFactory)


@pytest.mark.django_db
@pytest.fixture(scope='module')
def new_user_1(db, user_factory):
    user = user_factory.create()
    return user
