from azure.servicebus import ServiceBusClient

connection_str = 'key'
queue_name = 'pago'

def receive_message():
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)
    receiver = servicebus_client.get_queue_receiver(queue_name=queue_name, max_wait_time=5)
    with receiver:
        for msg in receiver.receive_messages(max_message_count=1):
            print("Mensaje recibido:", msg)
            receiver.complete_message(msg)
    if not receiver._session:  # Verificar si la sesión está cerrada
            print("No se encontraron más mensajes en la cola.")        

if __name__ == "__main__":
    receive_message()
