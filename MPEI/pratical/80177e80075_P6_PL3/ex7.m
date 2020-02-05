%     Bruno Filipe Oliveira Aguiar, N.Mec.: 80177
%     Jose' Pedro Domingues, N.Mec.: 80075

a = 15;
k = 0:100;

y = ( (a^d) / factorial(d) ) * exp(-a);

printf("exercicio a")
probabilidadeA = sum( (x == 0) * y)

display("exercicio b")
probabilidadeB = sum( (x > 10) * y)
