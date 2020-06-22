from apps.users.models import Users
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from apps.users.exceptions import RecordSaveError, RecordNotFoundError

class UpdateUser:
    def __init__(self, user_id, attributes):
        self._user_id = user_id
        self._name = attributes['name']
        self._phone = attributes['phone']

    def execute(self):
        try:
            user = Users.objects.get(id=self._user_id)
        except Users.DoesNotExist:
            raise RecordNotFoundError("User")
        print(self._name is not None)
        print(self._phone is not None)
        try:
            with transaction.atomic():
                if self._name is not None:
                    user.name = self._name
                if self._phone is not None:
                    user.phone = self._phone
                user.save()
            return user
        except (IntegrityError, ValidationError) as error:
            print('Caught this error: ' + repr(error))
            # log to honeybadger or kibana
            transaction.rollback()
            if hasattr(error, 'messages'):
                raise RecordSaveError("User", error.messages)




