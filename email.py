import email_to

server = email_to.EmailServer('smtp.gmail.com', 587, 'user@gmail.com', 'password')
server.quick_email('someone@else.com', 'Test',
                   ['# A Heading', 'Something else in the body'],
                   style='h1 {color: blue}')
