%     Bruno Filipe Oliveira Aguiar, N.Mec.: 80177
%     Jos� Pedro Domingues, N.Mec.: 80075

x = 1e6;
y = randn(1, x) * 2 + 14;

y(y>20) = 20;
y(y<0) = 0;

printf("exercicio a")
probabilidadeA = sum(y>12 & y<16) / x

printf("exercicio b")
probabilidadeB = sum(y>10 & y<18) / x

printf("exercicio c")
probabilidadeC = sum(y>=10) / x