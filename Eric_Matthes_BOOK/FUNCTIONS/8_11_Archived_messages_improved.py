def send_messages(msgs):
    """Print each message in the list"""
    for msg in msgs:
        print(msg)

def sent_messages(msgs):
    sent_msgs = []

    while msgs:
        msg = msgs.pop()
        sent_msgs.append(msg)
    #Add msg back to msgs
    for msg in sent_msgs:
        msgs.append(msg)
    return msgs

msgs = ['Hello!', 'How are you?', 'Where are you?']
send_messages(msgs)
print("\nSent messages")
sent_msgs = sent_messages(msgs[:])
send_messages(sent_msgs)
print("\nOriginal list")
send_messages(msgs)