#include "lists.h"
/**
 * check_cycle - main
 * @list: puntero a una lista
 * Return: 0 or 1
 **/
int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	listint_t *aux1 = list;

	if (!list)
		return (0);
	while (aux1)
	{
		if (aux && aux1)
		{
			aux = aux->next;
			aux1 = aux1->next->next;
				if (aux == aux1)
					return (1);
		}
		else
			return (0);
	}
	return (0);
}
