from symtable import Class

from django.db import models


class Case(models.Model):
    """Дело на сайте - набор материалов по конкретному делу"""
    name = models.CharField('Название дела', max_length=255)

    class Meta:
        db_table = 'case'
