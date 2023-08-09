#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct list_s - it is a singly linked list.
 * @num: the integer.
 * @nextn: points to next node.
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif
