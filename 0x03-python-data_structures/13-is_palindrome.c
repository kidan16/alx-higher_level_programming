#include <stdlib.h>
#include <stdio.h>
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
	listint_t *fill;
	int i, j = 0, v = 0;
	int *array;

	current = *head;
	fill = *head;

	if (*head == NULL || head == NULL)
		return (1);

	while (current->next != NULL)
	{
		current = current->next;
		j++;
	}

	array = malloc(sizeof(int) * (j + 2));
	if (array == NULL)
		return (NULL);

	while (fill->next != NULL)
	{
		array[v] = fill->n;
		fill = fill->next;
		v++;
	}
	array[v] = fill->n;

	for (i = 0, j; i < j; i++, j--)
	{
		if (array[i] != array[j])
			return (0);
	}

	return (1);
}
