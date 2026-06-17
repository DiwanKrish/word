#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5

sem_t forks[N];
sem_t mutex;

void *philosopher(void *num)
{
    int id = *(int *)num;

    while (1)
    {
        printf("Philosopher %d is thinking...\n", id);
        sleep(1);

        sem_wait(&mutex);

        sem_wait(&forks[id]);
        sem_wait(&forks[(id + 1) % N]);

        printf("Philosopher %d is eating...\n", id);
        sleep(2);

        printf("Philosopher %d finished eating.\n", id);

        sem_post(&forks[id]);
        sem_post(&forks[(id + 1) % N]);

        sem_post(&mutex);

        sleep(1);
    }

    return NULL;
}

int main()
{
    pthread_t threads[N];
    int ids[N];

    sem_init(&mutex, 0, 1);

    for (int i = 0; i < N; i++)
    {
        sem_init(&forks[i], 0, 1);
    }

    for (int i = 0; i < N; i++)
    {
        ids[i] = i;
        pthread_create(&threads[i], NULL, philosopher, &ids[i]);
    }

    for (int i = 0; i < N; i++)
    {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
