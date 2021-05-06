
print(f"\n\n-----------\nConnection\n____________\n")


class Connection:
    port = 55000
    conn_limit = 10
    conn_count = 0
    
    def __init__(self, host):
        # set the host for the instance
        self.host = host
        # set the port based on the class variable port
        # add 1 to the class's connection_count
        if (self.conn_count < Connection.conn_limit):
            self.conn_count += 1
            self.port = self.port + self.conn_count

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
        if len(self.connections) < self.conn_limit:
            self.connections.append(self)
            self.port = self.port + len(self.connections)
        
    def close(self):
        self.connections.remove(self)
        
    def __repr__(self):
        return f"host: {self.host}, port: {self.port} connections: {len(self.connections)}"


connection1 = Connection2("localhost")
connection2 = Connection2("localehost")
connection3 = Connection2("hostdulocal")

print(connection1.__dict__)
print(connection2.__dict__)
print(connection3.__dict__)
print(f"repr(connection1): {repr(connection1)}")
print(f"repr(connection2): {repr(connection2)}")
print(f"repr(connection3): {repr(connection3)}")

print(Connection2.__dict__)

connection1.close()
print(connection1.__dict__)
print(Connection2.__dict__)

