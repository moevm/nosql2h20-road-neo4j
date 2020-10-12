from neo4j import GraphDatabase

class Neo4jConnection:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_message(self, message):
        with self.driver.session() as session:
            msg = session.write_transaction(self.create_node, message)
            print(msg)

    @staticmethod
    def create_node(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN '\"' + a.message + '\"' + ' added with node id ' + id(a)",
                        message=message)
        return result.single()[0]

example = Neo4jConnection("bolt://localhost:7687", "debrone", "12345")
example.get_message("Hello,world!")
example.close()