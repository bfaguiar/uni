/**
 *  \author ...
 *  \tester ...
 */

#include "freelists.h"
#include "freelists.bin.h"

#include "probing.h"
#include "exception.h"

#include <errno.h>

/*
 * Even if some of them are not functionally necessary,
 * the following dictates must be obyed by the implementation:
 * - after every reference is transferred, 
 *      the previous location should be filled with NullReference
 */
void soDeplete(void)
{
    soProbe(541, "soDeplete()\n");
    soDepleteBin();
}
