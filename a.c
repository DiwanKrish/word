#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>
#include<sys/types.h>
#include<signal.h>

void execute_execvp()
{
    char *args[] = {"ls", "-l", NULL};

    execvp(args[0], args);

    perror("execvp failed");
    exit(1);
}

int main()
{
    pid_t pid;

    pid = fork();

    if(pid < 0)
    {
        perror("fork failed");
    }

    else if(pid == 0)
    {
        printf("Child process (PID:%d) executing execvp\n", getpid());

        execute_execvp();   // IMPORTANT
    }

    else
    {
        printf("Parent process (PID:%d) waiting for child\n", getpid());

        wait(NULL);

        printf("Child process finished, parent continues\n");

        printf("Killing parent process\n");

        kill(getpid(), SIGTERM);
    }

    return 0;
}
