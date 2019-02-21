import sys

script, input_encoding, error = sys.argv


# recursive function to print
def main(language_file, encoding, errors):
    # reads in one line
    line = language_file.readline()

    if line:
        # calls function to print encoded and decoded languages
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

