from setuptools import setup, find_packages

setup(
    name="Practic_X_O",
    version="0.1",
    description="Telegram-бот для игры в крестики-нолики",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Yudin, Kulish",
    url="https://github.com/Hell-Duck/Proect_tg_bot",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot>=20.0",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "tg_bot=main:main",
        ],
    },
)
