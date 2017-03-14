//More Voting Algorithm. 

class solution{
public: 
	int majorityElement(vector <int> &nums){
		int iMajor, iCont = 0; 
		int i, n =  nums.size() ;

		for( i  = 0; i < n ; i++){
			if(iCont == 0){
				iMajor = nums[i] ;
				iCont++ ;
			}
			else if(iMajor == nums[i] ;
				iCont++ ;
			else
				iCont-- ;

		} 
		
		//Because the problem says that there's a majority element
		//There's no need to check if iMajor is the majority element
		return iMajor ;

	}

};
