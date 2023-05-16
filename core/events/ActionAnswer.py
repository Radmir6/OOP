from core.base import Event, IncomingMessage
from core import Pythogram
import random


answers = ["Да", "Нет", "Наверное", "Возможно", "Скорее всего", "Определенно", "Мало вероятно", "Точно нет",
           "Даже не думай", "Никогда", "Точно", "Не могу сказать"]

class ActionAnswer(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        if text[-1] == "?":
            return text

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = answers[random.randint(0, len(answers))]
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
