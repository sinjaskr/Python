import pywhatkit as kit

number = "+1(647)853-3889"  # Replace with the phone number you want to send the message to
message = "hello"
hours = 18  # 24-hour format
minutes = 29

kit.sendwhatmsg(number, message, hours, minutes)
