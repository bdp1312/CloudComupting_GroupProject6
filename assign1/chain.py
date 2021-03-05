#This program can be run using mpi with any number of processes. 
#The root process (process 0) will get input from the user in a loop until a negative number is encountered
#Each number input by the user will get passed along a chain of processes, where process i will get the 
#number from i-1, then pass it to i+1. At every process, the number and rank of the process will be printed out.

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
    while True:
        value = int(input('Enter a number: '))
        if value < 0:
            comm.send(value, dest=rank + 1, tag = rank + 1)
            exit()
        else:
            print ("Process %d got %d" % (rank, value))
            comm.send(value, dest=rank + 1, tag = rank + 1)
            comm.recv(source=size-1)
elif rank == size - 1:
    while True:
        value = comm.recv(source = rank - 1, tag = rank)
        if value < 0:
            exit()
        else:
            print ("Process %d got %d" % (rank, value), flush=True)
            comm.send(0, dest=0)
else:
    while True:
        value = comm.recv(source = rank - 1, tag = rank)
        if value < 0:
            comm.send(value, dest=rank + 1, tag = rank + 1)
            exit()
        else:
            print ("Process %d got %d" % (rank, value))
            comm.send(value, dest=rank + 1, tag = rank + 1)
