from azure.servicebus import ServiceBusClient, ServiceBusMessage

connection_str = 'key'
queue_name = 'pago'

servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str, logging_enable=True)

def send_message():
    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=queue_name)
        with sender:
            message = ServiceBusMessage("Se ha recibido el pago del distribuidor")
            sender.send_messages(message)
            print("Mensaje enviado")


if __name__ == "__main__":
    send_message()

