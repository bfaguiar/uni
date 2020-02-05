%     Bruno Filipe Oliveira Aguiar, N.Mec.: 80177
%     Jose' Pedro Domingues, N.Mec.: 80075

x = 1e6;
y = randn(1, x)*10;

probabilidadeA = sum(y<3) / x
probabilidadeB = sum(y>7) / x
probabilidadeC = sum(y>1 & y<6) / x