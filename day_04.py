inp = "day_04_input.txt"
entries = list()
with open(inp) as f:
    # while True:
    entries = f.readlines()
        # if line:
        #     entries.append(line)
        # else:
        #     break

max_rows = len(entries)
required_fields = [
    'byr', 
    'iyr', 
    'eyr', 
    'hgt',
    'hcl', 
    'ecl', 
    'pid' 
]

optional_fields = ['cid']


def data_val(field, val):
    valid = True
    if 'byr' == field:
        val = int(val)
        if val < 1920 or val > 2002:
            valid = False
    elif 'iyr' == field:
        val = int(val)
        if val < 2010 or val > 2020:
            valid = False
    elif 'eyr' == field:
        val = int(val)
        if val < 2020 or val > 2030:
            valid = False
    elif 'hgt' == field:
        if 'cm' in val:
            val = val.replace('cm','')
            val = int(val)
            if val < 150 or val > 193:
                valid = False
        elif 'in' in val:
            val = val.replace('in','')
            val = int(val)
            if val < 59 or val > 76:
                valid = False
        else:
            valid = False
    elif 'hcl' == field:
        if val.startswith('#'):
            val = val.replace('#','')
            if len(val) != 6:
                valid = False
            for v in val:
                if v not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                    valid = False
        else:
            valid = False
    elif 'ecl' == field:
        if val not in ['amb', 'blu', 'brn', 'gry' ,'grn', 'hzl', 'oth']:
            valid = False
        else:
            val = val.replace(val, '')
            if val:
                valid = False
    elif 'pid' == field:
        try:
            integ = int(val)
            if len(val) != 9:
                valid = False
        except:
            valid = False
    print(field, data, valid)
    return valid

current_passport = list()
valid_passports = 0
data_valid = True
for entry in entries:
    if entry == '\n':
        pass_valid = True
        for p in required_fields:
            if p not in current_passport:
                pass_valid = False
                break
        if pass_valid and data_valid:
            valid_passports += 1
        current_passport = list()
        data_valid = True
    else:
        entry = entry.split(' ')
        for e in entry:
            field = e[0:3]
            data = e[4:].strip()
            current_passport.append(field)
            data_valid = data_valid and data_val(field, data)


print("Part 1 = ", valid_passports)
print("Part 2 = ", None)
