def send_messages(send_msgs):
    """Print each message in the list"""
    while msgs:
        msg = msgs.pop()
        print(msg)
        send_msgs.append(msg)

msgs = ['Hello!', 'How are you?', 'Where are you?']
send_msgs = []
send_messages(send_msgs)
print(send_msgs)
