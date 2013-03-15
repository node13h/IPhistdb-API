# Copyright 2013 Sergej Alikov

# This file is part of IPhistdb-API.

# IPhistdb is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# IPhistdb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with IPhistdb-API.  If not, see <http://www.gnu.org/licenses/>.

from django.contrib import admin
from apiv1.models import APIKey


class APIKeyAdmin(admin.ModelAdmin):
    fields = ('app',)
    list_display = ('app', 'key')

admin.site.register(APIKey, APIKeyAdmin)
