#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
  * check_cycle - find loop in loop
  * @list: start of linked list
  * Return: Loop Location or NULL
  */


int check_cycle(listint_t *list)
{
	listint_t *t = list;
	listint_t *r = list;

	while (t && r->next && r->next->next)
	{
		if ((t == r->next) || (t == r->next->next))
		{
			return (1);
		}
		t = t->next;
		r = r->next->next;
	}
	return (0);
}
