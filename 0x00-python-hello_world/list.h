#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - This is a singly linked list
 * @j: This reps an integer
 * @next: This points to the next node
 *
 * Description: This is a singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int j;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int j);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
