import sys

def format_output(output):
    result = ''
    line = ''
    count = 0
    for letter in output:
        line += letter
        count += 1
        if count == 5:
            result += line + ' '
            line = ''
            count = 0
    if line:
        result += line + '\n'
    return result

def encode(text, move):
    letters = [char.upper() for char in text if char.isalpha()]
    encoded = []
    for char in letters:
        ascii_val = ord(char)
        new_val = ascii_val + move
        if new_val > ord('Z'):
            final_val = (new_val - ord('Z')) % 26
            if final_val == 0:
                final_val = 26
            new_val = final_val + ord('A') - 1
        encoded.append(chr(new_val))
    return format_output(''.join(encoded))

args = sys.argv
if len(args) < 2:
    print("Please provide a shift value as a command line argument.")
    sys.exit(1)

shift = int(args[1])
for line in sys.stdin:
    result = encode(line.strip(), shift)
    sys.stdout.write(result)
