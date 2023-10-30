def weekly7DaysSales(ticketPrice):
    # 関数を完成させてください
    CUSTOMER = 150000
    BASE_PRICE = 250
    rate = 7000/10
    diff = BASE_PRICE - ticketPrice
    return int(CUSTOMER + diff * rate)
