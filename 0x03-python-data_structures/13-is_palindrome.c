#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * compare_lists - Compares two linked lists for equality.
 * @head1: A pointer to the head of the first linked list.
 * @head2: A pointer to the head of the second linked list.
 *
 * Return: If the linked lists are equal - 1.
 *         If the linked lists are not equal - 0.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = *head;
	listint_t *second_half, *midnode = NULL;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		midnode = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL;
	reverse_listint(&second_half);

	result = compare_lists(*head, second_half);

	if (midnode != NULL)
	{
		prev_slow->next = midnode;
		midnode->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return (result);
}
