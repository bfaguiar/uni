#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
//#    printf("Before the fork:\n");
//#    printf("  PID = %d, PPID = %d.\n",
//#            getpid(), getppid());

    int ret = fork();

//#printf("After the fork:\n");
//#    printf("  PID = %d, PPID = %d, ret = %d\n",
//#getpid(), getppid(), ret);
    
    /*
    */
    
    switch(ret) {
        case 0:
            printf("filho");
           
        case 1:
            printf("idk bro I am a strong person and a good one trust!@ i Love yoU");
        default:
            printf("pai");
    }
     
   /*
// #if (ret == 0)
// #        printf("filho");
#    else printf("pai"); ?==
    */
    return EXIT_SUCCESS;
}

