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

from django.db import models
import uuid
from django.db.models.signals import post_init
from django.dispatch import receiver


class APIKey(models.Model):
    app = models.CharField(max_length=64)
    key = models.CharField(max_length=64)

    def __unicode__(self):
        return self.app

    def generate_key(self, app):
        self.app = app
        self.key = str(uuid.uuid4())


@receiver(post_init, sender=APIKey)
def APIKey_post_init(sender, instance, **kwargs):
    if not instance.pk and len(instance.key) == 0:
        instance.generate_key("")
