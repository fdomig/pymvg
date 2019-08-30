import pymvg
import sys


def print_as_text(station):

    res = pymvg.get_departures_for(station)

    print("================================================================")
    print("Departures from {0:<40} [{1:5}]".format(
        station, res['server_time']))
    print("================================================================")

    for item in sorted(res['items'], key=lambda i: i['in_min']):
        print("{line:4}{type:<10}{station:<48}{in_min:>2}".format(**item))


def usage():
    print('Usage: %s <station>' % sys.argv[0])


if __name__ == '__main__':
    if len(sys.argv) is not 2:
        usage()
        sys.exit(1)

    print_as_text(sys.argv[1])
