from django.forms import ModelForm
from django.forms import DateInput

from calluploader.models.callmodel import CallModel


class CustomCallForm(ModelForm):
    class Meta:
        model = CallModel
        fields = ['user_phone_inner', 'user_id', 'phone_number', 'call_start_date', 'type', 'duration', 'record_url']
        labels = {'user_phone_inner': 'Внутренний номер пользователя. Обязательный.',
                  'user_id': 'Идентификатор пользователя. Обязательный.',
                  'phone_number': 'Номер телефона. Обязательный',
                  'call_start_date': 'Дата/время звонка',
                  'type': 'Тип звонка',
                  'duration': 'Длительность',
                  'record_url': 'Запись звонка'
                  }
        widgets = {
            'call_start_date': DateInput(attrs={'type': 'datetime-local'})}
