#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

class Node
{
  public:
    void *data;
    Node *previous;
    Node *next;

};

class Double_Linked_List
{
  private:
    Node *head, *tail;
    int size;
  public:
    Double_Linked_List();//default constructor

    void Add(void *data)
    {
      Node *temp = (Node*)malloc(sizeof(Node));
      temp->data = data;
      if (size == 0)
      {
        head = temp;
        tail = temp;
        temp->previous = head;
        temp->next = tail;
        size++;
      }
      else
      {
        tail->next = temp;
        temp->previous = tail;
        tail = temp;
      } 
      
    };
    void* operator [](int index)
    {
      if (index >= size || index < size) throw "Index out of range";
      Node *temp = head;
      int current = 0;

      while(index != current)
      {
        temp = temp->next;
        current++;
      }
      return temp->data;
    };
    void Remove (void* removing)
    {
      Node *temp = (Node*)malloc(sizeof(Node));
      temp->next = head;
      
      while (&temp->data != &removing)
        temp = temp->next;
      
      temp->previous->next = temp->next;
      temp->next->previous = temp->next;
    }
    void Remove_At (int index)
    {
      if (index >= size || index < size) throw "Index out of range";
      Node *temp = head;
      int current = 0;

      while(index != current)
      {
        temp = temp->next;
        current++;
      }
      temp->previous->next = temp->next;
      temp->next->previous = temp->next;
    }
};