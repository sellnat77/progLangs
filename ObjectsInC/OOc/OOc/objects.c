#include<stdio.h>

typedef enum { ANIMAL, DOG, CAT, LION } selectedAnimal;

//DECLARE STRUCTS
struct Animal
{
	void (**v_table)();
	int age;
};

struct Dog
{
	void (**v_table)();
	int age;
	double weight;
};

struct Cat
{
	void (**v_table)();
	int age;
	int numberOfLives;
};

struct Lion
{
	void (**v_table)();
	int age;
	int numberOfLives;
	double weight;
};

//SPEAK FUNCTIONS
void Speak_Dog(struct Animal *a);
void Speak_Cat(struct Animal *a);
void Speak_Lion(struct Animal *a);

//COST FUNCTIONS
double Get_Cost_Dog(struct Animal *a);
double Get_Cost_Cat(struct Animal *a);

//VTABLE ASSIGNMENTS
void (*v_table_dog[])();
void (*v_table_cat[])();
void (*v_table_lion[])();

//CONSTRUCTORS
void Construct_Dog(struct Animal *a);
void Construct_Cat(struct Animal *a);
void Construct_Lion(struct Animal *a);

//OPERATION FUNCTIONS
void animal_Operations(int selection);

int main()
{
	struct Animal *myAnimal = 1;
	int animalSelection;
	int age;
	int numLives;
	double weight;
	double cost;

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
		(struct Animal*) myAnimal = (struct Animal*)malloc(sizeof(struct Dog));
		
		if (myAnimal != NULL)
		{
			printf("Selected dog\n");
			printf("Enter dog's weight: ");
			scanf_s("%lf", &weight);
			printf("Enter dog's age:");
			scanf_s("%d", &age);

			Construct_Dog(&myAnimal);
			((struct Dog*)myAnimal)->weight = weight;
			((struct Dog*)myAnimal)->age = age;

			printf("\n");
			printf("\nSpeak animal!");
			((void(*)(struct Animal*))&myAnimal->v_table[0])(myAnimal);
			cost = ((double(*)(struct Animal*))&myAnimal->v_table[1])(myAnimal);
			//(myAnimal->v_table[1])(myAnimal);
			printf("\nYour animal costs %.2lf per month.\n", cost);

			free(&myAnimal);
		}
		else
		{
			break;
		}
		break;

	case CAT:
		myAnimal = malloc(sizeof(struct Cat));
		
		printf("Selected cat");
		printf("Enter cat's number of lives:");
		scanf_s("%d", &numLives);
		printf("Enter cat's age: %d");
		scanf_s("%d", &age);

		Construct_Cat(&myAnimal);
		((struct Cat*)myAnimal)->numberOfLives = numLives;
		((struct Cat*)myAnimal)->age = age;

		printf("\n");
		printf("\nSpeak animal!");
		((void(*)(struct Animal*))&myAnimal->v_table[0])(myAnimal);
		cost = ((double(*)(struct Animal*))&myAnimal->v_table[1])(myAnimal);
		//(myAnimal->v_table[1])(myAnimal);
		printf("\nYour animal costs %.2lf per month.\n", cost);

		free(&myAnimal);
		break;

	case LION:
		myAnimal = malloc(sizeof(struct Lion));
		printf("Selected lion");
		scanf_s("Enter lion's weight: %lf", &weight);
		scanf_s("Enter lion's number of lives: %d", &numLives);
		scanf_s("Enter lion's age: %d", &age);
		Construct_Lion(&myAnimal);
		((struct Lion*)myAnimal)->weight = weight;
		((struct Lion*)myAnimal)->numberOfLives = numLives;
		((struct Lion*)myAnimal)->age = age;

		printf("\n");
		printf("\nSpeak animal!");
		((void(*)(struct Animal*))&myAnimal->v_table[0])(myAnimal);
		cost = ((double(*)(struct Animal*))&myAnimal->v_table[1])(myAnimal);
		//(myAnimal->v_table[1])(myAnimal);
		printf("\nYour animal costs %.2lf per month.\n", cost);

		free(&myAnimal);
		break; 

	default:
		break;
	}

	
	return 1;
}

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
	return (((struct Dog*)a)->weight / 3) * 7.50;
};

double Get_Cost_Cat(struct Animal *a)
{
	return (((struct Cat*)a)->age * 5.50) + 100.00;
};

void (*v_table_dog[])()  = { &Speak_Dog , &Get_Cost_Dog };
void (*v_table_cat[])() = { &Speak_Cat , &Get_Cost_Cat };
void (*v_table_lion[])() = { &Speak_Lion, &Get_Cost_Cat };

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

void animal_Operations(int selection)
{
	double weight;
	int age;
	struct Animal* myAnimal = (struct Animal*)malloc(sizeof(struct Dog));

	if (myAnimal != NULL)
	{
		printf("Selected dog\n");
		printf("Enter dog's weight: ");
		scanf_s("%lf", &weight);
		printf("Enter dog's age:");
		scanf_s("%d", &age);

		Construct_Dog(&myAnimal);
		((struct Dog*)myAnimal)->weight = weight;
		((struct Dog*)myAnimal)->age = age;
	}
}