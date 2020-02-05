#ifndef PROCESS_H
#define PROCESS_H

#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>

//#define EXCEPTION_POLICY
//#define EXIT_POLICY // DEFAULT

#ifdef EXCEPTION_POLICY
#define check_error(status) \
   if (status == -1) \
      throw errno
#define pcheck_error(status) \
   if (status == (void*)-1) \
      throw errno
#else
#define check_error(status) \
   if (status == -1) \
      do { \
         fprintf (stderr, "%s at \"%s\":%d: %s\n", \
                  __FUNCTION__ , __FILE__, __LINE__, strerror (errno)); \
         *((int*)0) = 0; \
         abort (); \
      } while (0)
#define pcheck_error(status) \
   if (status == (void*)-1) \
      do { \
         fprintf (stderr, "%s at \"%s\":%d: %s\n", \
                  __FUNCTION__ , __FILE__, __LINE__, strerror (errno)); \
         *((int*)0) = 0; \
         abort (); \
      } while (0)
#endif

// process
//
pid_t pfork(void);
pid_t pwait(int *status);
pid_t pwaitpid(pid_t pid, int *status, int options);

// System V - shared memory

int pshmget(key_t key, size_t size, int shmflg);
int pshmctl(int shmid, int cmd, struct shmid_ds *buf);
void *pshmat(int shmid, const void *shmaddr, int shmflg);
void pshmdt(const void *shmaddr);

// System V - semaphores

int psemget(key_t key, int nsems, int semflg);
int psemctl(int semid, int semnum, int cmd, ...);
void psemop(int semid, struct sembuf *sops, size_t nsops);

// POSIX semaphores

#endif
