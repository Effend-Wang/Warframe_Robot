# 聊天机器人主程序

# 导入程序库
import send_message

print("这里是Warframe机器人v0.1版")
print("本机器人由（QQ：465152177）开发，未经作者允许禁止传播！\n")
print("本机器人支持查询：\n\t1、Warframe游戏内容查询\n\t2、Warframe Market交易查询\n\t3、Warframe游戏内容翻译\n")
print("输入消息来和我对话吧^_^\n")

while True:
	message=input(">>>")

	if (message!=""):
		message=send_message.message_create(message)
		print(message)

	print("")

