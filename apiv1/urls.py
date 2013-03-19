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

from django.conf.urls import patterns, include, url

RE_IP = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
RE_MAC = r'[0-9a-fA-F]{12}'
RE_DATE = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

p = (r'^ip/(?P<ip>{0})/$'.format(RE_IP), 'ip'), \
    (r'^ip/(?P<ip>{0})/(?P<date>{1})/$'.format(RE_IP, RE_DATE), 'ipbydate'), \
    (r'^mac/(?P<mac>{0})/$'.format(RE_MAC), 'mac'), \
    (r'^mac/(?P<mac>{0})/(?P<date>{1})/$'.format(RE_MAC, RE_DATE), 'macbydate'),


urlpatterns = patterns('apiv1.views', *p)
