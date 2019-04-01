from charms.reactive import when, when_not, when_any
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class SparkRequires(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        if any(unit.received['master-uri'] for unit in self.all_units):
            set_flag(self.expand_name('available'))

    @when_not('endpoint.{endpoint_name}.joined')
    def broken(self):
        clear_flag(self.expand_name('available'))
        

    def relation_data(self):
        """
        Get the list of the relation info for each unit.

        """
        units_data = []
        for relation in self.relations:
            for unit in relation.units:
                master_uri = unit.received['master-uri']
                ctxt = {
                    'master_uri': master_uri
                }
                units_data.append(ctxt)
        return units_data
