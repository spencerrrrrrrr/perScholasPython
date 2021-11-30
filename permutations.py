"""
Solution to Codewars Challenge "Permutations" in Python.
"In this kata you have to create all permutations of an input string and remove duplicates, if present.
This means, you have to shuffle all letters from the input in all possible orders."
Sample input given by Codewars is 'a', 'ab', and 'aabb' ie. permutations('aabb')
Link to challenge: https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
Note: not fulfilling the full attempt just yet.
"""
import itertools

def permutations(string):
    string_arr = list(itertools.permutations(string))  # IN WITH THE NEW, USING ITERTOOLS
    new_arr = []

    for x in string_arr:
        new_arr.append(''.join(x))

    print(new_arr)
    final_arr = []

    for x in new_arr:
        if x not in final_arr:
            final_arr.append(x)

    return final_arr


"""      OUT WITH THE OLD    
    temp_arr = [string]
    string_arr = list(string)
    final_arr = []

    if len(string_arr) <= 1:
        return temp_arr

    for j in range(len(string_arr)):
        for i in range(len(string_arr)):  # ------------------------------ Here I start shifting the characters.
            string_arr[j], string_arr[i] = string_arr[i], string_arr[j]  # Swap the characters at indexes i & j
            temp_arr.append(''.join(string_arr))  #------------------------Join chars as a string and append
                                                                         # our new character combination into an array
    for x in temp_arr:
        if x not in final_arr:
            final_arr.append(x) #Adding elements from temp_arr that are not already in my final_arr

    return final_arr
"""


print(permutations('aabb'))
