#include "lists.h"
/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: header of a linked list
* Return: 1 if it is a palindrome 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	int copy_list[3000];
	listint_t *aux = *head, *aux2 = *head;
	int len = 0;
	int i = 0;

	if (aux && aux->next != NULL)
	{
		while (aux)
		{
			len++;
			aux = aux->next;
		}

		while (aux2)
		{
			copy_list[i] = aux2->n;
			i++;
			aux2 = aux2->next;
		}
		len--;

		for (i = 0; i < len; i++)
		{
			if (copy_list[i] != copy_list[len])
				return (0);
			len--;
		}
	}
	return (1);
}
