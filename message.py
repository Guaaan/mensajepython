# importing the module
import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:
	
# sending message to reciever
# using pywhatkit
pywhatkit.sendwhatmsg("+56 945854758",
						"Hellofrom GeeksforGeeks",
						23, 41)
print("Successfully Sent!")

except:
	
# handling exception
# and printing error message
print("An Unexpected Error!")
