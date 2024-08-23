from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
import random



answers = ["Hello! how are you?", "Hi there!","Hey!","Howdy!","Greetings!","What’s up?"]
gritings = ["hi", "Hello", "hello","Hi","what's up","What's  up"]
router  = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name} to you")

@router.message(F.photo)
async def get_photo(message:Message):
    await message.reply("this is photo but i need some text to help you")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("i am a simple bot that can greet you")

@router.message(F.text == "Hello")
async def answer_hello(message: Message):
    await message.answer("Hello how are you?")

@router.message(F.text.in_(gritings))
async def answer_hello(message: Message):
    await message.answer(answers[random.randint(0,6)])