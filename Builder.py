class Builder():
    def __init__(self):
        self.body = ''

    def add_element(self, text: str, content: str, para: bool, **param):
        element = '<' + text
        option = [key + '=' + value for key, value in param.items()]
        if option:
            element += ' ' + ' ' .join(option)
        if para:
            element += '>' + content + '</' + text + '>'
        else:
            element += '>'
        return element

    def paragraph(self, text: str):
        self.body += self.add_element('p', text, True) + '\n'

    def title(self, text: str):
        self._title = text + '\n'

    def link(self, text: str, href: str):
        self.body += self.add_element('a', text, True, href=href) + '\n'

    def add_h(self, value: int, text: str):
        self.body += self.add_element('h' + str(value), text, True) + '\n'

    def div(self, text: str):
        self.body += self.add_element('div', text, True) + '\n'

    def img(self, href: str):
        self.body += self.add_element('img', '', False, href=href) + '\n'

    def list(self, list: list):
        self.body += self.add_element('ol', '', False)
        for i in range(len(list)):
            self.body += self.add_element('li', list[i], True)
        self.body += '</ol>' + '\n'

    def text(self, text: str):
        self.body += self.add_element('b', text, True) + '\n'

    def body(self):
        return self.body

    def render(self):
        return f'''
    <html>
        <head>
            {self.add_element('title',self._title, True)}
        </head>
        <body>
            {self.body}
            </body>
    </html>
    '''
html = Builder()
html.title("Test")
html.paragraph("First")
html.link("https://yander.ru", "Нажми")
html.div("fsdfd")
html.add_h(1, "Я студент")
html.img("https://yander.ru")
html.text("Я люблю")
html.list(["Закуски", "123"])
print(html.render())

