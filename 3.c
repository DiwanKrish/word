#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t mutex;

void *my_function(void *arg)
{
    int *num = (int *)arg;

    pthread_mutex_lock(&mutex);

    printf("Thread %d: Running\n", *num);
    sleep(1);
    printf("Thread %d: Finished\n", *num);

    pthread_mutex_unlock(&mutex);

    pthread_exit(NULL);
}

int main()
{
    pthread_t thread1, thread2;
    int t1 = 1, t2 = 2;

    pthread_mutex_init(&mutex, NULL);

    pthread_create(&thread1, NULL, my_function, (void *)&t1);
    pthread_create(&thread2, NULL, my_function, (void *)&t2);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    pthread_t detached_thread;
    pthread_create(&detached_thread, NULL, my_function, (void *)&t1);
    pthread_detach(detached_thread);

    sleep(2);

    pthread_mutex_destroy(&mutex);

    printf("Main thread exiting\n");

    return 0;
}
