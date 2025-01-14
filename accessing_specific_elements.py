{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0077fa77-d576-4df3-be4f-fc13aa045c46",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.random.randint(1,101, size=20) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "86250c50-8ca6-4abf-9059-48998efcf7d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 41  96  69  73  47  97  68  20  72  86 100  39  27  48  52  39  93 100\n",
      "  59  66]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "c97e5e22-f157-40bc-a874-beb0cc2521d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "reshaped_array = array.reshape(4,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "e3d3a05f-fad6-48d4-9469-4926c9115041",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 41  96  69  73  47]\n",
      " [ 97  68  20  72  86]\n",
      " [100  39  27  48  52]\n",
      " [ 39  93 100  59  66]]\n"
     ]
    }
   ],
   "source": [
    "print(reshaped_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "462bfd38-a6b4-402b-9aeb-60e8357b72d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reshaped_array[1,2] # accessing the element in the second row, third column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "26ec95a5-8dbe-4f54-9540-def1b4fbfcf5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "66"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reshaped_array[3,4] # accessing the element in the last row, last column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ed93f9e-25dd-499a-9ed4-20447494027f",
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
