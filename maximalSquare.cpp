//Leetcode 221: Maximal Square.
//Dynamic Programming problem

//We need a state matrix.

class Solution{
public: 
	int maximalSquare(vector <vector <char>> &matrix) {
		if(matrix.size())
			return 0 ;
		int row, col ;
		row = matrix.size() ;
		col = matrix[0].size() ;

		vector <vector<int>> state(row, vector<int>(col)) ;
		

	}


} ;
