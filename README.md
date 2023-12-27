## Приложение для Благотворительного фонда поддержки котиков QRKot

# О проекте

Приложение предоставляет возможность собирать пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.


# Установка и запуск

Клонировать репозиторий 

git clone git@github.com:SGERx/cat_charity_fund.git

Cоздать и активировать виртуальное окружение:

python3 -m venv venv

source venv/bin/activate
source venv/scripts/activate


Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt

# Используемые технологии

Python 3.9
FastAPI
SQLAlchemy 1.4
Git

# Автор

https://github.com/SGERx/

# Пример .env

APP_TITLE=Кошачий благотворительный фонд
APP_DESCRIPTION=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=<SECRET_WORD>
FIRST_SUPERUSER_EMAIL=<SUPERUSER_EMAIL>
FIRST_SUPERUSER_PASSWORD=<SUPERUSER_PASSWORD>

# Запуск миграций

Автогенерация миграций:

alembic revision --autogenerate -m "First migration"

Применение миграций:

alembic upgrade head

# Запуск приложения через uvicorn

uvicorn app.main:app --reload
