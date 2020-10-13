def add_to_file(file_name, word_dict):
    with open(file_name+'.txt', 'w+') as save_file:
        for key, value in word_dict.items():
            save_file.write(key + ': ' + value + '\n')



def edit_file_lines(file):
    file.mode = 'r+'

    lines = file.readlines()
    line_length = int(input('how long would you like your lines?: '))
    newLine = ''

    for line in lines:

        newLine = line
        if len(newLine) > line_length:
            reps = int(len(newLine) / line_length)

            for i in range(1, reps+1):
                newLine = newLine[:(line_length(i))] + '\n\t' + newLine[(line_length(i)):]

