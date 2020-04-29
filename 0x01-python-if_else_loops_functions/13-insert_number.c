#include<stdio.h>
#include<stdlib.h>
#include "lists.h"

/**
 *insert_node - inserts node in order
 *@head: head of linked list
 *@number: num to be added to the node
 *Return: new node address or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_new;
listint_t *tmp;
listint_t *new;

new_new = malloc(sizeof(listint_t));

if (head == NULL)
return (NULL);

tmp = *head;

new_new->n = number;
new_new->next = NULL;

if (*head == NULL || tmp->n > number)
{
*head = new_new;
new_new->next = tmp;
return (*head);
}
while (tmp->next)
{
if (tmp->n < number && tmp->next->n < number)
tmp = tmp->next;
else
{
new = tmp->next;
tmp->next = new_new;
new_new->next = new;
return (*head);
}
}
tmp->next = new_new;

return (*head);
}
