//type creation
typedef struct Node Node;

// node structure declaration
struct Node {
    int data;
    Node *prev;
    Node *next;
};
Node* fillNode(int length, char *argv[]);
void MergeSort(Node **first);
Node* joinLists(Node *a, Node *b);
void split(Node *start, Node **front, Node **back);
void printNodes(Node *first);