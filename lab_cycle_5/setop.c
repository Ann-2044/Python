#include<stdio.h>
#include<stdlib.h>

#define MAX_SIZE 32 
const int UNIVERSAL_SET = (1 << MAX_SIZE) - 1;

void add(int *set, int element) {
    if (element >= 0 && element < MAX_SIZE) {
        *set |= (1 << element);
    } else {
        printf("Error: Element %d is out of valid range (0-31).\n", element);
    }
}


void remove_element(int *set, int element) {
    if (element >= 0 && element < MAX_SIZE) {
        *set &= ~(1 << element);
    } else {
        printf("Error: Element %d is out of valid range (0-31).\n", element);
    }
}
int intersection_set(int set1, int set2) {
    return set1 & set2;
}

int difference_set(int set1, int set2) {
    return set1 & ~set2;
}


int complement_set(int set) {
    return ~set & UNIVERSAL_SET; 
}

void display_set(int set) {
    printf("{ ");
    for (int i = 0; i < MAX_SIZE; i++) {
        if (set & (1 << i)) {
            printf("%d ", i);
        }
    }
    printf("}\n");
}

int main() {
    int set1 = 0, set2 = 0, n1, n2, element, operation;

    
    printf("Enter the number of elements in Set 1: ");
    scanf("%d", &n1);
    printf("Enter the elements of Set 1: ");
    for (int i = 0; i < n1; i++) {
        scanf("%d", &element);
        add(&set1, element); 
    }
 printf("Set 1: ");
    display_set(set1);

    printf("Set 2: ");
    display_set(set2);

    
    do {
        printf("\nChoose an operation:\n");
        printf("1. Add element to Set 1\n");
        printf("2. Remove element from Set 1\n");
        printf("3. Union of Set 1 and Set 2\n");
        printf("4. Intersection of Set 1 and Set 2\n");
        printf("5. Difference of Set 1 and Set 2\n");
        printf("6. Complement of Set 1\n");
        printf("7. Exit\n");
        scanf("%d", &operation);

        switch (operation) {
            case 1:
                printf("Enter element to add to Set 1: ");
                scanf("%d", &element);
                add(&set1, element); 
                printf("Updated Set 1: ");
                display_set(set1);
                break;
case 2:
                printf("Enter element to remove from Set 1: ");
                scanf("%d", &element);
                remove_element(&set1, element); 
                printf("Updated Set 1: ");
                display_set(set1);
                break;
            case 3: {
                int union_result = union_set(set1, set2);
                printf("Union of Set 1 and Set 2: ");
                display_set(union_result);
                break;
            }
            case 4: {
                int intersection_result = intersection_set(set1, set2);
                printf("Intersection of Set 1 and Set 2: ");
                display_set(intersection_result);
                break;
            }
            case 5: {
                int difference_result = difference_set(set1, set2);
                printf("Difference (Set 1 - Set 2): ");
                display_set(difference_result);
                break;
 }
            case 6: {
                int complement_result = complement_set(set1);
                printf("Complement of Set 1: ");
                display_set(complement_result);
                break;
            }
            case 7:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice! Try again.\n");
        }
    } while (operation != 7);

    return 0;
}
