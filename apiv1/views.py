# IPhistdb-API - REST API for querying aggregated IP history data
# Copyright (C) 2013  Sergej Alikov <sergej.alikov@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.http import HttpResponse
from models import APIKey
from django.conf import settings
from aggdb import AggDB
import json
import datetime
import pytz


class AuthenticationException(Exception):
    pass


def requested_tz(request):
    return pytz.timezone(request.META.get("HTTP_TZ", "UTC"))


def require_apikey(fn):
    def wrapper(*args, **kwargs):
        if len(APIKey.objects.filter(key=args[0].META.get("HTTP_APIKEY", ""))) > 0:
            return fn(*args, **kwargs)
        else:
            raise AuthenticationException("Invalid API key")
    return wrapper


@require_apikey
def ip(request, ip):

    adb = AggDB()
    adb.lookup_tz = requested_tz(request)
    adb.connect(settings.APIV1_AGGDB_HOST,
                settings.APIV1_AGGDB_USER,
                settings.APIV1_AGGDB_PASS,
                settings.APIV1_AGGDB_DB)

    body = []

    for item in adb.lookup_by_ip(ip):
        body.append(item)

    adb.close()

    return HttpResponse(json.dumps(body, encoding="latin_1"))


@require_apikey
def ipbydate(request, ip, date):
    adb = AggDB()
    adb.lookup_tz = requested_tz(request)
    adb.connect(settings.APIV1_AGGDB_HOST,
                settings.APIV1_AGGDB_USER,
                settings.APIV1_AGGDB_PASS,
                settings.APIV1_AGGDB_DB)

    body = []

    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    for item in adb.lookup_by_ip(ip, dt):
        body.append(item)

    adb.close()

    return HttpResponse(json.dumps(body, encoding="latin_1"))


@require_apikey
def mac(request, mac):

    adb = AggDB()
    adb.lookup_tz = requested_tz(request)
    adb.connect(settings.APIV1_AGGDB_HOST,
                settings.APIV1_AGGDB_USER,
                settings.APIV1_AGGDB_PASS,
                settings.APIV1_AGGDB_DB)

    body = []

    for item in adb.lookup_by_mac(mac):
        body.append(item)

    adb.close()

    return HttpResponse(json.dumps(body, encoding="latin_1"))


@require_apikey
def macbydate(request, mac, date):
    adb = AggDB()
    adb.lookup_tz = requested_tz(request)
    adb.connect(settings.APIV1_AGGDB_HOST,
                settings.APIV1_AGGDB_USER,
                settings.APIV1_AGGDB_PASS,
                settings.APIV1_AGGDB_DB)

    body = []

    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    for item in adb.lookup_by_mac(mac, dt):
        body.append(item)

    adb.close()

    return HttpResponse(json.dumps(body, encoding="latin_1"))
