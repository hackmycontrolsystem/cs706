/* Copyright 1999-2005 The Apache Software Foundation or its licensors, as
 * applicable.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @file os2/os.h
 * @brief This file in included in all Apache source code. It contains definitions
 * of facilities available on _this_ operating system (HAVE_* macros),
 * and prototypes of OS specific functions defined in os.c or os-inline.c
 *
 * @defgroup APACHE_OS_OS2 os2
 * @ingroup  APACHE_OS
 * @{
 */

#ifndef APACHE_OS_H
#define APACHE_OS_H

#define PLATFORM "OS/2"

/* going away shortly... */
#define HAVE_DRIVE_LETTERS
#define HAVE_UNC_PATHS
#define CASE_BLIND_FILESYSTEM

#endif   /* ! APACHE_OS_H */
/** @} */
