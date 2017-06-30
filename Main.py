import os
import SmellExtract
import FileUtil

RESULT_ROOT_IN = "/Users/Tushar/Documents/Research/architectureSmells/Results"
OUT_FILE_PATH = "/Users/Tushar/Documents/Workspace/extractSmellInfo/"

counter = 1

# Case 1: I want to see whether there are generally a high percentage of imperative abstractions in the god components
# present in the subject repositories. Can you get me the total number of classes, number of imperative abstractions
# and number of unutilized abstractions present in all the god components found over all repos? I want to check,
# e.g. whether the high correlation between god component and imperative abstraction can actually be explained
# through a high percentage of imperative abstractions or not?
#FileUtil.writeFile(os.path.join(OUT_FILE_PATH, "smellsInfo1.csv"), "Project,Namespace,God Component,Unutilized Abstraction, Imperative Abstraction")

# Case 2: 2) Whether imperative abstractions contain complex or long methods? As God component is highly correlated to
# complex method as well as imperative abstraction, I want to check whether most of the methods inside imperative
# abstractions are complex/long or not. Actually we did not find the correlation between design and implementation
# smells or intra smell type correlations (architecture-architecture, implementation - implementation),
# perhaps that might have helped. But for this paper I think it will be sufficient if we can provide 3-4 examples
# concerning specific repos or all repos in general.
#FileUtil.writeFile(os.path.join(OUT_FILE_PATH, "smellsInfo2.csv"), "Project,Namespace,Type,Imperative Abstraction,Long Method,Complex Method")

#case 3 : 3) Any specific repo, where God component was decided on LOC rather than classes, and that component contains
# a high count of insufficient modularization instances. Also, which one is more common for god components (decision on
# number of classes or LOC)?
FileUtil.writeFile(os.path.join(OUT_FILE_PATH, "smellsInfo3.csv"), "Project,Namespace,God Component,NO of classes,LOC,Insufficient Modularization")

for dir in os.listdir(RESULT_ROOT_IN):
    if os.path.isdir(os.path.join(RESULT_ROOT_IN, dir)):
        print("Analyzing repo " + str(counter) + ": " + str(dir) + "\n")
        counter += 1
        #Case 1
        #SmellExtract.extractSmellInfo(RESULT_ROOT_IN, dir, os.path.join(OUT_FILE_PATH, "smellsInfo1.csv"))
        #Case 2
        #SmellExtract.extractSmellInfo2(RESULT_ROOT_IN, dir, os.path.join(OUT_FILE_PATH, "smellsInfo2.csv"))
        #Case 3
        SmellExtract.extractSmellInfo3(RESULT_ROOT_IN, dir, os.path.join(OUT_FILE_PATH, "smellsInfo3.csv"))