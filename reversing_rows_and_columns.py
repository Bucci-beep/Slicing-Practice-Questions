{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3fa780db-101b-454d-827d-dc812d725e19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Create a 2D array of shape (3, 4) with numbers from 1 to 12'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Create a 2D array of shape (3, 4) with numbers from 1 to 12'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "94973116-56fd-4b5c-9840-8d84a5a53065",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array =np.arange(1,13).reshape(3,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "30eee608-3389-486e-bfb3-b00a9565057b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3c15077b-0aa1-456e-a6b1-af2a24fce0b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' reverse each row'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''' reverse each row''' # use array[0] = array[0][::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5e469e6d-df3c-48f4-9d98-b4e78b55dfa2",
   "metadata": {},
   "outputs": [],
   "source": [
    "array[0] = array[0][::-1]\n",
    "array[1] = array[1][::-1]\n",
    "array[2] = array[2][::-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e79fed5a-e55b-42cd-9856-820c7a325304",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed rows of 2D array:\n",
      "[[12  1  1  1]\n",
      " [ 8  7  6  5]\n",
      " [ 1 11 10  9]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Reversed rows of 2D array:\")\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "747086e2-34c5-44b4-bb2d-39d068239726",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' reverse each column'"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''' reverse each column'''"
   ]
  },
  {
   "cell_type": "raw",
   "id": "9c6f75f4-479c-4d59-960e-4ee67fc422d2",
   "metadata": {},
   "source": [
    "import numpy as nparray_columns = np.arange(1,13).reshape(4,5)\n",
    "array_columns[:, 0] = array_columns[:, 0][::-1]\n",
    "\n",
    "array_columns[:, 1] = array_columns[:, 1][::-1]\n",
    "\n",
    "# Reverse the third column (index 2)\n",
    "array_columns[:, 2] = array_columns[:, 2][::-1]\n",
    "\n",
    "# Reverse the fourth column (index 3)\n",
    "array_columns[:, 3] = array_columns[:, 3][::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "8f300ecf-807b-4d0a-b89e-a618fe85f59a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed columns 2D array:\n",
      "[[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Reversed columns 2D array:\")\n",
    "print(array_columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "7650dc09-b5c7-4c41-8627-3f5187bfbc72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed Columns 2D Array:\n",
      "[[ 9 10 11 12]\n",
      " [ 5  6  7  8]\n",
      " [ 1  2  3  4]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Create a 2D array with shape (3, 4) and numbers from 1 to 12\n",
    "array_columns = np.arange(1, 13).reshape(3, 4)\n",
    "\n",
    "# Reverse the first column (index 0)\n",
    "array_columns[:, 0] = array_columns[:, 0][::-1]\n",
    "\n",
    "# Reverse the second column (index 1)\n",
    "array_columns[:, 1] = array_columns[:, 1][::-1]\n",
    "\n",
    "# Reverse the third column (index 2)\n",
    "array_columns[:, 2] = array_columns[:, 2][::-1]\n",
    "\n",
    "# Reverse the fourth column (index 3)\n",
    "array_columns[:, 3] = array_columns[:, 3][::-1]\n",
    "\n",
    "print(\"Reversed Columns 2D Array:\")\n",
    "print(array_columns)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "828077e9-ab6c-42a2-b06f-a295acde78f1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
