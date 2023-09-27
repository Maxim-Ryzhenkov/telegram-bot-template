from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    """ Токен для доступа к телеграм-боту """
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    """ Подгрузить переменные окружения из файла .env
        Инициализировать экземпляр класса Config и вернуть его.
    """
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
