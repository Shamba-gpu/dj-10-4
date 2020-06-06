from django.db import models

# В файле `models.py` нашего приложения создаем модель Phone с полями `id`, `name`, `price`, `image`, `release_date`,
# `lte_exists` и `slug`. Поле `id` - должно быть основным ключом модели.
class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True)



