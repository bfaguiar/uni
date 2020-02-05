## Copyright (C) 2017 Bruno
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} lcg (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Bruno <bruno@bruno>
## Created: 2017-10-24

function [ArrayRetornar] = lcg (X0, a, c, m, N)
  
  XArray = zeros(1, N); % Cria um array de zeros com comprimento N.
  XArray(1) = X0;       % Primeiro Elemento de U(1) e' igual a X0;
  
  for i = 2:N+1         % Fazer uma sequencia de numeros de N+1 porque o Primeiro Elemento Nao Conta.
    XArray(i) = rem(((a*XArray(i-1) + c)), m);
  end
  
  ArrayRetornar = XArray(1,2:N+1);
  
endfunction