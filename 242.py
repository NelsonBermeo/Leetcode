#We can use dictionaries or arrays or bruteforce here. Brute force with a count variable.
#We could also sort. 
#Here I will just document the method using dictionaries

#Dictionary 

def is_anagram_dic(s1, s2):
    if len(s1) != len(s2):
        return False
    count1, count2 = {}, {}
    for i in range(len(s1)):
        count1[s1[i]] = count1.get([s1[i]],0) + 1 #The count at that letter is updated if seen, the .get(0) returns a 0 for the first time a letter appears; an interesting method for dics
        count1[s2[i]] = count2.get([s2[i]],0) + 1
    #Then we can use the == which compares the dics
    return count1 == count2