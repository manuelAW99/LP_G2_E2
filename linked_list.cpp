#include<iostream>
#include<memory>
#include <vector>
#include <algorithm>
#include <iterator>

template<typename T>
using sptr = std::shared_ptr<T>;
template<typename T>
class Node 
{
  public:
    T data;
    sptr < Node<T> > previous;
    sptr < Node<T> > next;
    Node(){};
    Node(T data): data(data){};
};
template<typename T>
class Double_Linked_List
{
  public:
    sptr < Node<T> > head, tail;
    int size;
  public:
    Double_Linked_List(): size(0){};

    Double_Linked_List(T data)
    {
      Add(data);
    }

    //Copy
    Double_Linked_List(const Double_Linked_List& list)
    {
      auto temp = list.head;
      while(temp != nullptr)
      {
        Add(temp.data);
        temp = temp.next;
      }
    }

    //Movement
    Double_Linked_List(Double_Linked_List&& list)
    {
      *this = move(list);
    }

    //By copy
    Double_Linked_List& operator= (Double_Linked_List& list)
    {
      head = nullptr;
      tail = nullptr;
      size = 0;

      auto temp = list.head;
      while(temp != nullptr)
      {
        Add(temp.data);
        temp = temp.next;
      }

    }
    //by Movement
    Double_Linked_List& operator= (Double_Linked_List&& list)
    {
      head = nullptr;
      tail = nullptr;
      size = 0;

      swap(head, list.head);
      swap(tail, list.tail);
      swap(size, list.size);  

    }

    Double_Linked_List(vector <T> list)
    {
      for_each(list.begin(), list.end(), [this](T n) {Add(n);});
    }

    Double_Linked_List(std::initializer_list<T> list)
    {
      for_each(list.begin(), list.end(), [this](T n) {Add(n);});
    }

    T operator [](int index)
    {
      if (index >= size || index < 0) throw "Index out of range";
      auto temp = head;
      int current = 0;

      while(index != current)
      {
        temp = temp.next;
        current++;
      }
      return temp.data;
    };

    void Add(T data)
    {
      sptr < Node<T> > temp (new Node<T>(data));
      
      
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
    
    void Remove (T removing)
    {
      sptr < Node<T> > temp;
      temp.next = head;
      
      while (temp.data != removing)
        temp = temp.next;
      
      temp.previous.next = temp.next;
      temp.next.previous = temp.next;
    }
    void Remove_At (int index)
    {
      if (index >= size || index < size) throw "Index out of range";
      sptr < Node<T> > temp;
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
    ~Double_Linked_List()
    {
      head = nullptr;
      tail = nullptr;
      size = 0;
    }
};

int main()
{
  Double_Linked_List<int> temp;
  temp.Add(2);
  
}