"""timberline rfid models
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

from django.db import models
from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import User

class RfidTag(models.Model):
	"""
	Defines an RfidTag that can be associated with a user.
	
	"""
	
	tag_serial = models.CharField(max_length=16, unique=True, db_index=True)
	tag_comment = models.CharField(max_length=256, blank=True)
	user = models.ForeignKey(User)
	
class AuthConsumer(models.Model):
	"""
	Defines a user of authentication data from Timberline.
	
	"""
	
	name = models.CharField(
		max_length=256,
		help_text='Human-readable name for the authentication consumer.'
	)
	
	shared_key = models.CharField(
		max_length=256,
		help_text='Shared key used to verify authentication requests.'
	)
	
	uuid = UUIDField(
		help_text='Unique identifier used for authentication with the consumer.',
		db_index=True
	)
	
	users = models.ManyToManyField(
		User,
		help_text='Defines which users may be authenticated by this consumer.',
		blank=True
	)
	
	enabled = models.BooleanField(blank=True, default=True)


class RfidAccessEvent(models.Model):
	"""
	Logs access events for consumers.
	"""
	
	# log unknown tags too, so we have an optional fk relation with RfidTag
	tag_serial = models.CharField(max_length=16, unique=True, db_index=True)
	
	rfid_tag = models.ForeignKey(RfidTag, null=True, blank=True)
	
	# this is copied from the RfidTag at the time of query, so that if a card
	# changes holder it doesn't copy old access events across.
	user = models.ForeignKey(User, db_index=True)
	
	auth_consumer = models.ForeignKey(AuthConsumer, db_index=True)

	access_granted = models.BooleanField(blank=True)
	when = models.DateTimeField(auto_now_add=True)

	# was the event recorded "offline"?
	offline = models.BooleanField(blank=True)
	
	# the time at which the event was recorded can be different to when
	# it was reported for offline events.
	recorded = models.DateTimeField(auto_now_add=True)

