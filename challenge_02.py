import sys

OPERATIONS = {
    '#': lambda value: value + 1,
    '@': lambda value: value - 1,
    '*': lambda value: value * value
}

START_VALUE = 0
PRINT_OPERATION = "&"


def compiler(program_operations: str) -> str:
    if not program_operations:
        return ""

    program_output = ""
    program_value = START_VALUE

    for operation in program_operations:
        if operation == PRINT_OPERATION:
            program_output += str(program_value)
            continue

        operation_function = OPERATIONS.get(operation)
        if not operation_function:
            raise Exception(f"Operation {operation} is not defined")

        program_value = operation_function(program_value)

    return program_output


if __name__ == '__main__':
    print(compiler(sys.stdin.read()))
