/*
 * \author ...
 */

#include "syscalls.h"
#include "syscalls.bin.h"

#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <stdbool.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/statvfs.h>
#include <sys/stat.h>
#include <time.h>
#include <utime.h>
#include <libgen.h>
#include <string.h>


#include "syscalls.h"
#include "direntries.h"
#include "sbdealer.h"
#include "itdealer.h"
#include "ocdealer.h"
#include "czdealer.h"
#include "inodeattr.h"
#include "probing.h"
#include "exception.h"

/*
 *  \brief Change the name or the location of a file in the directory hierarchy of the file system.
 *
 *  It tries to emulate <em>rename</em> system call.
 *
 *  \param path path to an existing file
 *  \param newPath new path to the same file in replacement of the old one
 *
 *  \return 0 on success;
 *      -errno in case of error, being errno the system error that better represents the cause of failure
 */
int soRename(const char *path, const char *newPath)
{
    soProbe(227, "soRename(\"%s\", \"%s\")\n", path, newPath);

    try
    {
        char *path_1 = strdupa(path);
        char *dir_name_1 = dirname(strdupa(path_1));
        char *base_name_1 = basename(strdupa(path_1));


        char *path_2 = strdupa(newPath);
        char *dir_name_2 = dirname(strdupa(path_2));
        char *base_name_2 = basename(strdupa(path_2));

        uint32_t inode_pai_1,inode_pai_2,inDeleted,iRenamed;
        inode_pai_1 = NullReference;
        inode_pai_2 = NullReference;
        inDeleted = NullReference;
        iRenamed = NullReference;
        if (strlen(path)>PATH_MAX || strlen(newPath)>PATH_MAX)
        {
           throw SOException(ENAMETOOLONG, __FUNCTION__);
        }

        if (strlen(bn)>SOFS17_MAX_NAME || strlen(bn2)>SOFS17_MAX_NAME)
            throw SOException(ENAMETOOLONG, __FUNCTION__);

        if(strcmp(strdupa(path), strdupa(newPath))==0)
                return 0;

        soTraversePath(strdupa(base_name_1), &inode_pai_1);
        uint32_t ih1 = iOpen(inode_pai);

        soTraversePath(strdupa(base_name_2), &inode_pai_2);
        uint32_t ih2 = iOpen(inode_pai_2);

        soGetDirEntry(ih2, base_name_2, &inDeleted);

        if (inDeleted!=NullReference)
            soDeleteDirEntry(ih2, base_name_2, &inDeleted);

        if((iCheckAccess(ih1, W_OK) == false) || (iCheckAccess(ih2, W_OK) == false))
        {
               iSave(ih1);
               iSave(ih2);
               iClose(ih1);
               iClose(ih2);
               throw SOException(EACCES, __FUNCTION__);
        }
        soDeleteDirEntry(ih1, strdupa(base_name_1), &iRenamed);
        soAddDirEntry(ih2, base_name_2, iRenamed);

        uint32_t ih3 = iOpen(iRenamed);

        SOInode* inode = iGetPointer(ih3);

        if ((inode->mode & S_IFDIR)==S_IFDIR)
        {
            if(iCheckAccess(ih3, W_OK) == false)
            {
                iSave(ih1);
                iSave(ih2);
                iSave(ih3);
                iClose(ih1);
                iClose(ih2);
                iClose(ih3);
                throw SOException(EACCES, __FUNCTION__);
            }

            soDeleteDirEntry(ih3,"..",&inDeleted);
            soAddDirEntry(ih3,"..",inode_pai_2);
            iIncLnkcnt(ih2);
            iDecLnkcnt(ih1);
        }
        iSave(ih1);
        iSave(ih2);
        iSave(ih3);
        iClose(ih1);
        iClose(ih2);
        iClose(ih3);
        return 0;
        //soRenameBin(path, newPath);
    }
    catch(SOException & err)
    {
        return -err.en;
    }

    return 0;
}
