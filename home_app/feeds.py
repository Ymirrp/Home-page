import feedparser
import operator
import requests
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


def get_weather(lat, lon):
    api_url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + \
              "&lon=" + lon + "&units=metric&appid=c5d83ac177a5989b9d9ee9f886892237"
    print(api_url)
    res = requests.get(api_url)
    return parse_weather(res.json())


def parse_weather(w):
    translation = {
        "Thunderstorm": "Þrumuveður",
        "Drizzle": "Skúrir",
        "Rain": "Rigning",
        "Snow": "Snjókoma",
        "Clear": "Heiðskýrt",
        "Clouds": "Skýjað"
    }
    city = w['name']
    weather = translation[w['weather'][0]['main']]
    wind = w['wind']['speed']
    temp = int(round(w['main']['temp'], 0))
    degree = get_degree(int(w['wind']['deg']))
    present = datetime.now()
    time_diff = present - timedelta(seconds=w['dt'])
    time = time_diff.minute
    img = "http://openweathermap.org/img/wn/" + w['weather'][0]['icon'] + '.png'
    return {
        "city": city,
        "weather": weather,
        "temp": temp,
        "wind": wind,
        "deg": degree,
        "time": time,
        "icon": img
    }


def get_degree(deg):
    ret = ''
    if deg != 0:
        deg = deg / 32
    if deg < 3 or deg >= 31:
        # ret = 'N'
        ret = '&#8593'
    elif 3 <= deg < 8:
        # ret = 'N/A'
        ret = '&#8599'
    elif 8 <= deg < 11:
        # ret = 'A'
        ret = '&#8594'
    elif 11 <= deg < 16:
        # ret = 'S/A'
        ret = '&#8600'
    elif 16 <= deg < 19:
        # ret = 'S'
        ret = '&#8595'
    elif 19 <= deg < 24:
        # ret = 'S/V'
        ret = '&#8601'
    elif 24 <= deg < 27:
        # ret = 'V'
        ret = '&#8592'
    elif 27 <= deg < 30:
        # ret = 'N/V'
        ret = '&#8598'
    return ret

