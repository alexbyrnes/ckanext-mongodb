import ckan.plugins as plugins
import ckan.model.package

from pymongo import Connection

class MongoMapper(plugins.SingletonPlugin):
    plugins.implements(plugins.IMapper, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)


    def before_update(self, mapper, connection, instance):
        connection = Connection('localhost', 27017)
        collection = connection['ckan_db']['packages']
        
        package = instance.as_dict()

        #Filter out non-package updates
        if isinstance(instance, ckan.model.package.Package):
            package['_id'] = package['id']
            collection.save(package)
        
        connection.disconnect()


    def before_insert(self, mapper, connection, instance):
        return self.before_update(mapper, connection, instance)

    #IPackageController
    def before_view(self, pkg_dict):

        connection = Connection('localhost', 27017)
        collection = connection['ckan_db']['packages']

        results = collection.find_one({'_id': pkg_dict['id']})

        connection.disconnect()
        return results

