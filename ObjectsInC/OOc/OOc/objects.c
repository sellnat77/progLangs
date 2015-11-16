#include<stdio.h>

typedef enum { ANIMAL, DOG, CAT, LION } selectedAnimal;

//DECLARE STRUCTS
struct Animal
{
	void *((*v_table[2])());
	//void(**v_table)();
	int age;
};

struct Dog
{
	void *((*v_table[2])());
	//void(*v_table_dog[])();
	int age;
	double weight;
};

struct Cat
{
	void *((*v_table[2])());
	int age;
	int numberOfLives;
};

struct Lion
{
	void *((*v_table[2])());
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

int main()
{
	struct Animal *myAnimal = 1;
	int animalSelection = 0;
	int age;
	int numLives;
	double weight;
	double cost;

	
	while (animalSelection != 4)
	{
		printf("\nPlease choose an animal:");
		printf("\n1.)Dog");
		printf("\n2.)Cat");
		printf("\n3.)Lion");
		printf("\n4.)Exit\n--");
		scanf_s("%d", &animalSelection);

		switch (animalSelection)
		{
		case ANIMAL:
			printf("\n\nSelected base animal");
			break;

		case DOG:
			myAnimal = malloc(sizeof(struct Dog));

			printf("\n\nSelected dog");
			printf("\nEnter dog's age:");
			scanf_s("%d", &age);

			printf("\nEnter dog's weight: ");
			scanf_s("%lf", &weight);

			Construct_Dog(myAnimal);
			((struct Dog*)myAnimal)->age = age;
			((struct Dog*)myAnimal)->weight = weight;
			break;

		case CAT:
			myAnimal = malloc(sizeof(struct Cat));

			printf("\n\nSelected cat");
			printf("\nEnter cat's age: ");
			scanf_s("%d", &age);			
			
			printf("\nEnter cat's number of lives: ");
			scanf_s("%d", &numLives);		

			Construct_Cat(myAnimal);
			((struct Cat*)myAnimal)->numberOfLives = numLives;
			((struct Cat*)myAnimal)->age = age;
			break;

		case LION:
			myAnimal = malloc(sizeof(struct Lion));

			printf("\n\nSelected lion");
			printf("\nEnter lion's age: ");
			scanf_s("%d", &age);			
			
			printf("\nEnter lion's number of lives: ");
			scanf_s("%d", &numLives);

			printf("\nEnter lion's weight: ");
			scanf_s("%lf", &weight);

			Construct_Lion(myAnimal);
			((struct Lion*)myAnimal)->weight = weight;
			((struct Lion*)myAnimal)->numberOfLives = numLives;
			((struct Lion*)myAnimal)->age = age;
			
			break;

		default:
			printf("\n\n\t\tGoodbye!");
			return 1;
			break;
		}

		printf("\n\nSpeak animal!");
		((void(*)(struct Animal*))myAnimal->v_table[0])(myAnimal);
		cost = ((double(*)(struct Animal*))myAnimal->v_table[1])(myAnimal);
		printf("\n\nYour animal costs %.2lf per month.\n", cost);
		free(myAnimal);
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

void (*v_table_dog[])()  = { Speak_Dog , Get_Cost_Dog };
void (*v_table_cat[])() = { Speak_Cat , Get_Cost_Cat };
void (*v_table_lion[])() = { Speak_Lion, Get_Cost_Cat };

void Construct_Dog(struct Animal *a)
{
	((struct Dog*)a)->v_table[0] = v_table_dog[0];
	((struct Dog*)a)->v_table[1] = v_table_dog[1];
	((struct Dog*)a)->age = 0;
	((struct Dog*)a)->weight = 0;
};

void Construct_Cat(struct Animal *a)
{
	((struct Cat*)a)->v_table[0] = v_table_cat[0];
	((struct Cat*)a)->v_table[1] = v_table_cat[1];
	((struct Cat*)a)->age = 0;
	((struct Cat*)a)->numberOfLives = 0;
}

void Construct_Lion(struct Animal *a)
{
	((struct Lion*)a)->v_table[0] = v_table_lion[0];
	((struct Lion*)a)->v_table[1] = v_table_lion[1];
	((struct Lion*)a)->age = 0;
	((struct Lion*)a)->numberOfLives = 0;
	((struct Lion*)a)->weight = 0;
}