#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
  * reverse_listint - reverses linked list
  * @head: head of list
  * Return: start of reversed list
  */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;

	return (*head);
}

/**
 * is_palindrome - checks is list is plindrome
 *
 * @head: head of list
 *
 * Return: 1 or 0 if not a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *lead, *mid, *tail, *tmp;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tail = *head;
	lead = *head;

	while (tail && lead->next && lead->next->next)
	{
	tail = tail->next;
	lead = lead->next->next;
	}
	if (lead->next == NULL)
	{
		mid = tail;
	}
	else
	{
		mid = tail->next;
	}

	mid = reverse_listint(&mid);
	tmp = *head;

	while (mid)
	{
		if (mid->n == tmp->n)
		{
			mid = mid->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}
	return (1);
}
