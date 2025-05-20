def get_response(message):
    message = message.lower()
    if "leave" in message:
        return "Our leave policy allows 20 paid leaves annually. Apply via the HR portal."
    elif "contact" in message or "email" in message:
        return "You can contact HR at hr@example.com for any queries."
    elif "office hours" in message or "timing" in message:
        return "Office hours are 9 AM to 6 PM, Monday to Friday."
    elif "holiday" in message:
        return "You can find the holiday calendar on the HR portal or company website."
    else:
        return "Sorry, I didn't understand that. Please contact HR at hr@example.com."
