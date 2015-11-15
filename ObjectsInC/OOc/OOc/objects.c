#include<stdio.h>



struct Animal
{
	void **v_table;
	int age;
};

struct Dog
{
	void **v_table;
	int age;
	double weight;
};

struct Cat
{
	void **v_table;
	int age;
	int numberOfLives;
};

struct Lion
{
	void **v_table;
	int age;
	int numberOfLives;
	double weight;
};

typedef enum { ANIMAL, DOG, CAT, LION } selectedAnimal;

void Speak_Dog(struct Animal *a)
{
	printf("\nMeow! I weigh %.2lf pounds!", ((struct Dog*)a)->weight);
};

void Speak_Cat(struct Animal *a)
{
	printf("\nWoof! I have %d lives!", ((struct Cat*)a)->numberOfLives);
};

void Speak_Lion(struct Animal *a)
{
	printf("\nROAR! I weigh %.2lf pounds!", ((struct Lion*)a)->weight);
};

double Get_Cost_Dog(struct Animal *a)
{
	double cost = (((struct Dog*)a)->weight / 3) * 7.50;
	
	return cost;
};

double Get_Cost_Cat(struct Animal *a)
{
	double cost = (((struct Cat*)a)->age * 5.50) + 100.00;

	return cost;
};

void* v_table_dog[2] = { Speak_Dog, Get_Cost_Dog };
void* v_table_cat[2] = { Speak_Cat, Get_Cost_Cat };
void* v_table_lion[2] = { Speak_Lion, Get_Cost_Cat };

void Construct_Dog(struct Animal *a)
{
	((struct Dog*)a)->v_table = v_table_dog;
	((struct Dog*)a)->age = 0;
	((struct Dog*)a)->weight = 0;

};

void Construct_Cat(struct Animal *a)
{
	((struct Cat*)a)->v_table = v_table_cat;
	((struct Cat*)a)->age = 0;
	((struct Cat*)a)->numberOfLives = 0;
}

void Construct_Lion(struct Animal *a)
{
	((struct Lion*)a)->v_table = v_table_cat;
	((struct Lion*)a)->age = 0;
	((struct Lion*)a)->numberOfLives = 0;
	((struct Lion*)a)->weight = 0;
}

int main()
{
	struct Dog *dogPtr;
	struct Cat *catPtr;
	struct Lion *lionPtr;
	struct Animal *myAnimal = 1;
	int animalSelection;
	int age;
	int numLives;
	double weight;

	
	//printf("Printing the dog:\n\n\n\n");
	//((void (*)(struct Animal*))myAnimal->v_table[0])(myAnimal);

	
	printf("Please choose an animal:\n");
	printf("1.)Dog\n");
	printf("2.)Cat\n");
	printf("3.)Lion\n");
	scanf_s("%d", &animalSelection);

	switch (animalSelection)
	{
	case ANIMAL:
		printf("Selected base animal");
		break;

	case DOG:
		myAnimal = malloc(sizeof(struct Dog));
		//myAnimal = dogPtr;
		printf("Selected dog\n");
		printf("Enter dog's weight: ");
		scanf_s("%lf", &weight);
		printf("Enter dog's age:");
		scanf_s("%d", &age);
		
		Construct_Dog(&myAnimal);
		((struct Dog*)myAnimal)->weight = weight;
		((struct Dog*)myAnimal)->age = age;
		break;

	case CAT:
		catPtr = malloc(sizeof(struct Cat));
		myAnimal = &catPtr;
		printf("Selected cat");
		printf("Enter cat's number of lives:");
		scanf_s("%d", &numLives);
		printf("Enter cat's age: %d");
		scanf_s("%d", &age);

		Construct_Cat(&catPtr);
		catPtr->numberOfLives = numLives;
		catPtr->age = age;
		break;

	case LION:
		lionPtr = malloc(sizeof(struct Lion));
		myAnimal = &lionPtr;
		printf("Selected lion");
		scanf_s("Enter lion's weight: %lf", &weight);
		scanf_s("Enter lion's number of lives: %d", &numLives);
		scanf_s("Enter lion's age: %d", &age);
		Construct_Lion(&lionPtr);
		lionPtr->weight = weight;
		lionPtr->numberOfLives = numLives;
		lionPtr->age = age;
		break; 

	default:
		break;
	}

	printf("\n");
	printf("\nSpeak animal!");
	((void(*)(struct Animal*))&myAnimal->v_table[0])(myAnimal);
	double cost = 1.0;//((double(*)(struct Animal*))&myAnimal->v_table[1])(myAnimal);
	printf("\nYour animal costs %.2lf per month.\n",cost);

	free(myAnimal);
	return 1;
}