{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "19321108-6d96-4e7b-b006-e98126b59b32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'create a 2D array of shape (4,5) with numbers from 1 to 20, extract:\\n\\nThe second column.\\nThe last column.'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''create a 2D array of shape (4,5) with numbers from 1 to 20, extract:\n",
    "\n",
    "The second column.\n",
    "The last column.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7230387f-55a2-4144-91a0-92bdbbc13f08",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.arange(1,21)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1c95a890-0f78-4f01-96b8-df753668c4f5",
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
   "execution_count": 7,
   "id": "291c8b7f-8a5f-4e81-a84f-c1f36fa6a588",
   "metadata": {},
   "outputs": [],
   "source": [
    "reshaped_array = array.reshape(4,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8d723785-cfc9-4bda-b919-d4e97fc258ac",
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
   "execution_count": null,
   "id": "a9e1c4b9-6848-466a-aa6a-2ef055b37e64",
   "metadata": {},
   "outputs": [],
   "source": [
    "reshaped_array[:,"
   ]
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
