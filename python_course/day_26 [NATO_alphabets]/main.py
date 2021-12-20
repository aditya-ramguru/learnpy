import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#row.student
#row.score

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index,row) in data.iterrows()}
# print(nato_dict)
# for row in data.iterrows():
#     print(row[1])
#     print(type(row[1]))


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    val = input('Enter your name: ').upper()
    try:
       nato_list = [nato_dict[i] for i in val]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()