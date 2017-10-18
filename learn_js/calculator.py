import re


class Tokenizer():
    def __init__(self, program):
        self.program = program
        self.current_word = ""
        self.current_pos = 0

    def next_token(self):
        self.current_word = re.match(r"^\w+", self.program)
        return self.current_word



tok = Tokenizer("alp dd fefe 77")
print(tok.next_token())
