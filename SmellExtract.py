import os
import re
import FileUtil

def process_DS(line, OUT_FILE_PATH, dir):
    smell,project,namespace,cause, *rest = line.split(",")
    if (smell=='Dense Structure'):
        for m in re.finditer(r'Average degree = (\d+.\d+)', cause, re.IGNORECASE):
            reason = m.group(1)
            FileUtil.writeFile(os.path.join(OUT_FILE_PATH, "smellsInfo_DS.csv"), dir + "," + smell + "," + reason)


def process_UD(line, OUT_FILE_PATH, dir):
    smell,project,namespace,cause, *rest = line.split(",")
    if (smell=='Unstable Dependency'):
        for m in re.finditer(r'less stable component\(s\): ((\w|\.)*)', cause, re.IGNORECASE):
            reason = m.group(1)
            FileUtil.writeFile(os.path.join(OUT_FILE_PATH, "smellsInfo_UD.csv"), dir + "," + smell + "," + project +\
                               "," + namespace + "," + reason)


def process_GC(line, OUT_FILE_PATH, dir):
    smell,project,namespace,cause, *rest = line.split(",")
    if (smell=='God Component'):
        for m in re.finditer(r'component are: (\d+)', cause, re.IGNORECASE):
            reason = m.group(1)
            FileUtil.writeFile(os.path.join(OUT_FILE_PATH, "smellsInfo_GC.csv"), dir + "," + smell + "," + project +\
                               "," + namespace + "," + reason)


def process_case1(as_file, dir_in, out_file_path):
    project, *rest = as_file.split("_ArchSmells.csv")
    if os.path.isfile(os.path.join(dir_in, project + "_DesignSmells.csv")):
        ds_file = os.path.join(dir_in, project + "_DesignSmells.csv")
        with open (os.path.join(dir_in, as_file)) as asf:
            for line in asf:
                smell,aproject,namespace, *rest = line.split(",")
                if (smell=='God Component'):
                    unutil_abs = 0
                    imp_abs = 0
                    with open(ds_file) as dsf:
                        for ds_line in dsf:
                            dsmell,dnamespace,*drest = ds_line.split(",")
                            if namespace == dnamespace:
                                if dsmell == "Unutilized Abstraction":
                                    unutil_abs += 1
                                if dsmell == "Imperative Abstraction":
                                    imp_abs += 1
                    FileUtil.writeFile(out_file_path, aproject + "," + namespace + ",1," + str(unutil_abs) + "," + str(imp_abs))


def extractSmellInfo(RESULT_ROOT_IN, dir, OUT_FILE_PATH):
    for root, dirs, files in os.walk(os.path.join(RESULT_ROOT_IN, dir)):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for file in files:
            if file.endswith("_ArchSmells.csv"):
                process_case1(file, root, OUT_FILE_PATH)


def process_case2(ds_file, dir_in, out_file_path):
    project, *rest = ds_file.split("_DesignSmells.csv")
    if os.path.isfile(os.path.join(dir_in, project + "_ImpSmells.csv")):
        is_file = os.path.join(dir_in, project + "_ImpSmells.csv")
        with open (os.path.join(dir_in, ds_file)) as asf:
            for line in asf:
                smell,namespace,dclass, *rest = line.split(",")
                if (smell=='Imperative Abstraction'):
                    long_m = 0
                    comp_m = 0
                    with open(is_file) as dsf:
                        for ds_line in dsf:
                            ismell,inamespace,iclass,*drest = ds_line.split(",")
                            if namespace == inamespace:
                                if dclass == iclass:
                                    if ismell == "Long Method":
                                        long_m += 1
                                    if ismell == "Complex Method":
                                        comp_m += 1
                    FileUtil.writeFile(out_file_path, project + "," + namespace + "," + dclass + ",1," + str(long_m) + "," + str(comp_m))

def extractSmellInfo2(RESULT_ROOT_IN, dir, OUT_FILE_PATH):
    for root, dirs, files in os.walk(os.path.join(RESULT_ROOT_IN, dir)):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for file in files:
            if file.endswith("_DesignSmells.csv"):
                process_case2(file, root, OUT_FILE_PATH)