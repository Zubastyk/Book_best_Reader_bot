from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


# фильтр проверяет callback_data у объекта CallbackQuery на то, что он состоит из цифр
class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.isdigit()

# фильтр ловит callback_data от кнопок-закладок, которые нужно удалить в режиме редактирования закладок
class IsDelBookmarksCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.endswith('del') and callback.data[:-3].isdigit()
