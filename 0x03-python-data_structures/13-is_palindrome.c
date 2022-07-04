#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of singly linked list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *temp = *head;
	int head_val, tail_val;

	/* empty linked list condition */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* get head value for comparison */
	head_val = (*head)->n;
	while (current)
	{
		/* look ahead to see if next node from current is the tail */
		if ((current->next)->next == NULL)
		{
			/* assign val of tail for comparison */
			tail_val = (current->next)->n;
			/* update tail to current */
			current->next = NULL;

			if (head_val != tail_val)
				return (0);

			/* update head (N/B: temp is serving as the head) */
			temp = temp->next;
			/* is a palindrome if head is NULL */
			if (!temp)
				break;

			/* update head_val and current for traversing */
			head_val = temp->n;
			current = temp;
		}
		else
			current = current->next;
	}
	return (1);
}
