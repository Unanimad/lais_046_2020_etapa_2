import pandas as pd

from django.conf import settings

from django.core.management.base import BaseCommand

from vaccine_card.logistic.models import State, City, Address, HealthCenter


class Command(BaseCommand):
    help = "Auto import Address and HealthCenter."

    def handle(self, *args, **options):
        df_cities = pd.read_csv('data/municipios_ibge.csv')
        ufs = df_cities.groupby(['UF', 'Nome_UF'], as_index=False).count()

        for i, uf in ufs.iterrows():
            state, created = State.objects.update_or_create(name=uf['Nome_UF'],
                                                            defaults={'id': uf['UF']})

            for x, city in df_cities.loc[df_cities['UF'] == uf['UF']].iterrows():
                City.objects.update_or_create(name=city['Nome_Municipio'], state=state,
                                              defaults={'id': city['Codigo_Municipio']})

