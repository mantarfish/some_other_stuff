class TextBuffer:
    def __init__(self):
        self.text = ""
        self.edits = []

    def append(self, edit):
        self.text += edit.text
        self.edits.append(edit)

    def undo(self):
        edit = self.edits.pop()
        self.text = self.text[0: -len(edit.text)]

class Edit:
    def __init__(self, text):
        self.text = text

a = TextBuffer()
b = Edit("hello ")

a.append(b)
print('after edit', a.text)
a.undo()
print('after undo', a.text)

print('hello')