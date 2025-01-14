{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6b4cfd71-ad79-4753-9277-128acd6f2221",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Create a 1D array with numbers from 1 to 20. Reverse the array so the elements are in descending order.'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Create a 1D array with numbers from 1 to 20. Reverse the array so the elements are in descending order.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c92d5c5c-d3d7-4f7a-8dcb-d5b4c7721484",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.arange(1,21)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "14bcb0ee-1b1c-4ea4-8d33-1ab62d690f59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bb2c667a-629a-4f34-8e8b-62007b4f5c19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,\n",
       "        3,  2,  1])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22b1b067-c964-400e-8694-176fdb34a432",
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
