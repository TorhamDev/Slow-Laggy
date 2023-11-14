import sys
from detectors import is_a_println
from runners._io import println

argv = sys.argv

if len(argv) < 2:
    print("Error: Please enter the slow-laggy programm file.\nexmaple: sl test.sl")
    exit()

file_name = sys.argv[1]


###########################
# tokenizing prgram code  #
###########################
tokens: list[str] = []
with open(file_name) as program_file:

    for token in program_file.read().split("\n"):
        token and tokens.append(token.strip())


#####################
# Parse the Tokens! #
#####################
ast: list[dict[str, str]] = []
for token in tokens:
    if is_a_println(token):
        print_value = token[8:]
        ast.append({"OUTPUT": print_value[1:len(print_value)-1]})

########
# RUN! #
########
for ex in ast:
    ex_type = list(ex.keys())[0]
    if ex_type == "OUTPUT":
        println(ex[ex_type])
