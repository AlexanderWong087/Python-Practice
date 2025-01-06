def count_layers(rug_lst):
    count=1
    lst_layers=[]
    for i in range(len(rug_lst)):
        if (rug_lst[i] not in lst_layers) and rug_lst[i]==rug_lst[len(rug_lst)-i-1]:
            lst_layers.append(i)
            count+=1
    return count-1
print(count_layers([ 
  "AAAA", 
  "ABBA", 
  "AAAA" 
]))
print(
count_layers([ 
  "AAAAAAAAA", 
  "ABBBBBBBA", 
  "ABBAAABBA", 
  "ABBBBBBBA", 
  "AAAAAAAAA" 
]))
print(count_layers([ 
  "AAAAAAAAAAA", 
  "AABBBBBBBAA", 
  "AABCCCCCBAA", 
  "AABCAAACBAA", 
  "AABCADACBAA", 
  "AABCAAACBAA", 
  "AABCCCCCBAA", 
  "AABBBBBBBAA", 
  "AAAAAAAAAAA" 
]))

print(count_layers([ 
  "AAAAAAAAA", 
  "ABBBBBBBA", 
  "ABBAAABBA", 
  "ABBBABBBA", 
  "ABBBBBBBA", 
  "AAAAAAAAA" 
]))