#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
        MPI_Init(&argc, &argv);
        int world_rank;
        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
        int world_size;
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);
        int tag2 = 1;
        int tag1 = 2;       
        int arr[10000];
		srand(0);
		
		int i;
		for (i = 0; i < 100; i++) {
			arr[i] = rand();
		}

        printf ("\n--Current Rank: %d\n", world_rank);
        int index;
        int source = 0;
        int dest;
        if (world_rank == 0)
        {
            printf("* Rank 0 excecuting");
            index = 0;
            dest = 1;
            MPI_Send(&index, 1, MPI_INT, dest, tag1, MPI_COMM_WORLD);
            MPI_Send(&arr, 2, MPI_INT, dest, tag2, MPI_COMM_WORLD); 

			index = 3;
			dest = 2;
			MPI_Send(&index, 1, MPI_INT, dest, tag1, MPI_COMM_WORLD);
			MPI_Send(&arr[index], 3, MPI_INT, dest, tag2, MPI_COMM_WORLD);
        }
        else 
        {
            int sum = 0;
            int i;
            MPI_Recv(&index, 1, MPI_INT, source, tag1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            MPI_Recv(&arr[index], 20, MPI_INT, source, tag2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("At Rank: %d index is: %d\n", world_rank, index);
            for(i = index; i<=index+2; i++)
            {   
                printf("i: %d and arr[i]: %d\n", i, arr[i]);
                sum = arr[i]+sum;
            }
            printf("\n Mean is: %d and arr[3]: %d\n", sum/sizeof(arr), arr[3]);
        }       

        MPI_Finalize();
}