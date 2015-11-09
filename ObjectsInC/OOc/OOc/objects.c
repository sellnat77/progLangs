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

void* v_table_dog[2] = { Speak_Dog, Get_Cost_Dog };
void* v_table_cat[2] = { Speak_Cat, Get_Cost_Cat };
void* v_table_lion[2] = { Speak_Lion, Get_Cost_Cat };

void Speak_Dog(struct Animal *a)
{
	printf("Meow! I weigh %2.2f pounds!", ((struct Dog*)a)->weight);
};

void Speak_Cat(struct Animal *a)
{
	printf("Woof! I have %d lives!", ((struct Cat*)a)->numberOfLives);
};

void Speak_Lion(struct Animal *a)
{
	printf("ROAR! I weigh %2.2f pounds!", ((struct Lion*)a)->weight);
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

struct Dog Construct_Dog(struct Animal *a)
{
	((struct Dog*)a)->v_table = v_table_dog;
	((struct Dog*)a)->age = 0;
	((struct Dog*)a)->weight = 0;

};

struct Cat Construct_Cat(struct Animal *a)
{
	((struct Cat*)a)->v_table = v_table_cat;
	((struct Cat*)a)->age = 0;
	((struct Cat*)a)->numberOfLives = 0;
}

struct Lion Construct_Lion(struct Animal *a)
{
	((struct Lion*)a)->v_table = v_table_cat;
	((struct Lion*)a)->age = 0;
	((struct Lion*)a)->numberOfLives = 0;
	((struct Lion*)a)->weight = 0;
}

int main()
{
	struct Animal *myAnimal;
	int animalSelection;

	printf("Please choose an animal:\n");
	printf("1.)Dog\n");
	printf("2.)Cat\n");
	printf("3.)Lion\n");
	scanf("%d", &animalSelection);

	switch (animalSelection)
	{
	case 1:
		malloc(sizeof(struct Dog*));
		//myAnimal = (struct Animal*)Construct_Dog(myAnimal);
		break;
	case 2:
		malloc(sizeof(struct Cat*));
		break;
	case 3:
		malloc(sizeof(struct Lion*));
		break;
	default:
		break;
	}




	return 1;
}