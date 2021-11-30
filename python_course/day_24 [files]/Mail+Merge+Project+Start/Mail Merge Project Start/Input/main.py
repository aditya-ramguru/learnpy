with open('../input/Letters/starting_letter.txt') as file1:
    with open('../input/Names/invited_names.txt') as file2:
        f1 = file1.read()
        print(f1)
        for name in file2:
            #new = []
            name = name.rstrip()
            x = f1.replace('[name],', f'{name},')
            #new.append(x)
            # for i in range(1,len(f1)):
            #     new.append(f1[i])
            # letter =''.join(new)
            print(x)
            # with open(f'../output/ReadyToSend/To_{name}.txt', mode='w') as file3:
            #     file3.write(letter)



