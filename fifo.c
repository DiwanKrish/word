#include <stdio.h>

int main()
{
    int frames, pages, i, j, k, page_faults = 0;

    printf("Enter number of frames: ");
    scanf("%d", &frames);

    printf("Enter number of pages: ");
    scanf("%d", &pages);

    int frame[frames], page[pages];

    for (i = 0; i < frames; i++)
    {
        frame[i] = -1;
    }

    printf("Enter the page reference string:\n");
    for (i = 0; i < pages; i++)
    {
        scanf("%d", &page[i]);
    }

    int index = 0;

    for (i = 0; i < pages; i++)
    {
        int found = 0;

        for (j = 0; j < frames; j++)
        {
            if (frame[j] == page[i])
            {
                found = 1;
                break;
            }
        }

        if (found == 0)
        {
            frame[index] = page[i];
            index = (index + 1) % frames;
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
