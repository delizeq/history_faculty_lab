from django.db import models


class SiteContent(models.Model):
    """Текст головної сторінки. Налаштовується з адмінки (запис має бути один)."""

    title = models.CharField("заголовок", max_length=200)
    tagline = models.CharField("підзаголовок", max_length=300, blank=True)
    description = models.TextField("опис факультету")
    address = models.CharField("адреса", max_length=300, blank=True)
    phone = models.CharField("телефон", max_length=50, blank=True)
    email = models.EmailField("e-mail", blank=True)

    class Meta:
        verbose_name = "текст головної сторінки"
        verbose_name_plural = "текст головної сторінки"

    def __str__(self):
        return self.title

    @classmethod
    def get(cls):
        return cls.objects.first()


class Department(models.Model):
    name = models.CharField("назва", max_length=200)
    head = models.CharField("завідувач кафедри", max_length=200)

    class Meta:
        verbose_name = "кафедра"
        verbose_name_plural = "кафедри"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField("назва", max_length=200)
    code = models.CharField("код", max_length=20)
    description = models.TextField("опис")
    coordinator_name = models.CharField("імʼя координатора набору", max_length=200)
    coordinator_contact = models.CharField("контакт координатора набору", max_length=200)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="programs",
        verbose_name="випускова кафедра",
    )
    subjects = models.TextField("список дисциплін", blank=True, help_text="Кожна дисципліна з нового рядка.")

    class Meta:
        verbose_name = "спеціальність"
        verbose_name_plural = "спеціальності"
        ordering = ["code", "name"]

    def __str__(self):
        return f"{self.code} {self.name}"

    @property
    def subject_list(self):
        return [line.strip() for line in self.subjects.splitlines() if line.strip()]


class Teacher(models.Model):
    name = models.CharField("імʼя", max_length=200)
    position = models.CharField("посада", max_length=200)
    degree = models.CharField("науковий ступінь", max_length=200, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="кафедра",
    )

    class Meta:
        verbose_name = "викладач"
        verbose_name_plural = "викладачі"
        ordering = ["name"]

    def __str__(self):
        return self.name
