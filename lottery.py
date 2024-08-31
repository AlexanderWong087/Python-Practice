def lottery(ticket, win):
    mini_wins = 0
    for sublist in ticket:
        for char in sublist[0]:
            if ord(char) == sublist[1]:
                mini_wins += 1
                break
    if mini_wins >= win:
        return "Winner!"
    else:
        return "Loser!"

print(lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2))
print(lottery([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP", 84]], 1))
print(lottery([["ZSAMZB", 81], ["XWWCXP", 72], ["SYBRQOHP", 88], ["HJSVV", 75]], 1))