records = {}


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Tip: Enter input in format {command space value}"
        except KeyError:
            return "Unknown rec_id. Try again. Tip: Enter input in format {command space value}"
        except ValueError:
            return "Value error. Tip: Enter input in format {command space value} "
    return inner


@user_error
def add(*args):
    rec_id = args[0]
    rec_value = args[1]
    records[rec_id] = rec_value
    return f"Add record {rec_id = }, {rec_value = }"


@user_error
def change(*args):
    rec_id = args[0]
    new_value = args[1]
    rec = records[rec_id]
    if rec:
        records[rec_id] = new_value
        return f"Change record {rec_id = }, {new_value = }"


@user_error
def greeting(*args):
    return "How can I help you?"


@user_error
def phone(*args):
    rec_id = args[0]
    if rec_id in records:
        return f"Existing record {rec_id = }, {records[rec_id]} "


@user_error
def show_all(*args):
    return '\n'.join([f"{key}: {value}" for key, value in records.items()])


@user_error
def exit_programm(*args):
    return "EXIT_PROGRAM"


def unknown(*args):
    return "Unknown command. Try again."


COMMANDS = {add: ["add"],
            change: ["change"],
            greeting: ["hello"],
            phone: ["phone"],
            show_all: ["show all"],
            exit_programm: ["good bye", "close", "exit"]
            }


def parser(text: str):
    for func, kws in COMMANDS.items():
        if isinstance(kws, str):
            kws = [kws]
        for kw in kws:
            if text.startswith(kw):
                return func, text[len(kw):].strip().split()
    return unknown, []


def main():
    while True:
        user_input = input(">>>").lower()
        func, data = parser(user_input)
        result = func(*data)
        if result == "EXIT_PROGRAM":
            print("Good bye!")
            break
        else:
            print(result)


if __name__ == '__main__':
    main()
