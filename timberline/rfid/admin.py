"""timberline rfid admin
Copyright 2012-2013 Michael Farrell <http://micolous.id.au/>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.contrib import admin
from timberline.rfid.models import *

class RfidTagAdmin(admin.ModelAdmin):
	list_display = ('tag_serial', 'tag_comment', 'user')
	
class AuthConsumerAdmin(admin.ModelAdmin):
	list_display = ('name', 'uuid')
	
class RfidAccessEventAdmin(admin.ModelAdmin):
	list_display = ('tag_serial', 'rfid_tag', 'user', 'auth_consumer', 'when', 'access_granted', 'offline', 'recorded')

for x in (
	(RfidTag, RfidTagAdmin),
	(AuthConsumer, AuthConsumerAdmin),
	(RfidAccessEvent, RfidAccessEventAdmin),
):
	admin.site.register(*x)
