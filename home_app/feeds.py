import feedparser
import operator
from datetime import datetime, timedelta


def get_feed():
    visir_feeds = feedparser.parse("https://www.visir.is/rss/frettir/")
    mblinnlent_feeds = feedparser.parse("https://www.mbl.is/feeds/innlent/")
    mblerlent_feeds = feedparser.parse("https://www.mbl.is/feeds/erlent/")
    ruvinnlent_feeds = feedparser.parse("https://www.ruv.is/rss/innlent")
    ruverlent_feeds = feedparser.parse("https://www.ruv.is/rss/erlent")
    parsed_feed = parse_feed(
        visir_feeds['entries'],
        mblinnlent_feeds['entries'],
        mblerlent_feeds['entries'],
        ruvinnlent_feeds['entries'],
        ruverlent_feeds['entries']
    )
    return parsed_feed


def parse_feed(visir_f, mbli_f, mble_f, ruvi_f, ruve_f):
    news_lst = []
    for f in visir_f:
        parsed_v = parse_date('Visir', f)
        news_lst.append(parsed_v)
    for f in mbli_f:
        parsed_m = parse_date('Mbl', f)
        news_lst.append(parsed_m)
    for f in mble_f:
        parsed_m = parse_date('Mbl', f)
        news_lst.append(parsed_m)
    for f in ruvi_f:
        parsed_m = parse_date('Ruv', f)
        news_lst.append(parsed_m)
    for m in ruve_f:
        parsed_m = parse_date('Ruv', m)
        news_lst.append(parsed_m)
    news_lst.sort(key=operator.itemgetter('time'), reverse=True)
    return news_lst


def parse_date(site, entry):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    entry['site'] = site
    p = entry['published']
    day = p[5:7]
    month = months.index(p[8:11]) + 1
    month = '0' + str(month) if month < 10 else str(month)
    year = p[12:16]
    h = p[17:19]
    m = p[20:22]
    s = p[23:25]
    t_str = '{}{}{}{}{}{}'.format(year, month, day, h, m, s)
    entry['time'] = int(t_str)
    today = datetime.today()
    then = datetime(int(year), int(month), int(day), int(h), int(m), int(s))
    entry['time_diff'] = today - then
    if entry['time_diff'] < timedelta(minutes=1):
        if int(entry['time_diff'].seconds) == 1:
            entry['time_passed'] = str(int(entry['time_diff'].seconds)) + " sekúndu síðan"
        else:
            entry['time_passed'] = str(int(entry['time_diff'].seconds)) + " sekúndum síðan"
    elif entry['time_diff'] < timedelta(hours=1):
        if int(entry['time_diff'].seconds / 60) == 1:
            entry['time_passed'] = str(int(entry['time_diff'].seconds / 60)) + " mínutu síðan"
        else:
            entry['time_passed'] = str(int(entry['time_diff'].seconds / 60)) + " mínutum síðan"
    elif entry['time_diff'] < timedelta(days=1):
        if int(entry['time_diff'].seconds / 60**2) == 1:
            entry['time_passed'] = str(int(entry['time_diff'].seconds / 60 ** 2)) + " klukkutíma síðan"
        else:
            entry['time_passed'] = str(int(entry['time_diff'].seconds / 60**2)) + " klukkutímum síðan"
    else:
        if int((entry['time_diff'].seconds / 60**2) / 24) == 1:
            entry['time_passed'] = str(int((entry['time_diff'].seconds / 60**2) / 24)) + " degi síðan"
        else:
            entry['time_passed'] = str(int((entry['time_diff'].seconds / 60 ** 2) / 24)) + " dögum síðan"
    return entry