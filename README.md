"OlimpicHistory" 

Este projeto tem como objetivo utilizar Python e Django Framework para exemplificar o CRUD.

Foquei também em aprender e configurar a base de dados e o deploy do app no Heroku. Conhecimento que no início não tinha, mas agora ví como funciona.

Foram utilizadas duas base de dados como exemplo. Como a base athelete_events tinha mais de 200.000 registros, e o databse free fornecido pelo Heroku suporta no máximo 10.000 registros, então reduzi a base para 9.000 registros. Obviamente que o desempenho não está bom, devido a assinatura free do Heroku. Busquei hospedar o app também no Heroku, mas apesar de ter trabalhado em cima do tutorial, não consegui concluir esse processo.

O resultado aqui foi focado em trabalhar com as bases dadas, mas em uma próxima atualização seria importante criar uma tabela de atletas (athletes) e criar o relacionamento com "Athletes Events". Certamente fazer isso iria cumprir um requisito necessário em bases de dados de evitar a repetição de dados.

Também existe muito o que fazer sobre renderização de formulários para ter uma apresentação viável para o usuário. Mas consegui aplicar o Bootstrap fazendo alguma renderização que esteja aceitável.

