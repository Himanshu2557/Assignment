print('--------------------Question-6---------------------')

#inputting a word 
word = input("Enter the Word: ").lower()

#inputting a meaningful word with the exact same letters
testword = input("\nEnter a MEANINGFUL word to test your friendship: ").lower()

#defining dictionary from last assignment
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

#test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")
else:
    print("The word does have a meaning and letters are exact, friendship is not fake!!")
