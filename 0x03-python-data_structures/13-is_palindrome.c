#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks a list is a palindrome or not
 * @head: a pointer to a pointer to the first element
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j = 0;
	int List[];

	current = *head;

	if (*head == NULL)
		return (1);

	while (current -> next != NULL)
	{
		List[j] = current->n;
		current = current->next;
		j++;
	}
	List[j] = current->n;

	for (i = 0, j; i < j; i++, j--)
	{
		if (List[i] != List[j])
			return (0);
	} 

	return (1);
}
