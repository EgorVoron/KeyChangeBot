from keypy import reverse_keyboard
from config import API_TOKEN

def translate(input):
    result = reverse_keyboard(string=input, keyboard_lang_1='rus', keyboard_lang_2='eng')
    return result

