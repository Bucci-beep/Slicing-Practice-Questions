{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bbdf6371-21c7-4c02-85d9-e22f0425ae16",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.arange(21)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "df887119-8a90-4ff5-b79e-7d55ead55611",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6dd8942e-bbc5-418b-b83d-371ce33dbacb",
   "metadata": {},
   "outputs": [],
   "source": [
    "array = np.arange(1,21)\n",
    "reshaped_array = array.reshape(4,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5f1685a6-a49c-44ed-9d33-45208a67480b",
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
   "execution_count": 19,
   "id": "21076246-3412-406a-923d-01757bc06ca2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Generate a 2D array of shape (4, 5) with numbers from 1 to 20. \\nExtract:\\n\\nThe first row.\\nThe last row.'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Generate a 2D array of shape (4, 5) with numbers from 1 to 20. \n",
    "Extract:\n",
    "\n",
    "The first row.\n",
    "The last row.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ce312b3f-56f9-4cfc-a28f-88e1a3e4a7f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 6,  7,  8,  9, 10])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reshaped_array[1,:] #extracting the first row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "0b83b7ac-67c7-4503-9aa1-dd05d82d1fed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 5, 10, 15, 20])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reshaped_array[:,4] #extracting the last row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ddd2fbe-3495-4b3b-930a-c79cd276652c",
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
