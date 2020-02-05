% By: Bruno Filipe Oliveira Aguiar, N.Mec.: 80177
%   José Pedro Domingues, N.Mec.: 80075

nExperiencias = 1e6;
pecas = 5;
probabilidade = 0.3;

amostra = rand(5, nExperiencias) <= probabilidade;
soma = sum(amostra);

printf("exercicio a")
hist(soma, 5)

printf("exercicio b")
probabilidade = sum(s <= 2) / nExperiencias