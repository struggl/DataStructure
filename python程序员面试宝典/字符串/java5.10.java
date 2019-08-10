public void palindrome(String str)
{
	if (str==null || str.length()==0)
		return;
	char chs[] = str.toCharArray();
	int max_len = 0
	boolean f[i][j] = new boolean[chs.length][chs.length];
	for (int j=0;j<str.length();j++)
	{	
		int i=0;
		f[j][j] = true;
		for (;i<j;i++)
		{
			f[i][j] = (chs[j]==chs[i] && (j-i<2||j>0 && f[i+1][j-1]));
			if (f[i][j])
			{
				max_len = Math.max(max_len,j-i+1);
			}
		}
	}
	System.out.println(max_len);
}

