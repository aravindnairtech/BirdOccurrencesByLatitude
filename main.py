import torch
import numpy as np

print("WELCOME TO THE BIRD OCCURRENCES PROGRAM!")
print("Presented by: Aravind Nair and supervised by Professor Luca De Alfaro")
print("INSTRUCTIONS: ")
print("1. First, you will be asked to enter the name of the bird that you have found from an E-Bird Submission")
print("2. Second, you will input the numbers of each thing asked, and then once you are done typing CONFIRM...")
print("the program will find the best possible place to find the bird species (in California for now).")
print("3. If the results are not able to discover a place where there would be a DEFINITE place for a bird ")
print("to be in the given locations ")

continue1 = input("Type ENTER in all caps to Continue")
if continue1 != "ENTER":
    exit()

print("-------------------------")

month = input("What month did you find this bird?")
birdspecies = input("What is the name of the species of birds?")
temp = input("What was the high and low temperatures of the day?")
county = input("What county in California was this bird located in?")

#weights and biases
w = torch.randn(2,3, requires_grad=True)
b = torch.randn(2,requires_grad=True)

def mse(t1,t2):
    diff = t1 - t2
    return torch.sum(diff*diff)/diff.numel()

def model(x):
    return x @ w.t() + b






