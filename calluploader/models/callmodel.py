from django.db import models


class NumberChoices(models.IntegerChoices):
    outgoing = 1  # Исходящий
    incoming = 2  # Входящий
    outgoing_w_redirect = 3  # Входящий с перенаправлением
    reverse = 4  # Обратный


class CallModel(models.Model):
    # For calling register method
    user_phone_inner = models.CharField(blank=False, null=False)
    user_id = models.IntegerField(blank=False, null=False)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    call_start_date = models.CharField(max_length=200)  # iso8601 формат - Пример: 2021-02-03T18:25:10+03:00
    type = models.IntegerField(choices=NumberChoices.choices)

    # For calling finish method
    call_id = models.CharField(blank=True, null=False)
    duration = models.IntegerField(blank=False, null=False)
    record_url = models.FileField(upload_to='calls/%Y/%m/%d', null=True, blank=True)

    def register_call_id(self, but):
        res = but.call_api_method("telephony.externalcall.register", {
            "USER_PHONE_INNER": self.user_phone_inner,
            "USER_ID": self.user_id,
            "TYPE": self.type,
            "PHONE_NUMBER": self.phone_number,
            "CALL_START_DATE": self.call_start_date,
        })
        call_id = res['result']['CALL_ID']
        self.call_id = call_id
        self.save()

    def finish(self, but):
        res = but.call_api_method('telephony.externalcall.finish', {
            "CALL_ID": self.call_id,
            "USER_ID": self.user_id,
            "DURATION": self.duration,
            "RECORD_URL": f'https://9f331a7de5c6-14688458821772174966.ngrok-free.app/media/{self.record_url}',
        })

    def __str__(self):
        return f'Звонок от {self.call_start_date} длительностью {self.duration}, клиент - {self.phone_number}'
