from charms.reactive import when, set_flag, clear_flag
from charms.reactive import Endpoint


class SparkProvides(Endpoint):

    def configure(self, master_uri):
        """
        Provide the master_uri
            - master_uri
        """

        for relation in self.relations:
            ctxt = {
                'master_uri': master_uri
            }
            relation.to_publish.update(ctxt)
