import paho.mqtt.client as mqtt
import sys
 
#definicoes: 
Broker = "iot.eclipse.org"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoPublish = "TESTEMQTTSUGAI"


client = mqtt.Client()
client.connect(Broker, PortaBroker, KeepAliveBroker)

while True:
	teste = input("Informe algo: ")
	client.publish("paho/teste", teste)
	if teste == 'xx':
		break




# single(topic, payload=None, qos=0, retain=False, hostname="localhost",
#     port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None,
#     protocol=mqtt.MQTTv311, transport="tcp")
# while True:
#     temperature = sensor.blocking_read()
#     mqttc.publish("paho/temperature", temperature)

# import paho.mqtt.publish as publish

# msgs = [{'topic':"paho/test/multiple", 'payload':"multiple 1"},
#     ("paho/test/multiple", "multiple 2", 0, False)]
# publish.multiple(msgs, hostname="iot.eclipse.org")