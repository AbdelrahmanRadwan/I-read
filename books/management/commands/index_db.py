from django.core.management.base import BaseCommand
from elasticsearch.client import IndicesClient
from books.models import Book
from elasticsearch.helpers import bulk
from django.conf import settings



class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        self.recreateIndex()
        self.push_db_to_index()
        print("success...:)");

    def recreateIndex(self):
        """function to recreate the index in tge elasticsearch"""
        print( "delete the previous index and creating th new one...")
        indices_client=IndicesClient(client=settings.ES_CLIENT)
        index_name=Book._meta.es_index_name
        type_type=Book._meta.es_type_name
        if indices_client.exists(index=index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index_name)
        indices_client.put_mapping(
            doc_type=Book._meta.es_type_name,
            body=Book._meta.es_mapping,
            index=index_name
        )

    def push_db_to_index(self):
        """this is the function for push the data from the db to the index"""
        print( "preparing the data...")
        data=[
        self.create_for_bulk(product,'create') for product in Book.objects.all()
        ]
        print( "do the indexing....")
        bulk(settings.ES_CLIENT,actions=data,stats_only=True)

    def create_for_bulk(self,django_object,action):
        """this is the method used to prepate the objct for the indexing"""
        data=django_object.es_repr()
        meta={
        "_op_type":action,
        "_index":django_object._meta.es_index_name,
        "_type":django_object._meta.es_type_name,
        "_id":django_object.pk,
        }
        data.update(**meta)
        return data