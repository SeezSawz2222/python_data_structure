import random as rd

def get_def(word_list,word_dict):
    ranrom_index = rd.randrange(len(word_list))
    word = word_list.pop(ranrom_index)
    defi = word_dict.get(word)
    return word, defi

def word_def(rstring):
    word, defi = rstring.split(',', 1)
    return word, defi

fh = open("desktop\\PYTHONNNN\\Vocabulary_list.csv","r")
wd_list = fh.readlines()
#print(wd_list)

wd_list.pop(0)
wd_set = set(wd_list)
fh = open("desktop\\PYTHONNNN\\Vocabulary_set.csv","w")
fh.writelines(wd_set)

word_dict = dict()
for rs in wd_set:
    word, defi = word_def(rs)
    word_dict[word] = defi
    #print(word)

while True:
    wd_list = list(word_dict)
    choice_list = []
    for x in range(4):
        word,defi = get_def(wd_list,word_dict)
        choice_list.append(defi)
    rd.shuffle(choice_list)

    print(word)
    print("- - -- -  - -- - -")
    for idx, choice in enumerate(choice_list):
        print(idx+1,choice)
    print("PRESS KEY 1, 2, 3 or 4 to select and press 0 to exit")
    choice = int(input("ENTER: 2"))

    if choice_list[choice-1] == defi:
        print("CORRECT!!!")
    elif choice == 0:
        exit(0)
    else:
        print("INCORRECT!!!")