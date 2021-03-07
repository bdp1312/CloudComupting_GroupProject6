#This program can be run using mpi with any number of processes. 
#The root process (process 0) will get input from the user in a loop until a negative number is encountered
#Each number input by the user will get passed along a chain of processes, where process i will get the 
#number from i-1, then pass it to i+1. At every process, the number and rank of the process will be printed out.

from mpi4py import MPI
from time import sleep

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#Root process
if rank == 0:
    while True:
        #Get an input from the user
        value = int(input('Enter a number: '))
        if value < 0:
            #Send the kill signal to the next process in line before exiting
            comm.send(value, dest=rank + 1, tag = rank + 1)
            exit()
        else:
            #If input is not negative, print it out and send it to the next process
            print ("Process %d got %d" % (rank, value))
            comm.send(value, dest=rank + 1, tag = rank + 1)

            #Wait for a signal from the last process to indicate that the output has propagated to all processes
            comm.recv(source=size-1)

            #Sleep 1 sec to reduce how often the input prompt appears in the middle of the output
            sleep(1)
#Last process
elif rank == size - 1:
    while True:
        #Wait to recieve the next value from the previous process
        value = comm.recv(source = rank - 1, tag = rank)
        if value < 0:
            #Exit on negative value
            exit()
        else:
            #Print the value and then indicate that all processes have printed to the root process
            print ("Process %d got %d" % (rank, value), flush=True)
            comm.send(0, dest=0)
#All other processes
else:
    while True:
        #Wait to recieve the next value from the previous process
        value = comm.recv(source = rank - 1, tag = rank)
        if value < 0:
            #send the kill signal to the next process before exiting
            comm.send(value, dest=rank + 1, tag = rank + 1)
            exit()
        else:
            #Print the value and then send it to the next process
            print ("Process %d got %d" % (rank, value), flush=True)
            comm.send(value, dest=rank + 1, tag = rank + 1)
