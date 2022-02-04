#include <stdlib.h>
#include <stdio.h>

int check(int *lst, int row)
{
	for (int i = 0; i < row; i++)
		if ((lst[i] == lst[row]) || (abs(lst[row] - lst[i]) == row - i))
			return (0);
	return (1);
}

int tracking(int *lst, int N, int row)
{
	int ret = 0;

	if (row == N)
		return (1);
	for (int i = 0; i < N; i++)
	{
		lst[row] = i;
		if (check(lst, row))
			ret += tracking(lst, N, row + 1);
	}
	return (ret);
}

int main(void)
{
	int N;
	int *lst;

	scanf("%d", &N);
	lst = (int *)malloc(sizeof(int) * N);
	printf("%d", tracking(lst, N, 0));
	return (0);
}


// result : OK
/*

<review> : maybe 4 or more

*/
