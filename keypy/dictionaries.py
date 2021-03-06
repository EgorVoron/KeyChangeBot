rus2eng_letters = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y',
    'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']',
    'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h',
    'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z',
    'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm',
    'б': ',', 'ю': '.', ':': '^'
}

eng2rus_letters = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н',
    'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
    'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р',
    'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э', 'z': 'я',
    'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',
    ',': 'б', '.': 'ю', '/': '.', '?': ',', '&': '?', '^': ':'
}

arm2eng_letters = {
    '՝': '`', '՜': '~', 'Ձ': '#', 'ձ': '2', 'յ': '3', 'օ': '0', 'Օ': ')', 'ռ': '-', 'Ռ': '_', 'ժ': '=', 'Ժ': '+',
    'Խ': 'q', 'խ': 'Q', 'ւ': 'w', 'Ւ': 'W', 'Է': 'E', 'է': 'e', 'Ր': 'R', 'ր': 'r', 'Տ': 'T', 'տ': 't', 'Ե': 'Y',
    'ե': 'y', 'Ը': 'U', 'ը': 'u', 'Ի': 'I', 'ի': 'i', 'Ո': 'O', 'ո': 'o', 'Պ': 'P', 'պ': 'p', 'Չ': '{', 'չ': '[',
    'Ջ': '}', 'ջ': ']', '՞': '|', "'": '\\', 'Ա': 'A', 'ա': 'a', 'Ս': 'S', 'ս': 's', 'Դ': 'D', 'դ': 'd', 'Ֆ': 'F',
    'ֆ': 'f', 'Ք': 'G', 'ք': 'g', 'Հ': 'H', 'հ': 'h', 'Ճ': 'J', 'ճ': 'j', 'Կ': 'K', 'կ': 'k', 'Լ': 'L', 'լ': 'l',
    'Թ': ':', 'թ': ';', 'Փ': '"', 'փ': "'", 'Զ': 'Z', 'զ': 'z', 'Ց': 'X', 'ց': 'x', 'Գ': 'C', 'գ': 'c', 'Վ': 'V',
    'վ': 'v', 'Բ': 'B', 'բ': 'b', 'Ն': 'N', 'ն': 'n', 'Մ': 'M', 'մ': 'm', 'Շ': '<', 'շ': ',', 'Ղ': '>', 'ղ': '.',
    'Ծ': '?', 'ծ': '/'
}

eng2arm_letters = {
    '`': '՝', '~': '՜', '#': 'Ձ', '2': 'ձ', '3': 'յ', '0': 'օ', ')': 'Օ', '-': 'ռ', '_': 'Ռ', '=': 'ժ',
    '+': 'Ժ', 'q': 'Խ', 'Q': 'խ', 'w': 'ւ', 'W': 'Ւ', 'E': 'Է', 'e': 'է', 'R': 'Ր', 'r': 'ր', 'T': 'Տ',
    't': 'տ', 'Y': 'Ե', 'y': 'ե', 'U': 'Ը', 'u': 'ը', 'I': 'Ի', 'i': 'ի', 'O': 'Ո', 'o': 'ո', 'P': 'Պ',
    'p': 'պ', '{': 'Չ', '[': 'չ', '}': 'Ջ', ']': 'ջ', '|': '՞', '\\': "'", 'A': 'Ա', 'a': 'ա', 'S': 'Ս',
    's': 'ս', 'D': 'Դ', 'd': 'դ', 'F': 'Ֆ', 'f': 'ֆ', 'G': 'Ք', 'g': 'ք', 'H': 'Հ', 'h': 'հ', 'J': 'Ճ',
    'j': 'ճ', 'K': 'Կ', 'k': 'կ', 'L': 'Լ', 'l': 'լ', ':': 'Թ', ';': 'թ', '"': 'Փ', "'": 'փ', 'Z': 'Զ',
    'z': 'զ', 'X': 'Ց', 'x': 'ց', 'C': 'Գ', 'c': 'գ', 'V': 'Վ', 'v': 'վ', 'B': 'Բ', 'b': 'բ', 'N': 'Ն',
    'n': 'ն', 'M': 'Մ', 'm': 'մ', '<': 'Շ', ',': 'շ', '>': 'Ղ', '.': 'ղ', '?': 'Ծ', '/': 'ծ'
}

arm2rus_letters = {
    'Խ': 'й', 'ւ': 'ц', 'է': 'у', 'ր': 'к', 'տ': 'е', 'ե': 'н', 'ը': 'г', 'ի': 'ш', 'ո': 'щ', 'պ': 'з', 'չ': 'х',
    'ջ': 'ъ', 'ա': 'ф', 'ս': 'ы', 'դ': 'в', 'ֆ': 'а', 'ք': 'п', 'հ': 'р', 'ճ': 'о', 'կ': 'л', 'լ': 'д', 'թ': 'ж',
    'փ': 'э', 'զ': 'я', 'ց': 'ч', 'գ': 'с', 'վ': 'м', 'բ': 'и', 'ն': 'т', 'մ': 'ь', 'շ': 'б', 'ղ': 'ю', 'Ծ': ',',
    'ծ': '.'
}

rus2arm_letters = {
    'й': 'Խ', 'ц': 'ւ', 'у': 'է', 'к': 'ր', 'е': 'տ', 'н': 'ե', 'г': 'ը', 'ш': 'ի', 'щ': 'ո', 'з': 'պ',
    'х': 'չ', 'ъ': 'ջ', 'ф': 'ա', 'ы': 'ս', 'в': 'դ', 'а': 'ֆ', 'п': 'ք', 'р': 'հ', 'о': 'ճ', 'л': 'կ',
    'д': 'լ', 'ж': 'թ', 'э': 'փ', 'я': 'զ', 'ч': 'ց', 'с': 'գ', 'м': 'վ', 'и': 'բ', 'т': 'ն', 'ь': 'մ',
    'б': 'շ', 'ю': 'ղ', ',': 'Ծ', '.': 'ծ'
}
