#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - Prints all elements of a linked list.
 * @h: Pointer to the head of the list.
 * Return: Number of nodes in the list.
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n = 0; // Number of nodes

    current = h;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return n;
}

/**
 * add_nodeint_end - Adds new node at the end of a linked list.
 * @head: Pointer to point the first node of the linked list.
 * @n: Integer 
 * Return: new element or NULL if it fails.
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new_node;
    listint_t *current;

    current = *head;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;

    new_node->n = n;
    new_node->next = NULL;

    if (*head == NULL)
        *head = new_node;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new_node;
    }

    return new_node;
}

/**
 * free_listint - Frees a listint_t list.
 * @head: Pointer to the list to be freed.
 * Return: void.
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
