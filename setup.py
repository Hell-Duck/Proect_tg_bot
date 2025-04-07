from setuptools import setup, find_packages

setup(
    name="tictactoe_bot",  # Название пакета
    version="0.1",  # Версия
    description="Telegram-бот для игры в крестики-нолики",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="pashabezk",  # Ваше имя или ник
    author_email="your-email@example.com",  # Опционально
    url="https://github.com/your-username/tictactoe-bot",  # Ссылка на репозиторий
    packages=find_packages(),  # Автоматически находит все пакеты
    install_requires=[
        "python-telegram-bot>=20.0",  # Зависимости
    ],
    python_requires=">=3.7",  # Минимальная версия Python
    entry_points={
        "console_scripts": [
            "tictactoe-bot=main:main",  # Команда для запуска из терминала
        ],
    },
)
