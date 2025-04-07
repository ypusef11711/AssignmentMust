import string

char_class = None
lexeme = []
next_char = ''
lex_len = 0
token = None
next_token = None
input_string = "(sum + 457) / total"
input_index = 0

LETTER = 0
DIGIT = 1
UNKNOWN = 99

INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1

def add_char():
    global lex_len
    if lex_len <= 98:
        lexeme.append(next_char)
        lex_len += 1
    else:
        print("Error - lexeme is too long")

def get_char():
    global next_char, char_class, input_index
    if input_index < len(input_string):
        next_char = input_string[input_index]
        input_index += 1
    else:
        next_char = ''
    if next_char == '':
        char_class = EOF
    elif next_char.isalpha():
        char_class = LETTER
    elif next_char.isdigit():
        char_class = DIGIT
    else:
        char_class = UNKNOWN

def get_non_blank():
    while next_char.isspace():
        get_char()

def lookup(ch):
    global next_token
    if ch == '(':
        add_char()
        next_token = LEFT_PAREN
    elif ch == ')':
        add_char()
        next_token = RIGHT_PAREN
    elif ch == '+':
        add_char()
        next_token = ADD_OP
    elif ch == '-':
        add_char()
        next_token = SUB_OP
    elif ch == '*':
        add_char()
        next_token = MULT_OP
    elif ch == '/':
        add_char()
        next_token = DIV_OP
    else:
        add_char()
        next_token = EOF
    return next_token

def lex():
    global lex_len, next_token
    lex_len = 0
    get_non_blank()
    if char_class == LETTER:
        add_char()
        get_char()
        while char_class == LETTER or char_class == DIGIT:
            add_char()
            get_char()
        next_token = IDENT
    elif char_class == DIGIT:
        add_char()
        get_char()
        while char_class == DIGIT:
            add_char()
            get_char()
        next_token = INT_LIT
    elif char_class == UNKNOWN:
        lookup(next_char)
        get_char()
    elif char_class == EOF:
        next_token = EOF
        lexeme.extend(['E', 'O', 'F'])
    print(f"Next token is: {next_token}, Next lexeme is {''.join(lexeme)}")
    return next_token

def main():
    get_char()
    while next_token != EOF:
        lex()

if __name__ == "__main__":
    main()
