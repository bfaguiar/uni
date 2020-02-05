
% By: Bruno Filipe Oliveira Aguiar, N.Mec: 80177
%     Jose' Pedro Domingues, N.Mec.: 80075

printf("exercicio a")

%Espaco de amostragem
S = { 5, 50, 100 }

%Probabilidades dos Acontecimentos Elementares
p(5)   = 90/100
p(50)  = 9 /100
p(100) = 1 /100

Array5   = ones(1,90)*5;
Array55  = ones(1,9) *50;
Array100 = ones(1,1) *100;
tot      = [ Array5, Array55, Array100 ];

printf("exercicio b")

p5   = sum(total==5)  /length(tot);
p50  = sum(total==50) /length(tot);
p100 = sum(total==100)/length(tot);

printf("exercicio c")

stem([1 50 100],[p5 p50 p100]);
