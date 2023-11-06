def interestsPaid(initialLoan,didPayOnTime):
    # 関数を完成させてください
    total = initialLoan
    percentDefault = 1.02
    percentLate = 1.15
    serviceFee = 2.5

    if didPayOnTime:
        total = total * percentDefault
    else:
        total = total * percentLate
    
    return total + serviceFee
