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

    def get_cities(self):
        with self.driver.session() as session:
            return session.read_transaction(self.get_cities_bd)

    def get_works_from_city(self,city):
        with self.driver.session() as session:
            return session.read_transaction(self.get_works_from_city_bd,city)

    def get_work_details(self,id_work):
        with self.driver.session() as session:
            return session.read_transaction(self.get_work_details_bd,id_work)

    @staticmethod
    def get_work_details_bd(tx,id_work):
        nodes = tx.run("MATCH (n:Work) WHERE ID(n) = $id RETURN n", id=id_work)
        works = []
        for node in nodes:
            works.append(str(node['n'].id) + "|" + node['n'].get('title') + "|" + node['n'].get('address') + "|" + node['n'].get('date')+ "|" + node['n'].get('type'))
        return works[0]

    @staticmethod
    def get_cities_bd(tx):
        nodes = tx.run("MATCH (n:City) RETURN n")
        cities = []
        for node in nodes:
            cities.append(node['n'].get('title'))
        return cities

    @staticmethod
    def get_works_from_city_bd(tx,city):
        nodes = tx.run("MATCH (:City { title: $city })-->(n) RETURN n", city=city)
        works = []
        for node in nodes:
            works.append(str(node['n'].id) + "|" + node['n'].get('title') + "|" + node['n'].get('address'))
        return works


    @staticmethod
    def create_node(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN '\"' + a.message + '\"' + ' added with node id ' + id(a)",
                        message=message)
        return result.single()[0]

example = Neo4jConnection("bolt://localhost:7687", "debrone", "12345")
example.get_cities()
#example.close()