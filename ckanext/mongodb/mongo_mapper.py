import ckan.plugins as plugins
import ckan.model.package
from pylons import config

from pymongo import Connection


class MongoMapper(plugins.SingletonPlugin):
    plugins.implements(plugins.IMapper, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)

    DEFAULT_CONNECTION = 'mongodb://localhost:27017'
    DATABASE = 'ckan_db'
    COLLECTION = 'datasets'


    def before_update(self, mapper, connection, instance):
        mongocon = self.connect()
        collection = mongocon[self.DATABASE][self.COLLECTION]
        
        package = instance.as_dict()

        #Filter out non-package updates
        if isinstance(instance, ckan.model.package.Package):
            package['_id'] = package['id']
            collection.save(package)
        
        mongocon.disconnect()


    def before_insert(self, mapper, connection, instance):
        return self.before_update(mapper, connection, instance)

    def before_delete(self, mapper, connection, instance):
        mongocon = self.connect()
        collection = mongocon[self.DATABASE][self.COLLECTION]
        
        package = instance.as_dict()

        #Filter out non-package updates
        if isinstance(instance, ckan.model.package.Package):
            collection.remove({'_id':package['id']})

        mongocon.disconnect()


    #IPackageController
    def before_view(self, pkg_dict):
        mongocon = self.connect()
        collection = mongocon[self.DATABASE][self.COLLECTION]

        results = collection.find_one({'_id': pkg_dict['id']})

        mongocon.disconnect()

        return results

    def connect(self):
        conn_string = config.get('mongodb.connection_string',self.DEFAULT_CONNECTION)
        return Connection(conn_string)
