def whoIsWinner(hisCard):
    yourCard = 10
    if hisCard > yourCard or hisCard < 3:
        return "you lose"
    elif hisCard < yourCard:
        return "you win"
    else:
        return "draw"

# whoIsWinner(1) --> you lose
# whoIsWinner(2) --> you lose
# whoIsWinner(3) --> you win
# whoIsWinner(9) --> you win
# whoIsWinner(10) --> draw
# whoIsWinner(11) --> you lose
