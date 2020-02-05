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
## @deftypefn {Function File} {@var{retval} =} function1 (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Bruno <bruno@bruno>
## Created: 2017-09-25

function [probSimulacao] = function1 ( N, p, k, n)

% N = 1e5; % numero de experiencias
% p = 0.5; % probabilidade de cara
% k = 2;   % numero de caras
% n = 3;   % numero de lancamentos

lancamentos = rand(n, N) > p;
sucessos = sum(lancamentos) == k;
probSimulacao = sum(sucessos)

stem(n, sucessos)

endfunction
