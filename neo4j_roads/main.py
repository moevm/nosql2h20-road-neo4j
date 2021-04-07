from neo4j import GraphDatabase
import time

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
    def import_database_bd(tx):
        tx.run("CALL apoc.load.csv('works.csv')")

    def export_database(self):
        with self.driver.session() as session:
            return session.read_transaction(self.import_database_bd)

    @staticmethod
    def export_database_bd(tx):
        tx.run("CALL apoc.export.csv.all('works.csv', {})")

    def get_count_works_by_month(self,month):
        with self.driver.session() as session:
            return session.read_transaction(self.get_count_works_by_month_bd,month)

    @staticmethod
    def get_count_works_by_month_bd(tx, month):
        result = tx.run("MATCH (n:Work) where split(n.date,'.')[1] = $month return count(n)",month=month)
        return result.single()[0]

    def get_count_works_by_city(self, city):
        with self.driver.session() as session:
            return session.read_transaction(self.get_count_works_by_city_bd, city)

    @staticmethod
    def get_count_works_by_city_bd(tx, city):
        result = tx.run("MATCH (n:City { title: $city })-[r:HAS]->(c) return count(r)", city=city)
        return result.single()[0]

    def create_work(self,title,address,date,type,city):
        with self.driver.session() as session:
            return session.write_transaction(self.create_work_bd,title,address,date,type,city)

    @staticmethod
    def create_work_bd(tx,title,address,date,type,city):
        result = tx.run("CREATE (w:Work{title:$title, address:$address, date:$date,type:$type}) RETURN ID(w)",title = title,address = address,date=date,type=type)
        id_work = result.single()[0]
        tx.run("MATCH (w:Work), (c:City) WHERE ID(w)=$id AND c.title=$city CREATE (c)-[r:HAS]->(w)",id=id_work,city=city)

    def update_work_by_id(self,id_work,title,address,date,type):
        with self.driver.session() as session:
            return session.write_transaction(self.update_work_by_id_bd,id_work,title,address,date,type)

    @staticmethod
    def update_work_by_id_bd(tx, id_work,title,address,date,type):
        tx.run("MATCH (w:Work) where ID(w) = $id SET w.title=$title, w.address = $address, w.date = $date, "
               "w.type = $type", id=id_work,title = title,address = address,date=date,type=type)

    def delete_work_by_id(self,id_work):
        with self.driver.session() as session:
            return session.write_transaction(self.delete_work_by_id_bd,id_work)

    @staticmethod
    def delete_work_by_id_bd(tx, id_work):
        tx.run("MATCH (w:Work)<-[r:HAS]-(n) where ID(w) = $id DELETE r", id=id_work)
        tx.run("MATCH (n:Work) WHERE ID(n) = $id DELETE n", id=id_work)

    def get_works_by_filter(self,date,type,address):
        with self.driver.session() as session:
            return session.read_transaction(self.get_works_by_filter_bd,date,type,address)

    
    def import_database(self, data):
        print(data)
        for d in data:
            #title,address,date,type,city
            # create_work(d['title'], d['address'], d['date'], d['type'], d['city'])
            with self.driver.session() as session:
                session.write_transaction(self.create_work_bd,d['title'], d['address'], d['date'], d['type'], d['city'])

    @staticmethod
    def get_works_by_filter_bd(tx, date, type, address):
        params = {}
        query = "MATCH (n:Work{"
        if date != "":
            query += "date:$date"
            params['date'] = date
        if type != "":
            if "date" in params:
                query += ","
            query += "type:$type"
            params['type'] = type
        if address != "":
            if "type" in params or "date" in params:
                query += ","
            query += "address:$address"
            params['address'] = address
        query += "}) RETURN n"
        nodes = tx.run(query, parameters=params)
        works = []
        for node in nodes:
            print(node)
            works.append(str(node['n'].id) + "|" + node['n'].get('title') + "|" + node['n'].get('address'))
        return works

    def get_works_by_address(self,address):
        with self.driver.session() as session:
            return session.read_transaction(self.get_works_by_address_bd,address)

    @staticmethod
    def get_works_by_address_bd(tx, address):
        nodes = tx.run("MATCH (n:Work{address:$address}) RETURN n", address=address)
        works = []
        for node in nodes:
            works.append(str(node['n'].id) + "|" + node['n'].get('title') + "|" + node['n'].get('address'))
        return works

    def get_all_addresses(self):
        with self.driver.session() as session:
            return session.read_transaction(self.get_all_addresses_bd)

    @staticmethod
    def get_all_addresses_bd(tx):
        nodes = tx.run("MATCH (n:Work) RETURN DISTINCT n.address")
        addresses = []
        for node in nodes:
            addresses.append(node['n.address'])
        return addresses

    def get_works_by_type(self,type):
        with self.driver.session() as session:
            return session.read_transaction(self.get_works_by_type_bd,type)

    @staticmethod
    def get_works_by_type_bd(tx, type):
        nodes = tx.run("MATCH (n:Work{type:$type}) RETURN n", type=type)
        works = []
        for node in nodes:
            works.append(str(node['n'].id) + "|" + node['n'].get('title') + "|" + node['n'].get('address'))
        return works

    def get_all_types(self):
        with self.driver.session() as session:
            return session.read_transaction(self.get_all_types_bd)

    @staticmethod
    def get_all_types_bd(tx):
        nodes = tx.run("MATCH (n:Work) RETURN DISTINCT n.type")
        types = []
        for node in nodes:
            types.append(node['n.type'])
        return types

    def get_works_by_date(self,date):
        with self.driver.session() as session:
            return session.read_transaction(self.get_works_by_date_bd,date)

    @staticmethod
    def get_works_by_date_bd(tx,date):
        nodes = tx.run("MATCH (n:Work{date:$date}) RETURN n",date=date)
        works = []
        for node in nodes:
            works.append(str(node['n'].id) + "|" + node['n'].get('title') + "|" + node['n'].get('address'))
        return works

    def get_all_dates(self):
        with self.driver.session() as session:
            return session.read_transaction(self.get_all_dates_bd)

    @staticmethod
    def get_all_dates_bd(tx):
        nodes = tx.run("MATCH (n:Work) RETURN DISTINCT n.date")
        dates = []
        for node in nodes:
            dates.append(node['n.date'])
        return dates

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

    def get_cities(self):
        with self.driver.session() as session:
            return session.read_transaction(self.get_cities_bd)

    @staticmethod
    def get_cities_bd(tx):
        nodes = tx.run("MATCH (n:City) RETURN n")
        cities = []
        for node in nodes:
            cities.append(node['n'].get('title'))
        return cities

    def get_works_from_city(self,city):
        with self.driver.session() as session:
            return session.read_transaction(self.get_works_from_city_bd,city)

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


while True:
            try:
                example = Neo4jConnection("bolt://127.0.0.1:7687", "debrone", "12345")
                break
            except:  # Wait till neo4j gets available to connect to
                time.sleep(0.1)
#example.get_cities()
#example.close()
