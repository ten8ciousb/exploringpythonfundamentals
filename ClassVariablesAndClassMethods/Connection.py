
print(f"\n\n-----------\nConnection\n____________\n")


class Connection:
    port = 55000
    conn_limit = 10
    conn_count = 0
    
    def __init__(self, host):
        # set the host for the instance
        self.host = host
        # set the port based on the class variable port
        self.port = Connection.port
        # add 1 to the class's connection_count
        Connection.conn_count += 1

    def close(self):
        # reduce the class's connection_count by 1
        self.conn_count -= 1

    def __repr__(self):
        return f"host: {self.host}, port: {self.port} connections: {self.conn_count}"


connection = Connection("localhost")
connection2 = Connection("localhost")

print(f"connection.__dict__: {connection.__dict__}")
print(f"connection2.__dict__: {connection2.__dict__}")
print(f"Connection.__dict__: {Connection.__dict__}")
print(f"repr(connection): {repr(connection)}")

print(f"\n----------\nchange connection host and port\n_____________")
connection.host = "127.0.0.1"
connection.port ="8888"

print(f"connection.__dict__: {connection.__dict__}")
print(f"connection2.__dict__: {connection2.__dict__}")
print(f"Connection.__dict__: {Connection.__dict__}")
print(f"repr(connection): {repr(connection)}")


print(f"\n\n-----------\nConnection2\n____________\n")


class Connection2:
    port = 55000
    conn_limit = 10
    connections = []
    
    def __init__(self, host):
        self.host = host
        self.port = Connection2.port
        self.connections.append(self)
        
    def close(self):
        self.connections.remove(self)
        
    def __repr__(self):
        return f"{self.host}, {self.port}"


connection1 = Connection2("localhost")
connection2 = Connection2("localehost")
connection3 = Connection2("hostdulocal")

print(connection1.__dict__)
print(connection2.__dict__)
print(connection3.__dict__)
print(Connection2.__dict__)

connection1.close()
print(connection1.__dict__)
print(Connection2.__dict__)

