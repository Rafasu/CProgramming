//Extra Long Factorials.
//HackerRank
//Input consist of a single integer N, where 1 <= N <= 100
//Output: Factorial of N. 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std ;

int main(){
	vector <int> factorial ;
	int carry, digits, number, N ;

	//Initialization of vector.
	carry = 0 ;
	factorial.push_back(1) ;
	digits = 1 ;

	cin >> N ;

	//First Cycle iterates for the factorial.
	for(int i = 1 ; i <= N ; i++){
		//Second Cycle iterates the vector and makes operations.
		for(int j = 0 ; j < digits ;  j++){
			number = factorial[j] * i + carry ;
			factorial[j] = number % 10 ;
			carry = number /10 ;
		}

		//If there's a carry.
		while(carry > 0){
			factorial.push_back(carry%10) ;
			carry = carry/10 ;
			digits++ ;
		}
	}

	//Prints out the solution
	for(int i = digits - 1 ; i >= 0 ; i--){
		cout <<  factorial[i] ;
	}

	return 0 ;

}
