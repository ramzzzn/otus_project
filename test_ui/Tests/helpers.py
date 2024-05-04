import random
from faker import Faker
from datetime import datetime


def _format_timestamp():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('_%Y-%m-%d-%H-%M-%S')

    return formatted_datetime


def _generate_test_data(test_data: str, date: str):
    return test_data + date


def generate_test_customer():
    """Генерация тестовых данных для регистрации пользователя."""
    fake = Faker('ru_RU')
    return {
        'first_name': fake.first_name_male(),
        'last_name': fake.last_name_male(),
        'email': fake.free_email(),
        'password': "Testpassw0rd"
    }


def generate_test_data_company():
    """Генерация тестовых данных для регистрации компании."""
    fake = Faker('ru_RU')
    return {
        'company_name': fake.large_company(),
        'company_legal_name': fake.company(),
        'email': fake.company_email(),
        'street_address': fake.street_address(),
        'city': fake.city_name(),
        'postal_code': fake.postcode(),
        'phone': fake.phone_number(),
        'admin_email': fake.company_email(),
        'admin_first_name': fake.first_name_male(),
        'admin_last_name': fake.last_name_male()
    }


def generate_test_address():
    """Генерация тестовых данных для добавления нового адреса"""
    fake = Faker('ru_RU')
    return {
        'first_name': fake.first_name_male(),
        'last_name': fake.last_name_male(),
        'street_address': fake.street_address(),
        'city': fake.city_name(),
        'country': fake.current_country(),
        'postal_code': fake.postcode(),
        'phone': fake.phone_number()
    }


def generate_test_event():
    date = _format_timestamp()
    fake = Faker('ru_RU')
    return {
        'event': _generate_test_data('TestEvent', date),
        'message': _generate_test_data('TestMessage', date),
        'is_public': '1',
        'is_active': '1',
        'country': fake.current_country(),
        'first_name': fake.first_name_male(),
        'last_name': fake.last_name_male(),
        'email': fake.email()
    }


def generate_test_review():
    fake = Faker('ru_RU')
    return {
        'nickname': fake.user_name(),
        'summary': fake.sentence(nb_words=5),
        'review': fake.text(max_nb_chars=100)
    }


def generate_test_product():
    date = _format_timestamp()
    return {
        'product_name': _generate_test_data('TestProduct', date),
        'sku': _generate_test_data('SKU', date),
        'price': str(random.randint(10, 100))
    }


def generate_test_rule():
    date = _format_timestamp()
    return {
        'rule_name': _generate_test_data('TestRule', date),
        'customer_group': "Retailer",
        'discount': str(random.randint(1, 100))
    }
