from twilio.rest import Client

 
account_sid = 'AC970aa9aa62f3d0907eae384d484cdb09' 
auth_token = 'e5533d6fddd2da471381a994b0ab1331' 
client = Client(account_sid, auth_token) 


def send_text():
    bomdia = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=f'Bom dia.',
                              to='whatsapp:+555599309399'
                          )

    print(bomdia.sid)

    lembretes = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'Lembre-se de escovar os dentes do Bernardo, ler e treinar desenho.',
        to='whatsapp:+555599309399'
    )

    print(lembretes.sid)
