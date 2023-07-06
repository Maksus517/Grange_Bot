import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from config_data import load_config, Config
from handlers import router_ch, router_ih, router_ah, router_sh, router_dl, router_ai, router_ar_gm
from keyboards import set_main_menu
from data import load_data


logger = logging.getLogger(__name__)
redis: Redis = Redis(host='localhost')
storage: RedisStorage = RedisStorage(redis=redis)


async def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    load_data.select_users_data()

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    dp.include_router(router_ah)
    dp.include_router(router_ch)
    dp.include_router(router_ih)
    dp.include_router(router_sh)
    dp.include_router(router_dl)
    dp.include_router(router_ar_gm)
    dp.include_router(router_ai)

    await bot.send_message(chat_id=int(*config.tg_bot.admin_ids), text='Я перезагрузилсо!')
    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
