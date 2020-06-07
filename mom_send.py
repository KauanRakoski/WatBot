from twilio.rest import Client
import datetime
 
account_sid = 'AC970aa9aa62f3d0907eae384d484cdb09' 
auth_token = 'e5533d6fddd2da471381a994b0ab1331' 
client = Client(account_sid, auth_token) 

dia = str(datetime.datetime.today())


def send_text():
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=f'Atualizando...{dia}',
                              to='whatsapp:+555599309399'
                          )

    print(message.sid)
