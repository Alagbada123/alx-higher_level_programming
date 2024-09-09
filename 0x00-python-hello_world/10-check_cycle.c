#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of the linked list
 *
 * Description - check for lop in LL
 * Return: 1 if cycled, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
