from keypy import reverse_keyboard
from config import API_TOKEN

from aiogram import Bot, Dispatcher, types, executor


def translate_string(input_string):
    result = reverse_keyboard(string=input_string, keyboard_lang_1='rus', keyboard_lang_2='eng')
    return result


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def from_group(message: types.Message):
    return 'group' in message.chat.type


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Hi!\nI am KeyChangeBot, I can change '
                        'keyboard layout from english to russian and vice versa')


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply('Send me a text, written in a wrong layout and I will fix it!')


@dp.message_handler(commands=['kc'])
async def run_from_group(message: types.Message):
    if from_group(message):
        print(message.text)
        print(message.reply_to_message)
        if message.reply_to_message:
            print(message.reply_to_message.text)
            translated = translate_string(message.reply_to_message.text)
            await message.reply(translated)


@dp.message_handler()
async def run_from_user(message: types.Message):
    print(message.text)
    translated = translate_string(message.text)
    await message.reply(translated)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
