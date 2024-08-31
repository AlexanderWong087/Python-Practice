votes=input('Input the votes: ').split()
def find_all_candidates(arr):
    global candidates
    candidates = []
    for element in arr:
        if element not in candidates:
            candidates.append(element)
def count_votes(votes, participators):
    global results
    results={}
    for p in participators:
        