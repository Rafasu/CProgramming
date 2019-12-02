vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
    vector<int> results;
    // DO STUFF HERE AND POPULATE result
    int rows = A.size() ; ;
    int columns = A[0].size() ;
    int top, bottom , left, right, i, j ;
    top = 0;
    bottom = rows - 1 ;
    left = 0;
    right = columns -1 ;
    //Caso Base
  
    while(top <= bottom && left <= right ){
        //First row
        for(j = left; j <= right; j++){
            results.push_back(A[top][j]);
        }
        top++;
        
        for(i = top ; i <= bottom ; i++ ){
            results.push_back(A[i][right]);
        }
        right--;
        
        if(top <= bottom){
            for(j = right; j >= left ; j--){
                results.push_back(A[bottom][j]);
            }
            bottom--;
        }
        
        if(left <= right){
            for(i = bottom ; i >= top; i-- ){
                results.push_back(A[i][left]);
            }
            left++;
        }
        
        
    }
  
    return results;
}
   
