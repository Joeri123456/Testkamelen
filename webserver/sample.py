from flask import Flask, render_template
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim'
socketio = SocketIO(app)

MQTT_BROKER = '10.42.0.1'
MQTT_PORT = 1883
MQTT_TOPIC_SUB = 'GAMECONTROLLER/OUT/STATE'
MQTT_TOPIC_PUB = 'KNOPPEN/OUT/CMD'
MQTT_TOPIC_GETAL = 'GAMECONTROLLER/IN/SCOREMULTIPLIER'
MQTT_TOPIC_BEVESTIGING = 'GAMECONTROLLER/OUT/SCOREMULTIPLIER'

mqtt_client = mqtt.Client()

@app.route("/")
def index():
    return render_template("index.html")

# Wanneer een bericht wordt ontvangen op het sub-topic
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic
    print(f"Ontvangen van {topic}: {payload}")
    
    if topic == MQTT_TOPIC_SUB:
        socketio.emit('update_tekst', {'tekst': payload})
    elif topic == MQTT_TOPIC_BEVESTIGING:
        socketio.emit('bevestigd_getal', {'waarde': payload})

# WebSocket: browser vraagt om reset
@socketio.on('reset')
def handle_reset():
    print("Reset aangevraagd door client")
    mqtt_client.publish(MQTT_TOPIC_PUB, "RESET")

@socketio.on('start')
def handle_start():
    print("Start aangevraagd door client")
    mqtt_client.publish(MQTT_TOPIC_PUB, "START")

@socketio.on('nieuw_getal')
def handle_nieuw_getal(data):
    try:
        getal = int(data.get('getal'))
        if 1 <= getal <= 20:
            print(f"Verstuur getal: {getal}")
            mqtt_client.publish(MQTT_TOPIC_GETAL, str(getal))
        else:
            print("Getal buiten bereik (1-20)")
    except (ValueError, TypeError):
        print("Ongeldig getal ontvangen")

# Start MQTT-client in een aparte thread
def mqtt_thread():
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.subscribe(MQTT_TOPIC_SUB)
    mqtt_client.subscribe(MQTT_TOPIC_BEVESTIGING)
    mqtt_client.loop_forever()

threading.Thread(target=mqtt_thread, daemon=True).start()

if __name__ == "__main__":
    socketio.run(app, debug=True)
