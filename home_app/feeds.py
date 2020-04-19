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
    entry['time'] = '{}{}{}{}{}{}'.format(year, month, day, h, m, s)
    today = datetime.now()
    then = datetime(int(year), int(month), int(day), int(h), int(m), int(s))
    entry['time_diff'] = today - then
    time_diff = entry['time_diff']
    time_diff_seconds = int(time_diff.total_seconds())
    m, s = divmod(time_diff_seconds, 60)
    h, m = divmod(m, 60)

    if h > 23:
        if h // 24 == 1:
            entry['time_passed'] = str(h // 24) + " degi síðan"
        else:
            entry['time_passed'] = str(h // 24) + " dögum síðan"
    elif h > 0:
        if h == 1:
            entry['time_passed'] = str(h) + " klukkutíma síðan"
        else:
            entry['time_passed'] = str(h) + " klukkutímum síðan"
    elif m > 0:
        if m == 1:
            entry['time_passed'] = str(m) + " mínutu síðan"
        else:
            entry['time_passed'] = str(m) + " mínutum síðan"
    else:
        if s == 1:
            entry['time_passed'] = str(s) + " sekúndu síðan"
        else:
            entry['time_passed'] = str(s) + " sekúndum síðan"
    return entry
