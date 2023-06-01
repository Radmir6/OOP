from core.base import Event, IncomingMessage
from core import Pythogram
import random

memes = ["https://sun21-2.userapi.com/impg/BJUpTyU8Bzv9PaDkTqEK9zxuj2vyG7f1hvYU0Q/aMzAOLmcaL0.jpg?size=592x355"
         "&quality=95&sign=adc79dfbafc5056911ddebd8781c33d0&type=album",
         "https://sun9-40.userapi.com/impg/dh6DEPf2Jl0u7EXifQNYzsWtZZMQPjANpW5D_w/NebbBr3cJII.jpg?size=512x512&quality=95&sign=dd6210a669f5907b7c5a9c0bab3be39d&type=album",
         "https://sun21-1.userapi.com/impg/7Q1poIcFQhYFhzwAxGVWNEguBasDsCLN7w0ZzA/12MJ_Iap7IE.jpg?size=236x289"
         "&quality=95&sign=3256b3edc86fe10c1aa5822612b30cd5&type=album",
         "https://sun9-33.userapi.com/impg/tTd55wLQ9W2Wo2G6FqIf3xEzliCe87mNRIuqzg/mkz2EaRUEr4.jpg?size=609x474"
         "&quality=95&sign=c4f8a8ac5e58a6c03c3fcbc5f3a08b36&type=album",
         "https://sun21-2.userapi.com/impg/Rv85ju3bSnrDM46zz3-LfSXjp5PM3BkDUMcPIw/uM082Z4WeCI.jpg?size=1080x687"
         "&quality=95&sign=04f2ef3cec148cbd9a702b2522732deb&type=album",
         "https://sun9-80.userapi.com/impg/B2Q6XWE_oumGwAAviQ7gALF7kB6KSsl_DU5nWA/ByHdcgqdKgw.jpg?size=698x391"
         "&quality=95&sign=0ff9d692fccde886a5b27e49a37da837&type=album",
         "https://sun9-26.userapi.com/impg/Hlz9MH_gZ2M8CMuZwZdYlawKefa8g6aWj04NiQ/vi_reLyNAyI.jpg?size=640x673"
         "&quality=95&sign=d628045ee4a5addbc09931534a577de9&type=album",
         "https://sun21-1.userapi.com/impg/ney7Dnw63voeqOpWECqdtBOnYte-1_59MhPYgA/PCkYUG5dIWg.jpg?size=216x320"
         "&quality=95&sign=b2a92117b31c9842761d76704a01633b&type=album",
         "https://sun9-64.userapi.com/impg/lmJbOSzIoV1IBTYkTYyNrmLQ_kBJJezDlI8uRw/xEw00CyRyqA.jpg?size=320x320"
         "&quality=95&sign=b42856ec605a987b1c08b780383a3b7c&type=album",
         "https://sun9-45.userapi.com/impg/FC9G1vgggQI7yp_8d2DWbgBUJE3kdHeh9W7Drg/RRPBnx7UnGo.jpg?size=218x231"
         "&quality=95&sign=e5367bfee06792ea1d05275ea0a62f71&type=album",
         "https://sun9-13.userapi.com/impg/4epH4MmSGxs0m9v4ey1YYff9dkeh4ZN2JX179g/S6J6n8H-Qt4.jpg?size=577x393"
         "&quality=95&sign=919753345e76f3e6af703a182451c804&type=album",
         "https://sun21-1.userapi.com/impg/i9dMdSsc3-Zg7HHKxyoMAYarutXE7GFnrBocjw/bxBOawxQfjQ.jpg?size=300x168"
         "&quality=95&sign=adb4522d25f11dc2486e8ad78a6cdc67&type=album",
         "https://sun9-15.userapi.com/impg/43DC9HTWfQ1PYdNKwDLXKDS77OkUMSsSB_RBVA/DomS2bSYkFY.jpg?size=275x183"
         "&quality=95&sign=3830a0fa59c24b62ef643205d295dbf3&type=album",
         "https://sun9-13.userapi.com/impg/H0XrjclPBwr_ohyoBM3Iq6pI1oV5Y2BKKMCt2w/3cc0KlV37oo.jpg?size=271x186"
         "&quality=95&sign=bd1fb7599209bcce91c9a94edc12f0f9&type=album"]


class ActionMeme(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['мем']

    def action(self, message: IncomingMessage, *args, **kwargs):
        self.__sender.photo.send(
            file=memes[random.randint(0, len(memes) - 1)],
            chat=message.chat
        )
