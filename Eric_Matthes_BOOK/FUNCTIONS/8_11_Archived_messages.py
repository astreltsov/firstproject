msgs = ['Hello!', 'How are you?', 'Where are you?']
print(msgs)
def send_messages(send_msgs):
    """Print each message in the list"""
    while msgs:
        msg = msgs.pop()
        print(msg)
        send_msgs.append(msg)
    for msg in send_msgs:
        msgs.append(msg)

    return msgs

msgs = ['Hello!', 'How are you?', 'Where are you?']
send_msgs = []
send_messages(send_msgs)
print(send_msgs)
print(msgs)