from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno autora', help_text='Zadejte jméno autora',
                             error_messages={'blank': 'Jméno autora musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení autora', help_text='Zadejte příjmení autora',
                                error_messages={'blank': 'Příjmení autora musí být vyplněno'})
    narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození')
    umrti = models.DateField(blank=True, null=True, verbose_name='Datum úmrtí')
    biografie = models.TextField(blank=True, verbose_name='Životopis')
    fotografie = models.ImageField(upload_to='autori', verbose_name='Fotografie')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autoři'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Zanr(models.Model):
    nazev = models.CharField(max_length=20, verbose_name='Název žánru', help_text='Zadejte název žánru')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'

    def __str__(self):
        return f'{self.nazev}'


class Vydavatelstvi(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název vydavatelství', help_text='Zadejte název vydavatelství',
                             error_messages={'blank': 'Název vydavatelství je povinný údaj'})
    adresa = models.CharField(blank=True, null=True, max_length=200, verbose_name='Adresa')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Vydavatelství'
        verbose_name_plural = 'Vydavatelství'

    def __str__(self):
        return f'{self.nazev}'


class Kniha(models.Model):
    titul = models.CharField(max_length=100, verbose_name='Titul knihy', help_text='Zadejte titul knihy',
                             error_messages={'blank': 'Titul knihy musí být vyplněn'})
    autori = models.ManyToManyField(Autor)
    obsah = models.TextField(blank=True, verbose_name='Obsah knihy', help_text='Vložte obsah knihy')
    pocet_stran = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999)],
                                              verbose_name='Počet stran', help_text='Zadejte počet stran (max. 9999)')
    rok_vydani = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1500), MaxValueValidator(2100)],
                                             verbose_name='Rok vydání', help_text='Zadejte rok vydání (1500 - 2100)')
    obalka = models.ImageField(upload_to='obalky', verbose_name='Obálka knihy')
    zanry = models.ManyToManyField(Zanr)
    vydavatelstvi = models.ForeignKey('Vydavatelstvi', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Vydavatelství')

    class Meta:
        ordering = ['titul']
        verbose_name = 'Kniha'
        verbose_name_plural = 'Knihy'

    def __str__(self):
        return f'{self.titul} ({self.rok_vydani})'


class Recenze(models.Model):
    text = models.TextField(verbose_name="Text recenze",
                            help_text="Zadej text recenze")
    kniha = models.ForeignKey('Kniha',
                              on_delete=models.PROTECT,
                              verbose_name='Kniha')
    recenzent = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  verbose_name='Recenzent')
    HODNOCENI = (
        (0, ''),
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )
    hodnoceni = models.PositiveSmallIntegerField(choices=HODNOCENI,
                                                 verbose_name='Hodnocení',
                                                 default=3)
    cas = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['kniha', 'recenzent']
        verbose_name = 'Recenze'
        verbose_name_plural = 'Recenze'

    def __str__(self):
        return f'Recenze knihy {self.kniha} od {self.recenzent} ({self.cas.year})'