papers = int(input("How many papers are there to grade? "))
num_TAs = int(input("How many TAs are available? "))
papers_per_TA = papers // num_TAs
print('Each TA will grade', papers_per_TA, 'papers.')
prof_papers = papers % num_TAs
print("The professor will grade", prof_papers, "papers.")
