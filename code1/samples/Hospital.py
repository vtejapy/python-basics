class Patient(object):
    def __init__(self, id_number, name, allergies=[], bed_number='none'):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number


class  Hospital(object):
    def __init__(self, name, capacity, patients=[]):
        self.name = name
        self.capacity = capacity
        self.patients = patients
        self.open_bed_numbers = range(self.capacity)
        for i in range(len(self.patients)):
            self.patients[i].bed_number = i
            self.open_bed_numbers.pop(0)
    
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print 'Sorry, the hospital is full! :('
        else:
            patient.bed_number = self.open_bed_numbers.pop(0)
            self.patients.append(patient)
            print 'Patient ID #{} was successfully admitted'.format(patient.id_number)
        return self
        
    def discharge(self, patient_id_number):
        for i, patient in enumerate(self.patients):
            if patient.id_number == patient_id_number:
                self.open_bed_numbers.append(patient.bed_number)
                patient.bed_number = 'none'
                self.patients.pop(i)
                print 'Patient ID #{} was discharged'.format(patient.id_number)
                break
        return self


p0 = Patient(0, 'charlie')
p1 = Patient(1, 'emily')
p2 = Patient(2, 'bobby')
p3 = Patient(3, 'anna')
patients = [p0, p1, p2]

hospital = Hospital('Awesome Hospital', 6, patients)
print hospital.patients[0].name
print hospital.patients[0].bed_number
print 'open hospital beds:', hospital.open_bed_numbers

print '\n'

hospital.admit(p3)
print 'open hospital beds:', hospital.open_bed_numbers
print 'admitted patient name: ', hospital.patients[3].name
print 'admitted patient bed number: ', hospital.patients[3].bed_number

print '\n'

hospital.discharge(2)
print '# of patients:', len(hospital.patients)
print 'open hospital beds:', hospital.open_bed_numbers