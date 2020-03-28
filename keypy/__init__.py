try:
    from keypy.translate import change_keyboard, reverse_keyboard
except ModuleNotFoundError:
    from translate import change_keyboard, reverse_keyboard

__all__ = ['change_keyboard', 'reverse_keyboard']
