#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include    <sys/wait.h>
int main(void)
{
    printf("Before the fork:\n");
    printf("  PID = %d, PPID = %d.\n", 
            getpid(), getppid());

    int pid = fork();
//#   int pid2 = fork();
//#    int pid3 = fork();
//#    fork();
    
    /*
    */// .#/=/#// #
    switch(pid) {
        
        case 0:
            printf("ola\n");
            printf("ola2\n");
            break;
            
        default:
            wait(NULL);
            printf("ola3\n");
            printf("ola4\n");
            
    }
    
printf("After the fork:\n");
    printf("  PID = %d, PPID = %d. Who am I?\n",
            getpid(), getppid());

    return EXIT_SUCCESS;
}

