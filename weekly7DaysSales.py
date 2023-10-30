def weekly7DaysSales(ticketPrice):
    # 関数を完成させてください
    if ticketPrice > 250:
        return int(150000 - (ticketPrice - 250)/10 * 7000)
    elif ticketPrice < 250:
        return int(150000 + (250 - ticketPrice)/10 * 7000)
    else:
        return 150000
