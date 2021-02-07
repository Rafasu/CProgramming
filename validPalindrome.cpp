//LeetCode
//Two Pointers. String
//125. Valid Palindrome


class Solution{
public: 
	bool isPalindrome(string s){
		int i, j, n = s.length() ;
		char cTemp ;
		string sAlfanum = "" ;
		
		//Caso Espacio:
		if(n == 0)
			return true ;
		//Copia caracteres Alfanumericos de un string a otro.
		for(int i = 0; i < n; i++){
			cTemp = tolower(s[i]) ;
			if(isalnum(cTemp))
				sAlfanum += cTemp ;
		}

		//Checa si el nuevo string es palindrome.
		i = 0; j = sAlfanum.length() - 1 ;
		while(i < j){
			if(sAlfanum[i] != sAlfanum[j])
				return false ;
			i++ ;
			j-- ;

		}
		return true ;

	}

};
