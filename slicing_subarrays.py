{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bbfa6581-9831-4dca-b239-41206950882c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Generate a 2D array of shape (4, 5) with numbers from 1 to 20. '"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Generate a 2D array of shape (4, 5) with numbers from 1 to 20. '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d5901547-118a-4b50-96c7-2aba82e06c9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array =np.arange(1,21) # also use (array =np.arange(1,21)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9c106d14-c5ae-4f56-a7e6-cbd190400456",
   "metadata": {},
   "outputs": [],
   "source": [
    "reshaped_array = array.reshape(4,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5495b48e-ed71-4d73-99ce-6378e4f69e0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4  5]\n",
      " [ 6  7  8  9 10]\n",
      " [11 12 13 14 15]\n",
      " [16 17 18 19 20]]\n"
     ]
    }
   ],
   "source": [
    "print(reshaped_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "8bf8e685-2333-4bb7-b35c-048504952ddd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'extract subarray containing first two rows and first three columns'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''extract subarray containing first two rows and first three columns'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "6b438ea2-4281-4bc6-9fab-0a80879079d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [6, 7, 8]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reshaped_array[0:2,0:3] # also use reshaped_array = array[:2, :3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10ecd8e8-270e-400c-83e4-2c8ae55d8bfc",
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
