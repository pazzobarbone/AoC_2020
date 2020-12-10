inp = "day_04_input.txt"
entries = list()
with open(inp) as f:
    entries = f.readlines()
max_rows = len(entries)


class Validator():
    def __init__(self):
        self.required_fields = {
                    'byr': self._check_byr,
                    'iyr': self._check_iyr,
                    'eyr': self._check_eyr,
                    'hgt': self._check_hgt,
                    'hcl': self._check_hcl,
                    'ecl': self._check_ecl,
                    'pid': self._check_pid}

        self.optional_fields = {
                    'cid': self._check_cid}

    def check_passport(self, passport):
        stamp = True
        stamp = stamp and self._check_required_fields(passport)
        for f in passport.fields:
            if f in self.required_fields:
                stamp = stamp and self.required_fields[f](
                                                    passport.fields[f])
            elif f in self.optional_fields:
                stamp = stamp and self.optional_fields[f](
                                                    passport.fields[f])
        passport.valid = passport.valid and stamp

    def _check_required_fields(self, passport):
        for rf in self.required_fields:
            if rf not in passport.fields:
                return False
        return True

    def _check_byr(self, data):
        data = int(data)
        return (1920 <= data <= 2002)

    def _check_iyr(self, data):
        data = int(data)
        return (2010 <= data <= 2020)

    def _check_eyr(self, data):
        data = int(data)
        return (2020 <= data <= 2030)

    def _check_hgt(self, data):
        if 'cm' in data:
            data = data.replace('cm', '')
            data = int(data)
            return (150 <= data <= 193)
        elif 'in' in data:
            data = data.replace('in', '')
            data = int(data)
            return (59 <= data <= 76)
        else:
            return False

    def _check_hcl(self, data):
        stamp = True
        if data.startswith('#'):
            data = data.replace('#', '')
            if len(data) != 6:
                stamp = False
            else:
                for c in data:
                    if c not in ['0', '1', '2', '3', '4',
                                 '5', '6', '7', '8', '9',
                                 'a', 'b', 'c', 'd', 'e', 'f']:
                        stamp = False
                        break
        else:
            stamp = False

        return stamp

    def _check_ecl(self, data):
        stamp = True
        if data not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            stamp = False
        else:
            data = data.replace(data, '')
            if data:
                stamp = False

        return stamp

    def _check_pid(self, data):
        stamp = True
        try:
            int(data)
            if len(data) != 9:
                stamp = False
        except ValueError:
            stamp = False

        return stamp

    def _check_cid(self, data):
        return True


class Passport():
    def __init__(self):
        self.fields = dict()
        self.valid = True

    def add_field(self, name, data):
        self.fields[name] = data


validator = Validator()
checked_passports = list()
current_passport = Passport()
for entry in entries:
    if entry == '\n':
        validator.check_passport(current_passport)
        checked_passports.append(current_passport)
        current_passport = Passport()
    else:
        entry = entry.split(' ')
        for e in entry:
            field = e[0:3]
            data = e[4:].strip()
            current_passport.add_field(field, data)

valid_passports = 0
for p in checked_passports:
    if p.valid:
        valid_passports += 1

print("Part 2 = ", valid_passports)
