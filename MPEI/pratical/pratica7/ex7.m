## Author: Bruno Aguiar, 80177, Jose Domingues, 80075

% Ex1

clear all
clc

udata = load('u.data');

u = udata(1:end, 1:2); 
clear udata;

users = unique(u(:, 1));
uLen = length(users);

Set = cell(uLen, 1);

tic

for n = 1:uLen,
    aux = find(u(:, 1) == users(n));
    
    Set{n} = [Set{n} u(aux, 2)];
end

toc

%% Ex2

tic

J = zeros(1,uLen);
h = waitbar(0.0, 'Calculating distances...');
for n1 = 1:uLen,
    waitbar(n1/uLen,h);
    for n2 = n1+1:uLen,
        J(n1,n2) = jaccardDist(Set{n1},Set{n2});
    end
end
delete (h)

toc


%% Ex3

tic
minhash = zeros(1,100);
p = 1000;
while isprime(p) == 0
    p = p + 1;
end

h = waitbar(0,'Hashing...');
for i=1:100
    waitbar(i/uLen,h)
    a = floor(1 + rand(1,100) * (p - 1));
    c = floor(rand(1,100) * p);
    for u = 1:uLen
        films = Set{u};
        hm = p;
        for j = 1:length(films)
            hm = minHash(hm,a,j,c,p);
        end
    end
end

toc
close(h)

save('signatures.txt','hm','-ascii');

% Ex4 

threshold = 0.4

SimilarUsers = zeros(1,3);

tic

k = 1;
h = waitbar(0,'Finding similar pairs...');

for n1 = 1:uLen,
    waitbar(n1/uLen,h)
    for n2 = n1+1:uLen,
        if J(n1,n2) <= threshold
            SimilarUsers(k,:) = [users(n1) users(n2) J(n1,n2)]
            k = k+1;
        end
    end
end

toc
close(h)

save('similarusers.txt','SimilarUsers','-ascii');
