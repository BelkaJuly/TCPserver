from twisted.internet import protocol, reactor


class Twist(protocol.Protocol):

    # Событие connectionMade срабатывает при соединении
    def connectionMade(self):
        print('connection success!')

    # Событие dataReceived - получение и отправление данных
    def dataReceived(self, data):
        print(data)
        # transport.write - отправка сообщения
        self.transport.write('Hello from server!'.encode('utf-8'))

    # Событие connectionLost срабатывает при разрыве соединения с клиентом
    def connectionLost(self, reason):
        print('Connection lost!')


# Конфигурация поведения протокола описывается в – классе Factory из twisted.internet.protocol.Factory
factory = protocol.Factory()
factory.protocol = Twist
print('wait...')
reactor.listenTCP(777, factory)
reactor.run()
