#include "lists.h"
/**
 *insert_node - function add node
 *@head: lista
 *@number: int
 *Return: lista
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *aux = *head, *anterior = NULL;

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
		while (aux->n < number && aux->next != NULL)
		{
			anterior = aux;
			aux = aux->next;
		}
		if (aux->next == NULL)
			aux->next = new_node;
		if (anterior == NULL)
		{
			new_node->next = *head;
			*head = new_node;
		}
		else
		{
		new_node->next = aux;
		anterior->next = new_node;
		}
	}
	return (*head);
}
