#include <stdio.h>

int main()
{
    int frames, pages, i, j, k, page_faults = 0;

    printf("Enter number of frames: ");
    scanf("%d", &frames);

    printf("Enter number of pages: ");
    scanf("%d", &pages);

    int frame[frames], page[pages], recent[frames];

    for (i = 0; i < frames; i++)
    {
        frame[i] = -1;
        recent[i] = 0;
    }

    printf("Enter the page reference string:\n");
    for (i = 0; i < pages; i++)
    {
        scanf("%d", &page[i]);
    }

    int time = 0;

    for (i = 0; i < pages; i++)
    {
        int found = 0;

        for (j = 0; j < frames; j++)
        {
            if (frame[j] == page[i])
            {
                found = 1;
                time++;
                recent[j] = time;
                break;
            }
        }

        if (found == 0)
        {
            int lru_index = 0;
            int min_recent = recent[0];

            for (j = 1; j < frames; j++)
            {
                if (recent[j] < min_recent)
                {
                    min_recent = recent[j];
                    lru_index = j;
                }
            }

            frame[lru_index] = page[i];
            time++;
            recent[lru_index] = time;
            page_faults++;
        }

        printf("Frames after page %d: ", page[i]);

        for (k = 0; k < frames; k++)
        {
            if (frame[k] != -1)
                printf("%d ", frame[k]);
            else
                printf("- ");
        }

        printf("\n");
    }

    printf("\nTotal Page Faults = %d\n", page_faults);

    return 0;
}
