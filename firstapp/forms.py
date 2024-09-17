from django import forms


class UserForm(forms.Form):
    file = forms.ImageField(label="Изображение")
    date = forms.DateField(label="Введите дату")
    time = forms.DateField(label="Введите время")
    date_time = forms.DateTimeField(label="Введите дату и время")
    time_delta = forms.DurationField(label="Введите промежуток времени")
    date_time2 = forms.SplitDateTimeField(label="Введите дату и время (раздельно)")
    num = forms.IntegerField(label="Введите целое число")
    num2 = forms.DecimalField(label="Введите десятичное число")
    num3 = forms.FloatField(label="Введите число")
    ling = forms.ChoiceField(label="Выберите язык",
                             choices=((1, "Английский"),
                                      (2, "Немецкий"),
                                      (3, "Французский")))
    country = forms.MultipleChoiceField(label="Выберите страны",
                                        choices=((1, "Англия"),
                                                 (2, "Германия"),
                                                 (3, "Испания"),
                                                 (4, "Россия")))
    city = forms.TypedMultipleChoiceField(label="Выберите город",
                                          empty_value=None,
                                          choices=((1, "Москва"),
                                                   (2, "Воронеж"),
                                                   (3, "Курск"),
                                                   (4, "Томск")))
