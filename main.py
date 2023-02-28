student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_pandas = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_pandas)

# nato_alphabet = pandas.DataFrame(result)
# print(nato_alphabet)
new_dic = {row.letter: row.code for (index, row) in nato_pandas.iterrows()}
# print(new_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato_converter():
    word = input("enter a word to be converted: \n").upper()
    # nato_convert = [new_list for item in list]
    try:
        nato_convert = [new_dic[letter] for letter in word]
    except KeyError:
        print("only letters please!")
        nato_converter()
    else:
        print(nato_convert)
nato_converter()

