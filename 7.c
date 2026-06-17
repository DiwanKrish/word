#include <stdio.h>

int main()
{
    int n, m;

    printf("Enter no. of processes: ");
    scanf("%d", &n);

    printf("Enter number of resource types: ");
    scanf("%d", &m);

    int alloc[n][m];
    int max[n][m];
    int avail[m];

    printf("\nEnter allocation matrix:\n");
    for (int i = 0; i < n; i++)
    {
        printf("Process %d: ", i);
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &alloc[i][j]);
        }
    }

    printf("\nEnter maximum matrix:\n");
    for (int i = 0; i < n; i++)
    {
        printf("Process %d: ", i);
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &max[i][j]);
        }
    }

    printf("\nEnter available resources:\n");
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &avail[i]);
    }

    int need[n][m];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            need[i][j] = max[i][j] - alloc[i][j];
        }
    }

    int finish[n];

    for (int i = 0; i < n; i++)
    {
        finish[i] = 0;
    }

    int safeSeq[n];
    int count = 0;

    while (count < n)
    {
        int found = 0;

        for (int i = 0; i < n; i++)
        {
            if (!finish[i])
            {
                int j;

                for (j = 0; j < m; j++)
                {
                    if (need[i][j] > avail[j])
                        break;
                }

                if (j == m)
                {
                    for (int k = 0; k < m; k++)
                    {
                        avail[k] += alloc[i][k];
                    }

                    safeSeq[count++] = i;
                    finish[i] = 1;
                    found = 1;
                }
            }
        }

        if (!found)
        {
            printf("\nSystem is not in a safe state (Deadlock may occur).\n");
            return 1;
        }
    }

    printf("\nSystem is in a Safe State.\nSafe Sequence is: ");

    for (int i = 0; i < n; i++)
    {
        printf("P%d ", safeSeq[i]);
    }

    printf("\n");

    return 0;
}
