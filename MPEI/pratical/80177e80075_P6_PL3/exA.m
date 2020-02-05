% By: Bruno Filipe Oliveira Aguiar, N.Mec.: 80177 
%     Jose' Pedro Domingues, N.Mec.: 80075

nExperiencias = 10000;
lados = 6;
dados = 1;

pX = floor( rand(dados, nExperiencias) * (lados+1) );

 
% Funcao da Probabilidade Massa

probabilidade = [ sum(pX==1)/nExperiencias, sum(pX==2)/nExperiencias, sum(pX==3)/nExperiencias, sum(pX==4)/nExperiencias, sum(pX==5)/nExperiencias, sum(pX==6)/nExperiencias ]
stem(1:lados, probabilidade)

%Funcao da Distribuicao Acomulada

somaAcumulativa = [ 0 cumsum(probabilidade) ];
stairs(0:lados, somaAcumulativa)