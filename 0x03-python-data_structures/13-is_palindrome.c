#include "lists.h"
/**
*is palindrome - verifica si es palindrome
*@head: lista
*Return: int
**/
int is_palindrome(listint_t **head)
{
	int iterpar = 0, len = 0, ultimo;
	listint_t *aux = *head, *auxpar = *head;
	listint_t *recorrer = *head;

	if (*head == NULL)
		return (1);
	while (aux->next != NULL)
	{
		aux = aux->next;
		len++;
	}
	len++;
	ultimo = len;
	if (len % 2 == 0)
	{
		while (iterpar < len / 2 && auxpar->next != NULL)
		{
			if (auxpar->n == indice_list(recorrer, ultimo))
			{
				ultimo = ultimo - 1;
				auxpar = auxpar->next;
				iterpar++;
			}
			else
				return (0);
		}

	}
	else if (len % 2 != 0)
	{

	}
	return (1);
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

	while (iter < indice && aux->next != NULL)
	{
		aux = aux->next;
		iter++;
	}
	printf("%d\n",aux->n);
	return (aux->n);
}
