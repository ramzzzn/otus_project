# Установка базового образа
FROM python:3.12-alpine

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Запуск тестов
ENTRYPOINT ["pytest"]
