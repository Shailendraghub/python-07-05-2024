{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cd56487e-b9b3-4337-a5c3-33934d7c68d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1748652917264\n"
     ]
    }
   ],
   "source": [
    "x=10\n",
    "print(id(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0a061952-ecd4-4d95-b19d-6ae1596d339d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1748652917264\n"
     ]
    }
   ],
   "source": [
    "y=x\n",
    "print(id(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e45daa09-5a94-4167-85ae-79c2c80fef24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 1748652917264\n"
     ]
    }
   ],
   "source": [
    "x=10\n",
    "print(x, id(x))\n",
    "y=x\n",
    "print(\"y: \",y,)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1806e91a-137a-4213-8989-2830beb21ff8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(10%3)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
