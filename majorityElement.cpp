//169. LeetCode

//Moore's Voting Algorithm.
//Notes: Assumptions: No empty vector. There's a majority element.

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
		return iMajor ;
	}
};
