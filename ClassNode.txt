#include "stdafx.h"
#include "Node.h"
#include "stdlib.h"

int name; //identificatore progressivo
int state; //0: vulnerable,1: deactivated,-1:ill,-2: will ill
bool* next; //vettore di puntatori
int grade; //numero archi

Node::Node(int n,int d)
{
	group = -1;
	grade = 0;
	name = n;
	state = 0; 
	next = (bool*) malloc(d * sizeof(bool));
	for (int i = 0; i < d; i++) {
		next[i] = false;
	}
}

int Node::getName() {
	return name;
}

int Node::getState(){
	return state;
}

int Node::getGrade() {
	return grade;
}

int Node::getGroup() {
	return group;
}

void Node::setState(int set) {
	if (state == 1) return;
	if (state == set) return;
	if (state == 0 && set == -1) state = -1;
	if (state == 0 && set == -2) state = -2;
	if (state == -1 && set == -2) return;
	if (state == -2 && set == -1) state = -1;
	if (state == 0 && set == 1) state = 1;
	if (state == -2 && set == 1) state = -2; //invece di return
}

void Node::setGroup(int setG) {
	group = setG;
	return;
}

void Node::addNode(int n) {
	next[n] = true;
	grade++;
}

bool* Node::getNext() {
	return next;
}	

void Node::cutNext(int n) {
	next[n] = false;
	grade--;
}

Node::~Node() {
}