import datetime

ELECTION_DATE = datetime.date(2018, 9, 9)


def get_msg():
    today = datetime.date.today()
    delta_time = ELECTION_DATE - today
    msg = "Idag är det {} dagar kvar till riksdagsvalet".format(
        delta_time.days)
    return msg
