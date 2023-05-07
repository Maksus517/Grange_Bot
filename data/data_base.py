import psycopg2
from aiogram.types import Message
from config_data import load_config, Config

users_data: dict[int, dict[str, str | int | bool | None]] = {}
user_joke: dict[int, list] = {}


class DataBase:
    def __init__(self, message: Message | None) -> None:
        self.message: Message = message
        self.config: Config = load_config()
        self.connection = psycopg2.connect(
            host=self.config.data_base.host,
            user=self.config.data_base.user,
            password=self.config.data_base.password,
            database=self.config.data_base.db_name
        )

    def insert_user_data(self) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO users (id_user, user_name, user_premium) VALUES
                ({self.message.from_user.id},
                '{self.message.from_user.first_name}',
                'False')"""
            )
        self.connection.commit()

        if self.connection:
            self.connection.close()

    def insert_user_comment(self) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO comment (id_user, user_name, comment) VALUES
                ({self.message.from_user.id},
                '{self.message.from_user.first_name}',
                '{self.message.text}')"""
            )
        self.connection.commit()

        if self.connection:
            self.connection.close()

    def select_uses_data(self) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                """SELECT id_user, user_name, user_premium FROM users"""
            )
            for i in cursor.fetchall():
                users_data.setdefault(int(i[0]), {})
                users_data[i[0]].setdefault('user_name', str(i[1]))
                users_data[i[0]].setdefault('user_status', None)
                users_data[i[0]].setdefault('user_premium', bool(i[2]))

        if self.connection:
            self.connection.close()


load_data: DataBase = DataBase(None)
