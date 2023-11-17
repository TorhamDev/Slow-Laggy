import sys
from detectors import is_a_println, is_a_if,is_a_endif, check_if_condition
from runners._io import println

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
        if not token.startswith("#"):
            if token != "":
                token and tokens.append(token.strip())

#####################
# Parse the Tokens! #
#####################
ast: list[dict[str, str]] = []
inside_if = False
check_condition = False
do_rest = True
for token in tokens:
    if is_a_endif(token):
        inside_if = False
        do_rest = True
        continue

    if is_a_if(token):
        inside_if = True
        check_condition = check_if_condition(token)

    if inside_if and check_condition is False:
        do_rest = False
        continue

    if do_rest:
        if is_a_println(token):
            ast.append({"OUTPUT": token.split(" ", 1)[1].strip("'\"")})

    # else:
    #     # TODO: Create a error handling. we don't want use the python exceptions!
    #     # TODO: use something like this for exceptions => Error: if you want to i tell you the problem you need to wait for 1h
    #     raise (SyntaxError("look for it yourself i'm not gonna point to it xd"))

########
# RUN! #
########
for ex in ast:
    match ex:
        case {"OUTPUT": string}:
            println(string)
