#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - verify whether a linked list -
 * is a palindrome
 * @head: header of the linked list
 * Return: 1 for palindrom, 0 if not a palindrome
**/

int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
{
return (1);
}

listint_t *slow_ptr;
listint_t *fast_ptr;
listint_t *prev_node = NULL;
listint_t *next_node;

for (slow_ptr = *head, fast_ptr = *head;
fast_ptr != NULL && fast_ptr->next != NULL;
fast_ptr = fast_ptr->next->next)
{
prev_node = slow_ptr;
slow_ptr = slow_ptr->next;
}

if (fast_ptr != NULL)
{
slow_ptr = slow_ptr->next;
}

prev_node->next = NULL;
prev_node = NULL;

for (; slow_ptr != NULL; slow_ptr = next_node)
{
next_node = slow_ptr->next;
slow_ptr->next = prev_node;
prev_node = slow_ptr;
}

listint_t *part_one_ptr = *head;
listint_t *part_two_ptr = prev_node;

for (; part_one_ptr != NULL && part_two_ptr != NULL;
part_one_ptr = part_one_ptr->next,
part_two_ptr = part_two_ptr->next)
{
if (part_one_ptr->n != part_two_ptr->n)
{
return (0);
}
}

return (1);
}
