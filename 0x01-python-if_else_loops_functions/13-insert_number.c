#include "lists.h"
/**
 *insert_node - function add node
 *@head: lista
 *@number: int
 *Return: lista
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *aux = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
	}
	else
	{
		while (aux->next->n < number)
			aux = aux->next;
		new_node->next = aux->next;
		aux->next = new_node;
	}

	return (*head);
}
