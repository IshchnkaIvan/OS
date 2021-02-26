using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace Lab2
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

        public bool TryPop(out T item)
        {
            bool returnValue = true;
            lock (lockObject)
            {
                if (sequentialStack.Count == 0)
                {
                    item = default(T);
                    returnValue = false;
                }
                else
                {
                    item = sequentialStack.Pop();
                }
            }
            return returnValue;
        }

        public bool TryTake(out T item)
        {
            return TryPop(out item);
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
    }
}
