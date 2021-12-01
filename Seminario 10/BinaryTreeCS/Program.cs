using System;
using System.Collections;

namespace BinaryTreeCS {
    class Program {
        public static void Main(string[] args) {
            return;
        }
        class ABB {
            int value;
            ABB left;
            ABB right;
            public ABB(int value) {
                this.value = value;
                this.left = null;
                this.right = null;
            }
            public ABB(int value, ABB left, ABB right) {
                this.value = value;
                this.left = left;
                this.right = right;
            }
            public void Add(int v) {
                ABB node = SearchNode(v, this);
                if (node == null)
                    this.value = v;
                else
                    if (node.value == v) return;
                if (v < node.value)
                    node.left = new ABB(v);
                else node.right = new ABB(v);

            }
            public bool Contains(int v) {
                ABB node = SearchNode(v, this);
                if (node != null && node.value == v) return true;
                return false;
            }
            private ABB SearchNode(int x, ABB a) {
                if (a == null) return a;
                if (x < a.value && a.left != null) {
                    a = a.left;
                    return SearchNode(x, a);
                }
                if (x > a.value && a.right != null){
                    a = a.right;
                    return SearchNode(x, a);
                }
                return a;
            }
        }
    }
}