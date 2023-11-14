import sys
from detectors import is_a_println
from runners._io import println
import re

argv = sys.argv

if len(argv) < 2:
    print(
        "Error: Please enter the slow-laggy "
        f"programm file.\nexmaple: {argv[0]} test.sl"
)
    exit()

file_name = argv[1]


###########################
# tokenizing prgram code  #
###########################
tokens: list[str] = []
with open(file_name) as program_file:

    for token in program_file:
        if re.match(r"\S+", token):
            token and tokens.append(token.strip())


#####################
# Parse the Tokens! #
#####################
ast: list[dict[str, str]] = []
for token in filter(lambda line: not line.startswith("`"), tokens):
    keyword = token.split(" ", 1)

    if is_a_println(keyword[0]):
        ast.append({"OUTPUT": keyword[1].strip("'\"")})
    else:
        # TODO: Create a error handling. we don't want use the python exceptions!
        # TODO: use something like this for exceptions => Error: if you want to i tell you the problem you need to wait for 1h
        raise (SyntaxError("look for it yourself i'm not gonna point to it xd"))

########
# RUN! #
########
for ex in ast:
    match ex:
        case {"OUTPUT": string}:
            println(string)
