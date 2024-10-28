from aiogram import F, Router, Bot, Dispatcher 
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType
from messages import MESSAGES
from config import BOT_TOKEN, item_url, PAYMENTS_TOKEN, adm_ID
import keyboards as kb 
from messages import MESSAGES
from aiogram import types


bot = Bot(BOT_TOKEN)

router = Router()




@router.message(F.poto)
async def oter(message: Message):
    await message.answer("Я не знаю что то за картинка, нвжми на кнопку ниже если хочешь начать заново", reply_markup=kb.inline_kb8)

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer_photo("AgACAgIAAxkBAAICIWKsizBqE6foEIwpw5nikgGYTrEQAALbvDEbtN9hSR6JvAgvr62SAQADAgADcwADJAQ",
							  reply_markup=kb.inline_kb1)

@router.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer(MESSAGES['help'])


@router.callback_query(F.data =="But_1")
async def send_O1(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer_photo("AgACAgIAAxkBAAICKWKsizVC77yt1R4nFvTk5Rs87FofAALfvDEbtN9hSflUfMVzbFtdAQADAgADcwADJAQ", 
									reply_markup=kb.inline_kb2)

@router.callback_query(F.data =="But_2")
async def send_2(call: types.CallbackQuery):
	await call.message.delete_reply_markup()
	await call.message.answer_photo("AgACAgIAAxkBAAICJ2KsizV4HaX0pSTja4SVMmqzoie5AALevDEbtN9hSS438sC-ZKb6AQADAgADcwADJAQ", reply_markup=kb.greet_kb1)

@router.message(F.text==("Далее"))
async def send_3(message: types.Message):
	await message.answer_photo("AgACAgIAAxkBAAICqWKst07fSm95hBM2CectcQipYfMGAALJvTEbtN9hSW3t_Bdgz7f1AQADAgADcwADJAQ",   reply_markup=kb.greet_kb2)
	await message.answer(MESSAGES["next"], reply_markup=kb.inline_kb5)
	
@router.message(F.DOCUMENT)
async def echo_document(message: Message):
	await message.reply(str(message.document.file_id))

@router.message(F.ANIMATION)
async def echo_doc(message: Message):
    await message.reply(str(message.animation.file_id))

@router.message(F.PHOTO)
async def echo_docs(message: Message):
    await message.reply(str(message.photo[-1].file_id))



@router.callback_query(F.data =="But_5")
async def send5(call: types.CallbackQuery):
	await call.message.delete_reply_markup()
	await call.message.answer("""Еще бот может двумя разными способами отправлять ссылки.  <a href="https://github.com/">		ТАК</a>""", parse_mode=ParseMode.HTML, reply_markup=kb.inline_kb_full)

@router.callback_query(F.data =="But_6")
async def send6(call: types.CallbackQuery):
	await call.message.delete_reply_markup()
	await call.message.edit_text("""Ссылка изменилась <a href="https://github.com/aiogram/aiogram">
					ТЫК</a>""", parse_mode=ParseMode.HTML)
	await call.message.answer("Бот может изменять текст ранее отправленных им сообщений", reply_markup=kb.inline_kb7)


@router.callback_query(F.data =="But_7")
async def send7(call: types.CallbackQuery):
	await call.message.delete_reply_markup()
	await call.message.answer_photo("AgACAgIAAxkBAAICnGKstdSZegUzQadS5gwIiMRxl0yHAAK9vTEbtN9hSTqfmzxH6soRAQADAgADcwADJAQ",  MESSAGES["again"],  parse_mode=ParseMode.HTML )


# Пример данных для платежей и доставки
PRICES = [
    LabeledPrice(label='Волшебная палочка', amount=100000),
    LabeledPrice(label='На корм сове', amount=10000)
]

SUPERSPEED_SHIPPING_OPTION = ShippingOption(
    id='superspeed',
    title='Супер быстрая!',
    prices=[LabeledPrice(label='Лично в руки!', amount=80000)]
)

POST_SHIPPING_OPTION = ShippingOption(
    id='post',
    title='Совиная почта',
    prices=[LabeledPrice(label='Деревянная коробка',amount= 50000),
            LabeledPrice(label='Срочное отправление!',amount= 1000)]
)

PICKUP_SHIPPING_OPTION = ShippingOption(
    id='pickup',
    title='Самовывоз',
    prices=[LabeledPrice(label='Самовывоз из Петербурга', amount=10000)]
)

# Хендлер для команды /sell
@router.message(F.text==("Посмотреть"))
async def sell_process(message: Message):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title=MESSAGES['item_title'],
        description=MESSAGES['item_description'],
        provider_token=PAYMENTS_TOKEN,  # Используем переменную PAYMENTS_TOKEN
        currency='rub',  # Валюта (например, рубли)
        photo_url=item_url,  # Ссылка на изображение товара
        photo_height=512,  # Высота фото
        photo_width=512,   # Ширина фото
        photo_size=512,    # Размер фото
        need_email=True,  # Спрашивать у пользователя email
        need_phone_number=True,  # Спрашивать у пользователя телефон
        is_flexible=True,  # Указывать, что цена и доставка могут варьироваться
        prices=PRICES,  # Цены на товары
        start_parameter='sell_goods',
        payload='sell_process_payload'  # Произвольный payload
    )

@router.shipping_query(lambda q: True)
async def shipping_process(shipping_query: ShippingQuery):
    if shipping_query.shipping_address.country_code == 'AU':
        return await bot.answer_shipping_query(
            shipping_query.id,
            ok=False,
            error_message=MESSAGES['AU_error']
        )

    shipping_options = [SUPERSPEED_SHIPPING_OPTION]

    if shipping_query.shipping_address.country_code == 'RU':
        shipping_options.append(POST_SHIPPING_OPTION)

        if shipping_query.shipping_address.city == 'Санкт-Петербург':
            shipping_options.append(PICKUP_SHIPPING_OPTION)

    await bot.answer_shipping_query(
        shipping_query.id,
        ok=True,
        shipping_options=shipping_options
    )




@router.pre_checkout_query()
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@router.message(F.content_types == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment_handler(message: Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=MESSAGES['successful_payment'].format(
            total_amount=message.successful_payment.total_amount // 100,
            currency=message.successful_payment.currency
        ),
        reply_markup=kb.inline_kb5
    )