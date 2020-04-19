def shorten_line():
        try:
                file = open('Project ideas.txt', 'r')
        except:
                print('File not found.')

        lines = file.readlines()
        line_length = int(input('How long would you like your lines?'))
        newFile = open('Coding Projects.txt', 'w+')

        for line in lines:

                newLine = line

                if len(newLine) > line_length:
                        reps = int(len(newLine) / line_length)
                        for i in range(1, reps+1):
                                newLine = newLine[:(line_length*i)] + '\n\t' + newLine[(line_length*i):]


                newFile.write(newLine)

def make_spaces():
        with open('Python Fundamentals.txt', 'r') as file:
                with open('Fundamentals of Python.txt', 'w+') as newFile:

                        lines = file.readlines()
                        
                        for line in lines:
                                
                                isCap = False
                                newLine = line
                                for c in line:
                                        if c != c.lower():
                                                isCap == True
                                                break
                                        else:
                                                continue
                                if isCap == True:
                                        newLine = '\n\n' + line + '\n\n'

                                newFile.write(newLine)
                        

if __name__ == '__main__':
        make_spaces()
        
