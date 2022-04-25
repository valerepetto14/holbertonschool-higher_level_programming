#include "lists.h"
/**
 *check_cycle - check cycle
 *@list: list
 *Return: 0 or 1
 **/
int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	listint_t *aux1 = list;

	if (!list)
		return (0);
	while (1)
	{
		if (aux->next != NULL && aux1->next->next != NULL)
		{
			aux = aux->next;
			aux1 = aux1->next->next;
			if (aux1 == aux)
				return (1);
		}
		else
			return (0);
	}
}
