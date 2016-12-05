/* whoami.c - a simple implementation of whoami utility */
#include <pwd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

/*
void test_fn (int level, char *name) 
{
	if (level == 0 && name == NULL)
		fprintf (stderr, "I don't know!\n");
		return;
	else {
		return;
	}

}
*/

int
who_am_i (void)
{
	struct passwd *pw;
	char *user = NULL;

	pw = getpwuid (geteuid ());
	if (pw)
	 user = pw->pw_name;
	else if ((user = getenv ("USER")) == NULL)
	 {
	   fprintf (stderr, "I don't know!\n");
	   return 1;
	 }
	printf ("%s\n", user);
	//test_fn();
	return 0;
}

int
main_whoami (int argc, char **argv)
{
	if (argc > 1)
	 {
	   fprintf (stderr, "usage: whoami\n");
	   return 1;
	 }
	return who_am_i ();
}
