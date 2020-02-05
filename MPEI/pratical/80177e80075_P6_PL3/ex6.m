%     Bruno Filipe Oliveira Aguiar, N.Mec.: 80177
%     Jose' Pedro Domingues, N.Mec.: 80075

x = 8000;
y = 1/1000;
d = 7;

printf("Distribuicao de Poisson: ")
alfa = x * y;
( (alfa^d) / factorial(d) ) * exp(-alfa)

printf("Distribuicao binomial: ")
z = x - d + 1:x;
prod(x-d+1:x) / prod(1:d) * y^d * (1-y)^(x-d)