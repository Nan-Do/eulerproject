
#include <iostream>
#include <vector>
#include <set>

#include <math.h>
#include <stdio.h>
#include <string.h>

std::set<long> getSieveOfEratosthenes ( long max )
{
  std::vector<bool> primes(max, true);
  long sz = primes.size();

  for ( long i = 3; i < sz ; i+=2 )
    if ( primes[i] ) 
      for ( long j = i * i; j < sz; j+=i)
        primes[j] = false;

  std::set<long> ret;
  //ret.reserve(primes.size());
  //ret.push_back(2);
  ret.insert(2);

  for ( long i = 3; i < sz; i+=2 )
    if ( primes[i] )
      ret.insert(i);

  return ret;
}

std::vector<long> getDiagonals( long n )
{
    long last = 1;
    std::vector<long> ret;
    ret.push_back(1);
    
    for (int x = 2; x < n; x += 2)
    {
        for (int y = 0; y < 4; y++)
        {
            last += x;
            ret.push_back(last);
        }
    }
    
    return ret;
}
    


int main(){
    std::set<long> primes = getSieveOfEratosthenes(800000000);
    std::vector<long> diagonals;
    std::vector<long>::iterator it;
    double ratio = 0.0;
    long number_of_primes = 0;
    long matrix_side = 22801;
    
    while (1){
        number_of_primes = 0;
        diagonals = getDiagonals(matrix_side);
          
        for (it=diagonals.begin(); it!=diagonals.end(); it++)
            if (primes.find(*it) != primes.end())
                number_of_primes++;

        ratio = number_of_primes / (double) diagonals.size();
        std::cout << "Length: " << matrix_side << " Ratio: " << ratio <<  std::endl;
        
        if (ratio < 0.1) break;
        matrix_side += 2;
    }
}
