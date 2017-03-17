
import sys
import uuid

from cassandra.cqlengine.models import Model, columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.connection import cluster, session

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.policies import WhiteListRoundRobinPolicy
from cassandra.policies import ConstantReconnectionPolicy


hosts = ['127.0.0.1']
# conn = connection.setup(hosts,
#                         'cassandra_cqlengine',
#                         auth_provider=PlainTextAuthProvider(username="cassandra", password="cassandra"),
#                         load_balancing_policy=WhiteListRoundRobinPolicy(hosts),
#                         reconnection_policy=ConstantReconnectionPolicy(10, sys.maxint),
#                         )


connection.cluster = Cluster(
            hosts,
            auth_provider=PlainTextAuthProvider(username="cassandra", password="cassandra"),
            load_balancing_policy=WhiteListRoundRobinPolicy(hosts),
            # load_balancing_policy=DCAwareRoundRobinPolicy(data_center),
            reconnection_policy=ConstantReconnectionPolicy(10, sys.maxint),
            protocol_version=3
        )

connection.session = connection.cluster.connect()

class MyTableFromCqlengine(Model):
    __table_name__ = "mytable2"
    __keyspace__ = "cassandra_cqlengine"
    __default_ttl__ = 100

    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_id1 = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_id2 = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type = columns.Integer(index=True)
    created_at = columns.DateTime()
    description = columns.Text(required=False)

from cassandra.cqlengine.management import sync_table
sync_table(MyTableFromCqlengine)



from cassandra.cqlengine.named import NamedTable