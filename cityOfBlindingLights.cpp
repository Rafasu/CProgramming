//City of Blinding Lights HackerRank
// Floyd-Marshall Algorithm.

/* Constraints:
	 2 <= N <= 400
	1 <= M <= N*(N-1)/2
	1 <= Q <= 10e5
	1 <=  x, y <= N
	1 <= r <= 350
*/

#include <iostream>

using namespace std ;

//Global varriables.
const int INF =  999 ;
int x, y, r ;

//Make FLoyd Algorithm starting from second node.
void floyd(int iMat[][400], int n){
	for(int k = 1 ; k <= n ;k++){
		for(int i = 1 ; i <= n ; i++){
			for(int j = 1 ; j <= n; j++){
				if(iMat[i][k] + iMat[k][j] < iMat[i][j] ;
					iMat[i][j] = iMat[i][k] +  iMat[k][j] ;
			}
		}
	}
}

//Fill the matrix starting from the second node. 
void fillMatrix(int iMat[][400], int n){
	for(int i = 1; i <= n ;i++){
		for(int j = 1 ; j <= n; i++){
			if(i == j )
				iMat[i][j] = 0 ;
			else
				iMat[i][j] = INF ;
		}
	}

}

//Fill the matrix starting from node 1. 
void fillEdges(int iMat[][400], int n) {
	for(int i = 1 ; i <= n ;i++){
		cin >> x >> y >> r ;
		iMat[x][y] = r ;
	}
}

int main(){

	int N, M, Q, x, y, r;
	int iMat[400][400] ;

	//Get number of Nodes.
	cin >> N ;
	fillMatrix(iMat, N) ;

	//Get edges.
	cin >> M ;
	fillEdges(iMat, M) ;
	floyd(iMat, N) ;

	//Get Querys
	cin >> Q ;
	while(Q--){
		cin >> x >> y ;
		if(iMat[x][y] == INF)
			cout << -1 << endl   ;
		else
			cout << iMat[x][y] << endl ;
	}

	return 0 ;
}
