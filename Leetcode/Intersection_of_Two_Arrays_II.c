#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int *intersect(int *nums1, int nums1Size, int *nums2, int nums2Size, int *returnSize)
{
    qsort(nums1, nums1Size, sizeof(int), cmpfunc);
    qsort(nums2, nums2Size, sizeof(int), cmpfunc);
    int i, j = 0;
    int *result = (int *)malloc(sizeof(int));
    while (i < nums1Size && j < nums2Size)
    {
        if (*(nums1 + i) < *(nums2 + j))
        {
            i++;
        }
        else if (*(nums1 + i) == *(nums2 + j))
        {
            *returnSize += 1;
            result = realloc(result, *returnSize * sizeof(int));
            *(result + *returnSize - 1) = *(nums1 + i);
            i++;
            j++;
        }
        else
        {
            j++;
        }
    }
    return result;
}

int main(int argc, char *argv[])
{
    int nums1[] = {1, 2, 2, 1};
    int nums2[] = {2, 2};
    int returnSize = 0;
    int *result = intersect(nums1, sizeof(nums1) / sizeof(int), nums2, sizeof(nums2) / sizeof(int), &returnSize);
    for (int i = 0; i < returnSize; i++)
    {
        printf("%d", *(result + i));
    }
    return 0;
}
