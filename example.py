from lib.wcc import WebsocketCollabClient, ProtocolMessage, ProtocolMessageUnknown

WS_URL = "<url>"
USER = "<user>"
PASS = "<pass>"
CHANNEL_ID = "<channel id>"

client = WebsocketCollabClient()
client.connect(
    url=WS_URL,
    channel_id=CHANNEL_ID,
    user=USER,
    password=PASS)

def listener_all(msg: ProtocolMessageUnknown):
    print("RAW:", msg.to_dict())

def listener_text(msg: ProtocolMessage):
    print("RAW:", msg.to_dict())
    print(f"From: '{msg.payload.name}' Message: '{msg.payload.content}'")

client.on_all_messages(listener_all)
client.on_text_message(listener_text)

client.send_text("Hilda", "This is a test message", ["all"])
