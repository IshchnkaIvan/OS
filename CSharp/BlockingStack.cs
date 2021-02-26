using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace StackTests
{
    class BlockingStack<T>
    {
        private object lockObject = new object();

        private Stack<T> sequentialStack = null;

        public BlockingStack()
        {
            sequentialStack = new Stack<T>();
        }

        public BlockingStack(IEnumerable<T> collection)
        {
            sequentialStack = new Stack<T>(collection);
        }

        public void Push(T item)
        {
            lock (lockObject)
            {
                sequentialStack.Push(item);
            }
        }

        public bool TryPop()
        {
            bool returnValue = true;
            lock (lockObject)
            {
                if (sequentialStack.Count == 0)
                {
                    returnValue = false;
                }
                else
                {
                    sequentialStack.Pop();
                }
            }
            return returnValue;
        }


        public bool TryAdd(T item)
        {
            Push(item);
            return true;
        }

        public int Count
        {
            get
            {
                return sequentialStack.Count;
            }
        }

        public T Peek()
        {
            return sequentialStack.Peek();
        }

        public bool IsEmpty()
        {
            return Count == 0;
        }

        public bool Contains(T item)
        {
            return sequentialStack.Contains(item);
        }
        public void Clear()
        {
            while (TryPop());
        }
    }
}
