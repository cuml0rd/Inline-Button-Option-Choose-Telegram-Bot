from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import buttons

TOKEN = ''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def main_menu(message: types.Message):
    await message.reply('Choose numbers', reply_markup=buttons.numbers())
    
    
@dp.callback_query_handler()
async def hello(call: types.CallbackQuery, state=FSMContext):
    print(call.data)
    data = call.data.split('|')
    if 'type' in data:
        print(data)
        number = data[1]
        current_mode = bool(int(data[2]))
        new_mode = not current_mode
        match number:
            case '1':
                await state.update_data(one_on=new_mode)
            case '2':
                await state.update_data(two_on=new_mode)
            case '3':
                await state.update_data(three_on=new_mode)
            case '4':
                await state.update_data(four_on=new_mode)
        state_data = await state.get_data()
        one_on = 'one_on' in state_data and state_data['one_on']
        two_on = 'two_on' in state_data and state_data['two_on']
        three_on = 'three_on' in state_data and state_data['three_on']
        four_on = 'four_on' in state_data and state_data['four_on']
        await call.message.edit_text(call.message.text, reply_markup=buttons.numbers(one_on, two_on, three_on, four_on))
    elif 'confirm' in data:
        state_data = await state.get_data()
        await state.finish()
        choosen_numbers = []
        for key, value in state_data.items():
            if value:
                choosen_numbers.append(key.replace('_on', ''))
        if len(choosen_numbers) == 0:
            await call.message.edit_text('You have not chosen any numbers! Select at least one.', reply_markup=buttons.numbers())
        else:
            await call.message.edit_text(f'You chose numbers: {", ".join(choosen_numbers)}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
