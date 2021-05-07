import json
import pprint
def pretty_dict(name, what):
    print(f"{name}: {json.dumps(what.__dict__, sort_keys=True, indent=4)}")


print(f"\n\n-----------\nConnectionUsingClass\n____________\n")


class ConnectionUsingClass:
    port = 55000
    conn_limit = 10
    connections = []
    
    def __init__(self, host):
        self.host = host
        if len(ConnectionUsingClass.connections) < ConnectionUsingClass.conn_limit:
            ConnectionUsingClass.connections.append(self)
            self.port = self.port + len(self.connections)
        
    def close(self):
        ConnectionUsingClass.connections.remove(self)

    def __repr__(self):
        return f"host: {self.host}, port: {self.port} connections: {len(self.connections)}"


connection1 = ConnectionUsingClass("localhost")
connection2 = ConnectionUsingClass("localehost")
connection3 = ConnectionUsingClass("hostdulocal")

pretty_dict("connection1", connection1)
pretty_dict("connection2", connection2)
pretty_dict("connection3", connection3)
print(f"repr(connection1): {repr(connection1)}")
print(f"repr(connection2): {repr(connection2)}")
print(f"repr(connection3): {repr(connection3)}")

print(ConnectionUsingClass.__dict__)

print(f"\n\n-----------\nClose Connection\n____________\n")
connection1.close()
print(f"repr(connection1): {repr(connection1)}")
print(f"repr(connection2): {repr(connection2)}")
print(f"connection1.__dict__: {connection1.__dict__}")
print(f"ConnectionUsingClass.__dict__: {ConnectionUsingClass.__dict__}")



print(f"\n\n-----------\nConnectionDunderClass\n____________\n")
class ConnectionDunderClass:
    port = 55000
    conn_limit = 10
    connections = []
    
    def __init__(self, host):
        self.host = host
        if len(self.__class__.connections) < self.__class__.conn_limit:
            self.__class__.connections.append(self)
            self.__class__.port = self.__class__.port + len(self.__class__.connections)
        
    def close(self):
        self.__class__.connections.remove(self)
        
    def __repr__(self):
        return f"host: {self.host}, port: {self.port} connections: {len(self.connections)}"


connection1 = ConnectionDunderClass("localhost")
connection2 = ConnectionDunderClass("localehost")
connection3 = ConnectionDunderClass("hostdulocal")

print(connection1.__dict__)
print(connection2.__dict__)
print(connection3.__dict__)
print(f"repr(connection1): {repr(connection1)}")
print(f"repr(connection2): {repr(connection2)}")
print(f"repr(connection3): {repr(connection3)}")

print(ConnectionDunderClass.__dict__)

connection1.close()
print(connection1.__dict__)
print(ConnectionDunderClass.__dict__)


print(f"\n\n-----------\nConnectionUsingClassMethods\n____________\n")
class ConnectionUsingClassMethods:
    port = 55000
    conn_limit = 10
    connections = []

    
    def __init__(self, host):
        # set the host for the instance
        self.host = host
        # set the port based on the class variable port
        # add 1 to the class's connection_count
        self.add_connection(self)
        self.port = self.get_next_port()
        
    @classmethod
    def add_connection(cls, self):
        if len(cls.connections) < cls.conn_limit:
            cls.connections.append(self)

    @classmethod
    def get_next_port(cls):
        return cls.port + len(cls.connections)

    @classmethod
    def remove_connection(cls, self):
        cls.connections.remove(self)

    def close(self):
        # reduce the class's connection_count by 1
        self.remove_connection(self)

    def __repr__(self):
        return f"host: {self.host}, port: {self.port} connections: {len(self.connections)}"

    @classmethod
    def get_connection_count(cls):
        return len(cls.connections)

    @classmethod
    def print_connections(cls):
        for connection in cls.connections:
            print(connection)

connection = ConnectionUsingClassMethods("localhost")
connection2 = ConnectionUsingClassMethods("localehost")

pretty_dict("connection", connection)
pretty_dict("connection2", connection2)
print(f"ConnectionUsingClassMethods: {ConnectionUsingClassMethods.__dict__}")
print(f"repr(connection) : {repr(connection)}")

print(f"\n----------\nchange connection host and port\n_____________")
connection.host = "127.0.0.1"
connection.port ="8888"

pretty_dict("connection", connection)
pretty_dict("connection2", connection2)
print(f"ConnectionUsingClassMethods.__dict__: {ConnectionUsingClassMethods.__dict__}")
print(f"repr(connection): {repr(connection)}")


print(f"connection count: {connection.get_connection_count()}")
print(f"ConnectionUsingClassMethods count: {ConnectionUsingClassMethods.get_connection_count()}")

ConnectionUsingClassMethods.print_connections()
connection.print_connections()

print(f"\n----------\n close connection \n_____________")
connection.close()
print(f"connection count: {connection.get_connection_count()}")
print(f"ConnectionUsingClassMethods count: {ConnectionUsingClassMethods.get_connection_count()}")
ConnectionUsingClassMethods.print_connections()
connection.print_connections()
