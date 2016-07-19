class BikeTheftRouter: 
    def db_for_read(self, model, **hints):
        "Point all operations on 'theft_app' models to legacydb"
        if model._meta.app_label == 'theft_app':
            return 'legacy'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on 'theft_app' models to legacydb"
        if model._meta.app_label == 'theft_app':
            return 'legacy'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if both models in theft app or both not"
        if obj1._meta.app_label == 'theft_app' and obj2._meta.app_label == 'theft_app':
            return True
        # Allow if neither is Portland_bike_theft app
        elif 'theft_app' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'legacy' or model._meta.app_label == "theft_app":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True