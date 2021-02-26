using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace StackTests
{
    [TestClass]
    public class StackTests
    {
        BlockingStack<int> stack = new BlockingStack<int>();
        Stack<int> defaultStack = new Stack<int>();

        public void PushElement()
        {
            for (int i = 0; i < 100; i++)
            {
                //stack.Push(0);
                defaultStack.Push(0);
            }
        }
        [TestMethod]
        public void TestPush()
        {
            defaultStack.Clear();

            Thread[] threads = new Thread[8];
            for (int i = 0; i < 8; i++)
            {
                threads[i] = new Thread(PushElement);
                threads[i].Start();
            }
            for (int i = 0; i < 8; i++)
            {
                threads[i].Join();
            }
            //Assert.AreEqual(800, stack.Count);
            Assert.AreEqual(800, defaultStack.Count);
        }

        public void PopElement()
        {
            for (int i = 0; i < 100; i++)
            {
                stack.TryPop();
                //defaultStack.Pop();
            }
        }
        [TestMethod]
        public void TestPop()
        {
            //defaultStack.Clear();
            stack.Clear();
            for (int i = 0; i < 800; i++)
            {
                stack.Push(0);
                //defaultStack.Push(0);
            }
            Thread[] threads = new Thread[8];
            for (int i = 0; i < 8; i++)
            {
                threads[i] = new Thread(PopElement);
                threads[i].Start();
            }
            for (int i = 0; i < 8; i++)
            {
                threads[i].Join();
            }
            Assert.AreEqual(0, stack.Count);
            //Assert.AreEqual(0, defaultStack.Count);
        }
        public void PopElement()
        {
            for (int i = 0; i < 100; i++)
            {
                stack.TryPop();
                //defaultStack.Pop();
            }
        }
        [TestMethod]
        public void TestPop()
        {
            //defaultStack.Clear();
            stack.Clear();
            for (int i = 0; i < 800; i++)
            {
                stack.Push(0);
                //defaultStack.Push(0);
            }
            Thread[] threads = new Thread[8];
            for (int i = 0; i < 8; i++)
            {
                threads[i] = new Thread(PopElement);
                threads[i].Start();
            }
            for (int i = 0; i < 8; i++)
            {
                threads[i].Join();
            }
            Assert.AreEqual(0, stack.Count);
            //Assert.AreEqual(0, defaultStack.Count);
        }
    }
}
