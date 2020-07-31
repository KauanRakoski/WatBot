from twilio.rest import Client

 
account_sid = 'AC970aa9aa62f3d0907eae384d484cdb09' 
auth_token = 'e5533d6fddd2da471381a994b0ab1331' 
client = Client(account_sid, auth_token) 


def send_text():
    bomdia = client.messages.create(
                              from_='whatsapp:+',
                              body=f'Bom dia.',
                              to='whatsapp:+'
                          )

    print(bomdia.sid)

    lembretes = client.messages.create(
        from_='whatsapp: num',
        body=f'lorem ipsum',
        to='boiler plate text'
    )

    print(lembretes.sid)
