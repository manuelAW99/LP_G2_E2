#include<iostream>
#include<memory>

using namespace std;
template<typename T>
class Node 
{
  public:
    T data;
    shared_ptr< Node<T> > previous;
    shared_ptr< Node<T> > next;
    Node(){};
    Node(T data): data(data){};
};
template<typename T>
class Double_Linked_List
{
  public:
    shared_ptr< Node<T> > head, tail;
    int size;
  public:
    Double_Linked_List(): size(0){};

    void Add(T data)
    {
      shared_ptr< Node<T> > temp (new Node<T>(data));
      
      
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
    T operator [](int index)
    {
      if (index >= size || index < size) throw "Index out of range";
      shared_ptr< Node<T> > temp;
      temp = head;
      int current = 0;

      while(index != current)
      {
        temp = temp.next;
        current++;
      }
      return temp.data;
    };
    void Remove (T removing)
    {
      shared_ptr< Node<T> > temp;
      temp.next = head;
      
      while (temp.data != removing)
        temp = temp.next;
      
      temp.previous.next = temp.next;
      temp.next.previous = temp.next;
    }
    void Remove_At (int index)
    {
      if (index >= size || index < size) throw "Index out of range";
      shared_ptr< Node<T> > temp;
      temp = head;
      int current = 0;

      while(index != current)
      {
        temp = temp.next;
        current++;
      }
      temp.previous.next = temp.next;
      temp.next.previous = temp.next;
    }
};

int main()
{
  Double_Linked_List<int> temp;
  temp.Add(2);
  int a = temp.head->data;
  cout << a << endl;
}