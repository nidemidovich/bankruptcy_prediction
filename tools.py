import os
import pickle

def make_cases(path):
    """
    Makes dict with cases info from files with courts cases

    Arguments:
        path, str: path to files with courts cases

    Returns:
        cases, dict: dict with cases info
    """
    cases = {
        'inn': [],
        'resultType': [],
        'caseNo': [],
        'caseDate': [],
        'instanceDate': [],
        'caseType': [],
        'sum': [],
        'type': []
    }

    files = os.listdir(path)
    for file in files:
        with open(os.path.join(path, file), 'rb') as pkl:
            record = pickle.load(pkl, encoding='utf-8')
            
            if record['cases_list'] == []:
                keys = ['resultType', 'caseNo', 'caseDate', 'instanceDate', 'caseType', 'sum', 'type']
                for key in keys: cases[key].append('n/a')

                cases['inn'].append(int(record['inn']))

            else:
                for case in record['cases_list']:
                    sides = []
                    for side in case['case_sides']:
                        if side['INN'].isdigit():
                            if record['inn'] == int(side['INN']): 
                                sides.append(side['type'])
                    
                    keys = ['caseNo', 'caseDate', 'instanceDate', 'resultType', 'sum']
                    for key in keys: cases[key].extend([case[key] for _ in range(len(sides))])
                    
                    cases['inn'].extend([int(record['inn']) for _ in range(len(sides))])
                    cases['caseType'].extend(case['caseType']['code'] for _ in range(len(sides)))
                    cases['type'].extend(sides)
    
    return cases