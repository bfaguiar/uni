#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <assert.h>
#include <stdarg.h>
#include <sys/types.h>
#include <sys/wait.h>
#include "process.h"

// process

pid_t pfork(void)
{
   pid_t res = fork();
   check_error(res);
   return res;
}

pid_t pwait(int *status)
{
   pid_t res = wait(status);
   check_error(res);
   return res;
}

pid_t pwaitpid(pid_t pid, int *status, int options)
{
   pid_t res = waitpid(pid, status, options);
   check_error(res);
   return res;
}

// System V - shared memory

int pshmget(key_t key, size_t size, int shmflg)
{
   assert(size > 0);

   int res = shmget(key, size, shmflg);
   check_error(res);
   return res;
}

int pshmctl(int shmid, int cmd, struct shmid_ds *buf)
{
   int res = shmctl(shmid, cmd, buf);
   check_error(res);
   return res;
}

void *pshmat(int shmid, const void *shmaddr, int shmflg)
{
   void *res = shmat(shmid, shmaddr, shmflg);
   pcheck_error(res);
   return res;
}

void pshmdt(const void *shmaddr)
{
   int st = shmdt(shmaddr);
   check_error(st);
}

// System V - semaphores

int psemget(key_t key, int nsems, int semflg)
{
   assert(nsems > 0);

   int res = semget(key, nsems, semflg);
   check_error(res);
   return res;
}

int psemctl(int semid, int semnum, int cmd, ...)
{
   va_list vargs;
   va_start(vargs, cmd);
   int res = semctl(semid, semnum, cmd, vargs);
   check_error(res);
   va_end(vargs);
   return res;
}

void psemop(int semid, struct sembuf *sops, size_t nsops)
{
   int st = semop(semid, sops, nsops);
   check_error(st);
}

// POSIX semaphores

