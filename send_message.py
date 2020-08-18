from warframe.warframe_operate import warframe

# 创建需要发送的消息
def message_create(message_from_user):

	message_to_send=""
	message_check=message_from_user.split()
	if (len(message_check)<=1):
		return ""

	message_to_send=warframe(message_check,message_from_user)

	return message_to_send
