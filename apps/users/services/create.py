from apps.users.models import Users
from apps.users.exceptions import RecordSaveError
from django.core.exceptions import ValidationError


class CreateUser:

    def __init__(self, attributes):
        self._name = attributes['name']
        self._phone = attributes['phone']

    def execute(self):
        try:
            user = Users(
                name=self._name,
                phone=self._phone,
            )
            user.save()
            return user
        except ValidationError as error:
            raise RecordSaveError("User", error.messages)
        except Exception as error:
            print('Caught this error: ' + repr(error))
            # log to honeybadger or kibana
            raise