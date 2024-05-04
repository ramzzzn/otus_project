import logging
import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.service import Service as SafariService


# "https://demo-magento-2.auroracreation.com/en/"

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--base_url", action="store", default="https://magento2-b2b.magebit.com/")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--ya_driver", default="C:/otus_homeworks/homework_web/drivers/yandexdriver.exe")
    parser.addoption("--log_level", action="store", default="INFO")


def setup_logger(name: str, log_level: str) -> logging.Logger:
    # создаем папку logs, если её нет
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logger = logging.getLogger(name)
    # задаем путь, где будут храниться логи
    file_handler = logging.FileHandler(f"logs/{name}.log")
    # задаем формат логов
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    return logger


@pytest.fixture
def browser(request):
    # присваиваем полученные значения при запуске
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--base_url")
    headless = request.config.getoption("--headless")
    ya_driver = request.config.getoption("--ya_driver")
    log_level = request.config.getoption("--log_level")

    # настраиваем логирование
    logger = setup_logger(request.node.name, log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    # настраиваем веб-драйвер, согласно выбранному браузеру:
    if browser_name == "Chrome":
        service = ChromiumService()
        options = ChromiumOptions()
        if headless:
            options.add_argument("headless=new")
        _browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "Firefox":
        service = FirefoxService()
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        _browser = webdriver.Firefox(service=service, options=options)
    elif browser_name == "Edge":
        service = EdgeService()
        options = EdgeOptions()
        if headless:
            options.add_argument("headless=new")
        _browser = webdriver.Edge(service=service, options=options)
    elif browser_name == "Yandex":
        service = ChromiumService(executable_path=ya_driver)
        options = ChromiumOptions()
        if headless:
            options.add_argument("headless=new")
        _browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "Safari":
        service = SafariService()
        _browser = webdriver.Safari(service=service)

    _browser.maximize_window()
    _browser.log_level = log_level
    _browser.logger = logger
    _browser.test_name = request.node.name
    _browser.url = url

    logger.info("Browser %s started" % browser_name)

    def fin():
        _browser.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    # закрываем браузер после выполнения теста с выводом в лог
    request.addfinalizer(fin)
    return _browser
