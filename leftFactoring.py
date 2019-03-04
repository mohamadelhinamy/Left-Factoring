import argparse
import json

def readInputFile(file):
    f = open(file)
    map1 = {}
    for line in f:
        line = line.replace('\n','')  
        rules = line.split(':') 
        rules[0] = rules[0].strip()
        map1[rules[0]] = rules[1]   
    for element, body in map1.items() :
        body = body.strip() 
        map1[element] = body.split('|')
    for element, body in map1.items() :
        v = []
        for b in body :
            v.append(b.strip())
        map1[element] = v    
    print(map1)     
    return map1

def left_factor_elimination(map):
    newRules = {} 
    exist =False
    new_values = []
    other_values = []
    for key,value in map.items() :
        for idx,v in enumerate(value):
            x = v[0]
            for idx1 , v1 in enumerate(value):
                if v1[0]==v[0] and idx1 > idx and v1[0].isupper() == True and v1[1:] not in new_values:
                    exist = True
                    new_values.append(v1[1:])
            if exist == True and v[0].isupper() == True and v[1:] not in new_values:
                new_values.append(v[1:])
                other_values.append(v[0]+v[0]+'\'')
            else :
                if v[1:] not in new_values:
                    other_values.append(v)
        newRules[key] = other_values            
        newRules[key+'\''] = new_values     
        exist = False
        new_values = []
        other_values = []
    print(newRules)
    return newRules                




if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()
    mappy=readInputFile(args.file)
    left_factor_elimination = left_factor_elimination(mappy)
    f = open("task_4_2_result.txt", "w")
    for key,value in left_factor_elimination.items() :
        f.write(key+' : ')
        for v in value :
            f.write(v)
            if not v is value[-1]:
                f.write(' | ')
        f.write('\n')    
      
    f.close()



