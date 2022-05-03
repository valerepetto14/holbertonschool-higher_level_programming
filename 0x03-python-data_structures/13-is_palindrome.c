#include "lists.h"
/**
*is_palindrome - verifica si es palindrome
*@head: lista
*Return: int
**/
int is_palindrome(listint_t **head)
{
	int iter = 0, len = 0, ultimo;
	listint_t *aux = *head, *auxpar = *head, *recorrer = *head;

	if (head == NULL) /* non-existing list is not */
		return (0);
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL) /* one node list returns true */
		return (1);
	while (aux->next != NULL)
	{
		aux = aux->next;
		len++; }
	len++;
	ultimo = len;
	if (len % 2 == 0)
	{
		while (iter < len / 2)
		{
			if (auxpar->n == indice_list(recorrer, ultimo))
			{
				ultimo = ultimo - 1;
				auxpar = auxpar->next;
				iter++; }
			else
				return (0); }
	}
	else
	{
		while (iter < (len / 2) - 1)
		{
			if (auxpar->n == indice_list(recorrer, ultimo))
			{
				ultimo = ultimo - 1;
				auxpar = auxpar->next;
				iter++;
			}
			else
				return (0); }
	} return (1);
}

/**
 *indice_list - printea
 *@head: pointer
 *@indice: int
 *Return: int
 **/
int indice_list(listint_t *head, int indice)
{
	listint_t *aux = head;
	int iter = 0;

	indice--;
	while (iter < indice && aux->next != NULL)
	{
		aux = aux->next;
		iter++;
	}
	return (aux->n);
}
