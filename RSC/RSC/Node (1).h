#pragma once

class Node
{
private:
	int name;
	int state; //0: vulnerable,1: deactivated,-1:ill,-2:will ill
	bool* next;
	int grade;
public:
	Node(int,int);
	int getState();
	int getName();
	void setState(int);
	void addNode(int);
	bool* getNext();
	void cutNext(int);
	int getGrade();
	~Node();
};

