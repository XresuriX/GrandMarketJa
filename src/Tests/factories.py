import pytest
from django.db.models import Model
import factory
from factory.django import DjangoModelFactory
from faker import Faker
from decimal import Decimal as D
from apps.partner.models import Partner, PartnerGroup


from oscar.core.loading import get_model
from oscar.test.factories import ProductFactory, CategoryFactory, OptionFactory, PartnerFactory
from oscar.core.compat import AUTH_USER_MODEL

fake = Faker()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = AUTH_USER_MODEL

    email = "a@a.com"
    first_name = "tester"
    password = "tester"
    is_active = "True"
    is_staff = "True"

class PartnersFactory(DjangoModelFactory):
    name = factory.LazyAttribute(lambda _: fake.name())
    image = factory.LazyAttribute(lambda _: fake.file_name(category='image'))
    primary_delivery_location = factory.LazyAttribute(lambda _: fake.address())
    secondary_delivery_location = factory.LazyAttribute(lambda _: fake.address())
    contact_number = factory.LazyAttribute(lambda _: fake.phone_number())

    class Meta:
        model = Partner

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return

        # Create a new user using the UserFactory
        user = UserFactory.create()

        # Add the newly created user to the partner's users field
        self.users.add(user)


    

"""
class StallStockFactory(DjangoModelFactory):
    owner = factory.SubFactory(Stall)
    product = factory.SubFactory(ProductFactory)
    price_currency = 'JMD'
    price = D('12000.99') 
    num_in_stock = factory.LazyAttribute(lambda _: fake.random_int())
    num_allocated = factory.LazyAttribute(lambda _: fake.random_int())
    low_stock_threshold = '5'
    date_created = factory.LazyAttribute(lambda _: fake.date())
    date_updated = factory.LazyAttribute(lambda _: fake.date())
    
    class Meta:
        model = StallStock

        owner = factory.SubFactory(UserFactory)
    code = factory.LazyAttribute(lambda _: fake.slug())
    category = factory.SubFactory(CategoryFactory)

from oscar.apps.catalogue.abstract_models import *
class AttributeOptionGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractAttributeOptionGroup

    name = factory.LazyAttribute(lambda _: fake.name())
class Meta:
        model = Partner
    
    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.users.add(user)
                self.admin_users.add(user)

class AttributeOptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractAttributeOption

    group = factory.SubFactory(AttributeOptionGroupFactory)


class OptionsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractOption

    name = factory.LazyAttribute(lambda _: fake.name())
    code = factory.LazyAttribute(lambda _: fake.name())
    type = factory.LazyAttribute(lambda _: fake.random_choices(elements=('Text', 'Integer', 'Boolean', 'Float', 'Richtext', 'Date', 'Datetime', 'Option', 'Multi_Option', 'Entity', 'File', 'Image')))
    required = factory.LazyAttribute(lambda _: fake.boolean())
    option_group = factory.SubFactory(AttributeOptionGroupFactory)
    help_text = factory.LazyAttribute(lambda _: fake.paragraph())
    order = 


class ProductClassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractProductClass

    name = factory.LazyAttribute(lambda _: fake.name())
    slug = factory.LazyAttribute(lambda _: fake.name())
    requires_shipping = factory.LazyAttribute(lambda _: fake.boolean())
    track_stock = factory.LazyAttribute(lambda _: fake.boolean())
    options = factory.SubFactory(OptionsFactory)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractCategory

    name = factory.LazyAttribute(lambda _: fake.name())
    description = factory.LazyAttribute(lambda _: fake.paragraphs())
    meta_title = factory.LazyAttribute(lambda _: fake.name())
    meta_description = factory.LazyAttribute(lambda _: fake.paragraphs())
    image = factory.LazyAttribute(lambda _: fake.file_name(category='image'))
    slug = name
    is_public = True
    ancestors_are_public = True

class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractProductAttribute

    product_class = factory.SubFactory(ProductClassFactory)
    name = factory.LazyAttribute(lambda _: fake.name())
    code = factory.LazyAttribute(lambda _: fake.slug('name'))
    type = factory.LazyAttribute(lambda _: fake.random_choices(elements=('Text', 'Integer', 'Boolean', 'Float', 'Richtext', 'Date', 'Datetime', 'Option', 'Multi_Option', 'Entity', 'File', 'Image')))
    option_group = factory.SubFactory(AttributeOptionGroupFactory)
    required = factory.LazyAttribute(lambda _: fake.boolean())

class ProductCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractProductCategory

    product = factory.RelatedFactory(ProductFactory)
    category = factory.SubFactory(CategoryFactory)

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractProduct

    structure = factory.LazyAttribute(lambda _: fake.random_choices(elements=('standlone', 'parent', 'child')))
    is_public = factory.LazyAttribute(lambda _: fake.boolean())
    upc = factory.LazyAttribute(lambda _: fake.upc_a())
    parent = factory.RelatedFactory(ProductCategoryFactory)
    title = factory.LazyAttribute(lambda _: fake.name())
    slug = factory.LazyAttribute(lambda _: fake.slug())
    description = factory.LazyAttribute(lambda _: fake.paragraphs())
    meta_title = factory.LazyAttribute(lambda _: fake.name())
    meta_description = factory.LazyAttribute(lambda _: fake.paragraphs())
    product_class = factory.SubFactory(ProductClassFactory)
    attributes = factory.SubFactory(ProductAttributeFactory)
    product_options = factory.SubFactory(OptionsFactory)
    recommended_products = factory.RelatedFactory(ProductFactory)
    rating = factory.LazyAttribute(lambda _: fake.random_int())
    date_created = factory.LazyAttribute(lambda _: fake.date())
    date_updated = factory.LazyAttribute(lambda _: fake.date())
    categories = factory.SubFactory(CategoryFactory)
    is_discountable = factory.LazyAttribute(lambda _: fake.boolean())




class ProductRecommendationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractProductRecommendation

    primary = factory.SubFactory(ProductFactory)
    recommendation = factory.SubFactory(ProductFactory)
    ranking = factory.LazyAttribute(lambda _: fake.random_int())


class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractProductAttributeValue

    attribute = factory.SubFactory(ProductAttributeFactory)
    product = factory.SubFactory(ProductFactory)
    value_text = factory.LazyAttribute(lambda _: fake.text())
    value_integer = factory.LazyAttribute(lambda _: fake.random_int())
    value_boolean = factory.LazyAttribute(lambda _: fake.boolean())
    value_richtext = factory.LazyAttribute(lambda _: fake.text())    
    value_datetime = factory.LazyAttribute(lambda _: fake.date())
    value_multi_option = factory.SubFactory(AttributeOptionFactory)
    value_option = factory.SubFactory(AttributeOptionFactory)
    value_file = factory.LazyAttribute(lambda _: fake.file_name())
    value_image = factory.LazyAttribute(lambda _: fake.file_name(category='image'))
    entity_object_id = factory.LazyAttribute(lambda _: fake.random_int())

class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractProductImage

    product = factory.SubFactory(AttributeOptionGroupFactory)
    original = factory.LazyAttribute(lambda _: fake.file_name(category='image'))
    display_order = factory.LazyAttribute(lambda _: fake.random_int())
    date_created = factory.LazyAttribute(lambda _: fake.date())





class StoreAddressFactory(factory.django.DjangoModelFactory):
    country = factory.SubFactory()

    class Meta:
        model = get_model('stores', 'StoreAddress')
"""