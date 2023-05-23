import psycopg2
from aiogram.types import Message
from config_data import load_config, Config


users_data = {}
user_id_premium: list = []


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

    async def insert_user_data(self) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO users (id_user, user_name) VALUES
                ({self.message.from_user.id},
                '{self.message.from_user.first_name}')"""
            )
        self.connection.commit()

        if self.connection:
            self.connection.close()

    async def insert_user_comment(self) -> None:
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

    def select_users_data(self) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                """SELECT id_user, user_name FROM users"""
            )
            for i in cursor.fetchall():
                users_data.setdefault(int(i[0]), {})
                users_data[i[0]].setdefault('user_name', str(i[1]))
                users_data[i[0]].setdefault('user_status', 'chat')
                users_data[i[0]].setdefault('counter', 0)
                users_data[i[0]].setdefault('message_data', None)
                users_data[i[0]].setdefault('data_list', [])
                users_data[i[0]].setdefault('games_data', None)

        if self.connection:
            self.connection.close()


load_data: DataBase = DataBase(None)
