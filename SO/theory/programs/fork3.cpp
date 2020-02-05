#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
    printf("Before the fork:\n");
    printf("  PID = %d, PPID = %d.\n", 
            getpid(), getppid());

    int ret = fork();

    if (ret == 0)
    {
        printf("I'm the child:\n");
        printf("  PID = %d, PPID = %d\n", 
            getpid(), getppid());
        int count = 0;
        printf("Child Exiting...\n");
        
    }
    
    else
    {
        printf("I'm the parent:\n");
        printf("  PID = %d, PPID = %d\n", 
            getpid(), getppid());
        printf("Parent Exiting...\n");
        exit(0);
    }

    return EXIT_SUCCESS;
}

