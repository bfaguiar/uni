Nexperiencias = 1e5; % numero de experiencias
N = 10; % numero de lancamentos por experiencia
p = 0.5; % probabilidade de sair cara ou coroa.
cara = 10; 
k = 10;

matrizGeradora = rand(N, Nexperiencias) > 0.5;

somaDasCoroas = sum(matrizGeradora)==k;

probabilidadeDasCoroas = sum(somaDasCoroas)/Nexperiencias