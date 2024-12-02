# Используем официальный образ Python
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY ./src .

# Устанавливаем переменную среды для Django
ENV DJANGO_SETTINGS_MODULE=bot_admin.settings

# Создаем папку для статических файлов
RUN python manage.py collectstatic --noinput

# Открываем порт для приложения
EXPOSE 8000

# Команда для запуска приложения через gunicorn
CMD ["gunicorn", "bot_admin.wsgi:application", "--bind", "0.0.0.0:8000"]
