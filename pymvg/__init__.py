from requests_html import HTMLSession


def _get_as_html(station):
    return HTMLSession().get(
        'http://www.mvg-live.de/ims/dfiStaticAuswahl.svc',
        params={'haltestelle': station},
        headers={'Content-Type': 'text/html; charset=UTF-8'}
    ).html


def _parse(html):
    server_time = html.xpath(
        '//td[@class="serverTimeColumn"]/text()')[0]

    results = []
    for row in html.xpath('//table[@class="departureTable departureView"]/tr[@class="rowOdd" or @class="rowEven"]'):
        line = row.xpath(
            '//td[@class="lineColumn"]/text()', first=True)
        station = row.xpath(
            '//td[@class="stationColumn"]/text()', first=True)
        in_min = row.xpath(
            '//td[@class="inMinColumn"]/text()', first=True)
        results.append({
            'type': _get_type(line),
            'line': line,
            'station': _get_station_decoded(station),
            'in_min': int(in_min)
        })

    return {'server_time': server_time, 'items': results}


def _fix_station(station):
    if station.startswith('Karlsplatz'):
        return 'Karlsplatz (Stachus)'
    elif station.startswith('Stachus'):
        return 'Karlsplatz (Stachus)'
    return station


def _get_type(line):
    if line.startswith('U'):
        return 'subway'
    if line.startswith('S'):
        return 's-train'
    return 'bus/tram'


def _get_station_decoded(station):
    return station.strip().encode(encoding='UTF-8').decode('UTF-8')


def get_departures_for(station):
    """Get departures for given station

    Parameters:
    -----------

    station : string
      Name of a station

    Returns a dictonary with a list of upcoming departures which is formated like this::

    {
      'server_time': '12:05'
      'items': [
        { 'line': 'U2', 'type': 'subway', 'station': 'Messestadt Ost', 'in_min': 2 },
        { 'line': 'U2', 'type': 'subway', 'station': 'Feldmoching', 'in_min': 5 },
        { 'line': 'U2', 'type': 'subway', 'station': 'Messestadt Ost', 'in_min': 12 }
      ]
    }

    """
    return _parse(_get_as_html(_fix_station(station)))
