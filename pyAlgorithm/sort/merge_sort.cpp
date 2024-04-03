#include <iostream>
using namespace std;

int N,arr[1000001];
int *arr2;

void merge(int left, int right)
{
    printf("merge: %d %d\n",left, right);
	int mid = (left + right) / 2;

	int i = left; //arr 왼쪽배열 커서값
	int j = mid + 1; //arr 오른쪽 배열 커서값

	int k = left; //arr2 배열 커서 값
	while (i <= mid && j <= right)
	{
		if (arr[i] <= arr[j]) 
			arr2[k++] = arr[i++]; 
		else
			arr2[k++] = arr[j++];
	}

    //비교대상 없을 시,
	int tmp = i > mid ? j : i;
	
	while(k<=right) arr2[k++] = arr[tmp++];

    //arr2에 있는 값 arr에 복사
	for (int i=left; i<=right;i++){
        arr[i] = arr2[i];
        printf("%d ",arr[i]);
    } 
    printf("\n");
}

void merge_sort(int left,int right)
{
	int mid;
	if (left < right)
	{
		mid = (left + right) / 2; 
		merge_sort(left, mid);
		merge_sort(mid + 1, right);

        printf("%d %d\n",left, right);
		merge(left, right);
	}
}

int main()
{
	scanf("%d",&N);
	arr2 = new int[N];
	for (int i=0;i<N;i++) scanf("%d",&arr[i]);

	merge_sort(0, N - 1);

	for (int i=0;i<N;i++) printf("%d ",arr[i]) ;
}