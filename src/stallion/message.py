from stringparser import pickleEncode



"""
Message class is for messages that 
are send and receive between server and client.
"""
class Message:
    """
    constructor.

    @param type: message type which can be (subscribe, unsubscribe or normal)
    """
    def __init__(self, type=1, topic="", data=""):
        self.type = type
        self.setTopic(topic=topic)
        self.setData(data=data)

    """
    setTopic.

    @param topic: message topic.
    """
    def setTopic(self, topic):
        self.topic = topic
    
    """
    setData.

    @param data: message payload.
    """
    def setData(self, data):
        self.data = pickleEncode(data)


"""
newMessage.

creates a new message object.
"""
def newMessage(type=1, topic="", data="") -> Message:
    return Message(type=type, topic=topic, data=data)
