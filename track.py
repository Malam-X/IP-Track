
# IP API
# DR4G0N5


"""     MODULES      """

import os, sys
import requests


__author__='DR4G0N5'


def promt(promt):

    """     INPUT PROMT      """

    return input(promt).strip()


def clear(clr):

    """     CLEAR      """

    return os.system(clr)


class menu:

    """     MENU      """

    def __init__(self, target):

        """     REQUESTS      """

        self.url = 'http://ip-api.com'
        self.full = self.url+'/json/{TARGET}'
        self.request = requests.get(self.full.format(TARGET=target))
        self.respon = self.request.json()
        q = self.query()

    def query(self):

        """     QUERY      """

        return self.respon['query']

    def status(self):

        """     STATUS      """

        return self.respon['status']

    def country(self):

        """     COUNTRY      """

        return self.respon['country']

    def countryCode(self):

        """     COUNTRY CODE      """

        return self.respon['countryCode']

    def city(self):

        """     CITY      """

        return self.respon['city']

    def zip(self):

        """     ZIP      """

        return self.respon['zip']

    def lat(self):

        """     LATITUDE      """

        return self.respon['lat']

    def lon(self):

        """     LONGTITUDE      """

        return self.respon['lon']

    def timezone(self):

        """     TIMEZONE      """

        return self.respon['timezone']

    def isp(self):

        """     ISP      """

        return self.respon['isp']

    def org(self):

        """     ORGANIZATION      """

        return self.respon['org']

    def aS(self):

        """     AS      """

        return self.respon['as']

def logs(ip):

    """     LOGS      """

    x = menu(ip)
    LOGS = ('''
    Ip : {ip}
    Country : {country}
    City : {city}
    Zip : {zip}
    Isp : {isp}
    Organization : {org}

    Google Maps

    Latitude : {lat}
    Longtitude : {lon}
    Google Maps : https://www.google.com/maps/@{lat},{lon},12z
    ''')

    """     FORMAT      """

    x = LOGS.format(
        ip=x.query(),
        country=x.country(),
        city=x.city(),
        zip=x.zip(),
        isp=x.isp(),
        org=x.org(),
        lat=x.lat(),
        lon=x.lon())
    print(x)
if __name__ == '__main__':

    """     TARGET      """

    target = '0'
    try:
        if sys.argv[1] == '':
            print('Usage python main.py 1.1.1.1')
        else:
            target = sys.argv[1]
        logs(sys.argv[1])

        """  INDEX ERROR  """

    except IndexError:
        print('Usage python main.py 1.1.1.1')

        """  IP NOT FOUND ERROR  """

    except KeyError:
        print('[-] IP Not Found')

        """  ABORTED  """

    except KeyboardInterrupt:
        sys.exit('[!] Aborted.')
