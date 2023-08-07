#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list node */
struct listint_s {
    int n;
    struct listint_s *next;
};
typedef struct listint_s listint_t;

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list) {
    listint_t *slow, *fast;

    if (list == NULL)
        return 0;

    slow = list;
    fast = list->next;

    while (fast != NULL && fast->next != NULL) {
        if (fast == slow)
            return 1;
        slow = slow->next;
        fast = fast->next->next;
    }

    return 0;
}

int main(void) {
    listint_t *list = NULL;

    // Creating a linked list with a cycle for testing purposes
    list = malloc(sizeof(listint_t));
    if (list == NULL)
        return 1;
    list->n = 1;

    list->next = malloc(sizeof(listint_t));
    if (list->next == NULL) {
        free(list);
        return 1;
    }
    list->next->n = 2;
    list->next->next = list; // Create a cycle by pointing back to the head

    int result = check_cycle(list);
    printf("Result: %d\n", result);

    // Clean up: Free the allocated memory
    free(list->next);
    free(list);

    return 0;
}
