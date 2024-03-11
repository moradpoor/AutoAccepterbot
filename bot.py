from aiogram import Bot , Router ,filters , Dispatcher
from aiogram.types import Message, ChatJoinRequest
from aiogram.enums import ParseMode
import asyncio
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

TOEKN = '6603511266:AAGEPXZmMC0frgU-GNopqWJBEdAryKSi0js'


START_TEXT = '''
<b>
سلام {}
به ربات تایید خودکار عضویت خوش اومدی</b>

کافیه ربات رو توی کانالت ادمین تا تمامی درخواست های عضویت رو خودکار تایید کنه

'''

APROVE_TEXT = ''''
کاربر عزیز {} سلام 
در خواست عضویت شما در کانال <b>{}</b> تایید شده است 

<a href="https://t.me/c/{}/9999"> ورود به کانال </a>

'''

bot = Bot(TOEKN)
dp = Dispatcher()
my_router = Router(name=__name__)
dp.include_router(my_router)


@my_router.message(filters.CommandStart())
async def start_message_handler(message: Message):
    await message.reply(
        START_TEXT.format(message.chat.first_name),
        quote=True,parse_mode=ParseMode.HTML
    )

@my_router.chat_join_request()
async def chat_join_request_handler(message : ChatJoinRequest) :
    await message.approve()
    await bot.send_message(
        message.from_user.id,
        APROVE_TEXT.format(
            message.from_user.first_name,
            message.chat.title,
            str(message.chat.id).replace('-100','')
        ),parse_mode=ParseMode.HTML
    )

async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)

asyncio.run(main())