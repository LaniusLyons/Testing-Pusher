import pusher
from django.conf import settings


pusher_client = pusher.Pusher(
  app_id=settings.PUSHER_APP_ID,
  key=settings.PUSHER_KEY,
  secret=settings.PUSHER_SECRET,
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})