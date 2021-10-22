#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;
template<typename R, typename... T>
using function = R(*)(T...);
template<typename T>
using sptr = shared_ptr<T>;
template<typename T>
class Node 
{
  public:
    T data;
    sptr < Node<T> > previous = nullptr, next = nullptr;
    Node(){};
    Node(T data): data(data){};
};
template<typename T>
class Double_Linked_List
{
  private:
    sptr < Node<T> > head = nullptr, tail = nullptr;
    int size = 0;
  public:
    Double_Linked_List(): size(0){};

    Double_Linked_List(T data)
    {
      Add_Last(data);
    }

    //Copy
    Double_Linked_List(const Double_Linked_List& list)
    {
      auto temp = list.head;
      while(temp != nullptr)
      {
        Add_Last(temp->data);
        temp = temp->next;
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
        Add_Last(temp->data);
        temp = temp->next;
      }
      return *this;
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
      return *this;
    }

    Double_Linked_List(vector <T> list)
    {
      for_each(list.begin(), list.end(), [this](T n) {Add_Last(n);});
    }

    Double_Linked_List(initializer_list<T> list)
    {
      for_each(list.begin(), list.end(), [this](T n) {Add_Last(n);});
    }

    T Length()
    {
      return size;
    }

    T operator [](int index)
    {
      return At(index);
    }

    T At(int index)
    {
      if (index >= size || index < 0) throw ("Index out of range");
      auto temp = head;
      int current = 0;

      while(index != current)
      {
        temp = temp->next;
        current++;
      }
      return temp->data;
    }

    void Add_Last(T data) noexcept
    {
      sptr < Node<T> > temp (new Node<T>(data));      
      if (size == 0)
      {
        head = temp;
        tail = temp;
      }
      else
      {
        tail->next = temp;
        temp->previous = tail;
        tail = temp;
      } 
      size++;
    };
    
    
    void Remove_Last ()
    {
      if (size > 1)
      {
        tail = tail->previous;
        tail->next = nullptr;
      }
      else if (size == 1)
      {
        head = nullptr;
        tail = nullptr;
      }
      else 
      {
        throw("No elements");
      }
      size--;
    }

    void Remove_At (int index)
    {
      if (index >= size || index < 0) throw ("Index out of range");
      auto temp = head;
      int current = 0;

      while(index != current)
      {
        temp = temp->next;
        current++;
      }
      temp->previous->next = temp->next;
      temp->next->previous = temp->next;
      size--;
    }

    template<typename R>
    Double_Linked_List<R> Map(function<R, T> func)
    {
      Double_Linked_List<R> list;
      for (int i = 0; i < size; i++)
      {
        list.Add_Last(func(At(i)));
      }
      return list;
    }

    void ToString()
    {
      cout<<"[";
      auto current = head;
      for (int i = 0; i < size; i++)
      {
        cout<<current->data;
        current = current->next;
        if (i+1 != size) cout<< ", ";
      }
      cout<<"]"<<endl;
    }

    ~Double_Linked_List()
    {
      head = nullptr;
      tail = nullptr;
      size = 0;
    }
};

char Func(int c)
{
  return (char)c + 'A';
}

int main()
{
  Double_Linked_List<int> a{1,2,3,4};
  a.Remove_Last();
  a.Add_Last(5);
  cout<<a.Length()<<endl;
  a.Remove_At(2);
  cout<<a[2]<<endl;
  a.ToString();

  Double_Linked_List<int> b = {3,4,5,6};
  b.ToString();

  Double_Linked_List<int> c;
  c.ToString();
  c = b;
  c.ToString();

  vector<int> d{1,2,4,74};
  b = d;
  b.ToString();

  Double_Linked_List<int> e(1);
  e.Add_Last(5);
  e.ToString();
  cout<<e.At(1)<<endl;

  Double_Linked_List<char> f = e.Map(Func);
  f.ToString();

  Double_Linked_List<int> g(e);
  g.ToString();
}