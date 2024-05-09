import allure

from api_tools.base_request import BaseRequest

BASE_URL_JOKE_API = 'https://v2.jokeapi.dev'


class JokeAPI(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_JOKE_API)

    @allure.step("Отправляю запрос на получение общей информации об API")
    def get_info(self):
        response = self.get("info")
        return response

    @allure.step("Отправляю запрос на получение шутки")
    def get_joke(self, categories=[], resp_format: str = "json", **kwargs):
        req = "joke"
        if len(categories):
            req += f"/{','.join(categories)}"
        else:
            req += "/Any"
        req += f"?format={resp_format}"
        if kwargs.get("blacklist_flags"):
            req += f"&blacklistFlags={','.join(kwargs.get('blacklist_flags'))}"
        if kwargs.get("joke_type"):
            req += f"&type={kwargs.get('joke_type')}"
        if kwargs.get("contains"):
            req += f"&contains={kwargs.get('contains')}"
        if kwargs.get("id"):
            req += f"&idRange=={kwargs.get('id')[0]}-{kwargs.get('id')[1]}"
        if kwargs.get("amount"):
            req += f"&amount={kwargs.get('amount')}"
        if kwargs.get("lang"):
            req += f"&lang={kwargs.get('lang')}"
        if kwargs.get("safe-mode"):
            req += f"&safe-mode"
        response = self.get(req)
        return response

    @allure.step("Отправляю запрос на публикацию шутки")
    def submit_joke(self, category, joke, flags: dict, lang="en", expected_error=False):
        data = {'formatVersion': 3,
                'category': category
                }
        if type(joke) == list:
            data['type'] = "twopart"
            data['setup'] = joke[0]
            data['delivery'] = joke[1]
        else:
            data['type'] = "single"
            data['joke'] = joke
        data['flags'] = flags
        data['lang'] = lang
        response = self.post(data, endpoint="submit?dry-run", is_json=True, expected_error=expected_error)
        return response
