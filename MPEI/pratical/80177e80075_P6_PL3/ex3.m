
% By: Bruno Filipe Oliveira Aguiar, N.Mec.: 80177
%     Jose' Pedro Domingues, N.Mec.: 80075

nExperimentos = 1e6;
probabilidadeCara = 1/2;
probabilidade = rand(4, nExperimentos) < probabilidadeCara;

numeroCoroas = sum(probabilidade);

prinf("exercicio a")

mtrx = zeros(1,5);

for idx = 1:5
   
   mtrx(idx) = sum(numeroCoroas == (idx-1) ) / nExperimentos;

end


printf("exercicio c")

bar(0:4 ,matrx);


printf("exercicio d")

% p(k) = comb_nk(4, k)*(1/2)^k*(1-1/2)^(4-k): FORMULA

k = 0;
p0 = comb_nk(4, 0)*(1/2)^0*(1-1/2)^(4-0);

k = 1;
p1 = comb_nk(4, 1)*(1/2)^1*(1-1/2)^(4-1);

k = 2;
p2 = comb_nk(4, 2)*(1/2)^2*(1-1/2)^(4-2);

k = 3;
p3 = comb_nk(4, 3)*(1/2)^3*(1-1/2)^(4-3);

k = 4;
p4 = comb_nk(4, 4)*(1/2)^4*(1-1/2)^(4-4);


printf("exercico e")

p_i = p2 + p3 + p4;

p_ii = p0 + p1;

p_iii = p1 + p2 + p3;



