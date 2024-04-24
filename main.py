import nltk
import inspect
import re

def get_nltk_functions():
    nltk_functions = ["download", "help", "exit"]
    for name, obj in inspect.getmembers(nltk):
        if inspect.isfunction(obj):
            nltk_functions.append(name)
    return nltk_functions

def nltk_prompt():
    nltk_commands = get_nltk_functions()
    print("NLTK Command Prompt")
    print("Type 'help' for list of NLTK functions or 'exit' to quit.")

    while True:
        command = input(">>> ").strip().lower()

        if command == 'exit':
            print("Exiting NLTK Prompt...")
            break
        elif command == 'help':
            print("Available commands:")
            for func in nltk_commands:
                print("-", func)
        elif command in nltk_commands:
            print("You selected:", command)
            # Ask for function arguments
            args = input("Enter function arguments: ").strip()
            # Call the function with arguments
            execute_nltk_function(command, args)
        elif command.startswith('download'):
            if command == 'download_all':
                nltk.download("all")
            else:
                download_package(command)
        else:
            print("Invalid command. Type 'help' for list of NLTK functions.")

def execute_nltk_function(func_name, args_str):
    # Parse the arguments string into a dictionary
    args = {}
    for arg_pair in args_str.split():
        key, value = re.split(r'\s*=\s*', arg_pair)
        args[key] = eval(value)

    # Call the NLTK function with the provided arguments
    func = getattr(nltk, func_name)
    result = func(**args)
    print("Function result:", result)

def download_package(command):
    parts = command.split(' ')
    if len(parts) < 2:
        nltk.download_gui()
    else:
        package_name = parts[1]
        if len(parts) > 2:
            args_str = ' '.join(parts[2:])
        else:
            args_str = ''
        execute_nltk_function('download', f'package="{package_name}" {args_str}')

nltk_prompt()