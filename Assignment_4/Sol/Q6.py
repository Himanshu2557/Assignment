print('--------------------Question-6---------------------')

#inputting a word 
word = input("Enter the Word: ").lower()

#inputting a meaningful word with the exact same letters
testword = input("\nEnter a MEANINGFULL word to test your friendship: ").lower()

#defining dictionary to check if letters are same
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

# checking same letter condition
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")
else:
#shopkeeper to verify the word's meaning
    while True:
        ans = input("\nDoes the word makes sense?(y or n)\n").lower()

        if ans == 'y':
            print("The friends pass the friendship test!!\n")
            break
        elif ans == 'n':
            print("The word doesn't have a meaning, friendship is fake!!\n\n")
            break
        else:
            print("Invalid input, try again")