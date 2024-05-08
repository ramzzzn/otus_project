import allure
import pytest
from hamcrest import assert_that, equal_to, is_not, empty, is_in, contains_string


@allure.feature('API tests')
class TestJokeAPI:
    """
    test_get_info: Проверка получения общей информации об эндпоинте
    test_get_random_joke: Проверка получения случайной шутки
    test_get_joke_by_category: Проверка получения шутки с указанием категории
    test_get_joke_by_category_alias: Проверка получения шутки с указанием псевдонима категории
    test_get_joke_by_wrong_category: Проверка получения шутки с указанием некорректной категории
    test_get_joke_with_blacklist_flag: Проверка получения шутки с указанием флага черного списка
    test_get_joke_with_wrong_blacklist_flag: Проверка получения шутки с указанием некорректного флага черного списка
    test_get_joke_by_type: Проверка получения шутки с указанием типа шутки
    test_submit_joke: Проверка публикации шутки с помощью метода POST
    """

    @allure.title("Проверка получения общей информации об эндпоинте")
    def test_get_info(self, joke_api):
        result = joke_api.get_info()
        assert_that(result, is_not(empty()), 'No response was received from the server')
        assert_that(result['error'], equal_to(False), "An error was received when receiving a response from the server")

    @allure.title("Проверка получения случайной шутки")
    def test_get_random_joke(self, joke_api):
        result = joke_api.get_joke()
        assert_that(result, is_not(empty()), "No response was received from the server")
        assert_that(result['error'], equal_to(False), "An error was received when receiving a response from the server")

    @allure.title("Проверка получения шутки с указанием категории")
    @pytest.mark.parametrize('category', [['Misc'],
                                          ['Spooky', 'Programming'],
                                          ['Any', 'Misc', 'Programming', 'Dark', 'Pun', 'Spooky', 'Christmas']],
                             ids=['one_category', 'two_categories', 'all_categories'])
    def test_get_joke_by_category(self, joke_api, category):
        result = joke_api.get_joke(category)
        assert_that(result, is_not(empty()), "No response was received from the server")
        assert_that(result['error'], equal_to(False), "An error was received when receiving a response from the server")
        assert_that(result['category'], is_in(category), "Category from response does not match the specified one")

    @allure.title("Проверка получения шутки с указанием псевдонима категории")
    @pytest.mark.parametrize('category_alias, resolved_category', [(['Halloween'], ['Spooky']),
                                                                   (['Coding', 'Development'], ['Programming']),
                                                                   (['Miscellaneous', 'Coding', 'Development',
                                                                     'Halloween'],
                                                                    ['Misc', 'Programming', 'Spooky'])],
                             ids=['one_category_alias', 'two_category_aliases', 'all_category_aliases'])
    def test_get_joke_by_category_alias(self, joke_api, category_alias, resolved_category):
        """
         Отправка запроса на получение шутки с указанием псевдонима категории:
         Miscellaneous = Misc
         Coding = Programming
         Development = Programming
         Halloween = Spooky
        """
        result = joke_api.get_joke(category_alias)
        assert_that(result, is_not(empty()), "No response was received from the server")
        assert_that(result['error'], equal_to(False), "An error was received when receiving a response from the server")
        assert_that(result['category'], is_in(resolved_category), "Category from response does not match the category "
                                                                  "alias")

    @allure.title("Проверка получения шутки с указанием некорректной категории")
    @pytest.mark.parametrize('category', [['Category'],
                                          ['123456'],
                                          ['!@#$!']],
                             ids=['not_exist', 'digits', 'symbols'])
    def test_get_joke_by_wrong_category(self, joke_api, category):
        result = joke_api.get_joke(category)
        assert_that(result, is_not(empty()), "No response was received from the server")
        assert_that(result['error'], equal_to(True), "Expected error was not received from the server")
        assert_that(result['message'], equal_to("No matching joke found"))
        assert_that(result['additionalInfo'], contains_string("The specified category/ies is/are invalid."))

    @allure.title("Проверка получения шутки с указанием флага черного списка")
    @pytest.mark.parametrize('blacklist_flag', [['nsfw'],
                                                ['nsfw', 'racist'],
                                                ['nsfw', 'religious', 'political', 'racist', 'sexist', 'explicit']],
                             ids=['one_flag', 'two_flags', 'all_flags'])
    def test_get_joke_with_blacklist_flag(self, joke_api, blacklist_flag):
        result = joke_api.get_joke(blacklist_flags=blacklist_flag)
        assert_that(result, is_not(empty()), "No response was received from the server")
        assert_that(result['error'], equal_to(False), "An error was received when receiving a response from the server")
        for flag in blacklist_flag:
            assert_that(result['flags'][flag], equal_to(False), f"Got a joke with the flag {flag}= true")

    @allure.title("Проверка получения шутки с указанием некорректного флага черного списка")
    @pytest.mark.parametrize('blacklist_flag', [['test'],
                                                ['12324'],
                                                ['%%%%%']],
                             ids=['not_exist', 'digits', 'symbols'])
    def test_get_joke_with_wrong_blacklist_flag(self, joke_api, blacklist_flag):
        result = joke_api.get_joke(blacklist_flags=blacklist_flag)
        assert_that(result, is_not(empty()), "No response was received from the server")
        assert_that(result['error'], equal_to(True), "Expected error was not received from the server")
        assert_that(result['additionalInfo'], contains_string("The specified flags are invalid."))

    @allure.title("Проверка получения шутки с указанием типа шутки")
    @pytest.mark.parametrize('joke_type', ["single", "twopart"])
    def test_get_joke_by_type(self, joke_api, joke_type):
        """
        Отправка запроса на получение шутки с указанием типа шутки:
        single - шутка состоит из одной строки, которая представляет собой всю шутку.
        twopart - шутка состоит из двух частей, первая часть setup, вторая часть delivery.
        """
        result = joke_api.get_joke(joke_type=joke_type)
        assert_that(result, is_not(empty()), "No response was received from the server")
        assert_that(result['error'], equal_to(False), "An error was received when receiving a response from the server")
        assert_that(result['type'], equal_to(joke_type), "Type from response does not match the specified one")
        if result['type'] == 'single':
            assert_that(result['joke'], is_not(empty()), "The joke text is missing")
        else:
            assert_that(result['setup'], is_not(empty()), "A joke with the 'twopart' type has no setup")
            assert_that(result['delivery'], is_not(empty()), "A joke with the 'twopart' type has no delivery")

    @allure.title("Проверка публикации шутки с помощью метода POST")
    @pytest.mark.parametrize('category, joke, flags', [("Halloween", "TestJoke",
                                                        {'nsfw': True, 'religious': True, 'political': True,
                                                         'racist': True, 'sexist': True, 'explicit': True}),
                                                       ("Halloween", ["TestJokeSetup", "TestJokeDelivery"],
                                                        {'nsfw': False, 'religious': False, 'political': False,
                                                         'racist': False, 'sexist': False, 'explicit': False})
                                                       ])
    def test_submit_joke(self, joke_api, category, joke, flags):
        result = joke_api.submit_joke(category, joke, flags)
        assert_that(result['error'], equal_to(False), "An error was received when receiving a response from the server")
        assert_that(result['message'], equal_to("Dry Run complete! No errors were found."))
