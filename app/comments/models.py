"""Copyright 2014 Cyrus Dasadia

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from django.db import models
from django.contrib.auth.models import User
from cito_engine.models import Incident


class Comments(models.Model):
    text = models.TextField(max_length=500)
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_created=True, auto_now_add=True)
    incident = models.ForeignKey(Incident)

    def __unicode__(self):
        return "%s:%s:%s" % (self.incident.id, self.date_added, self.user)