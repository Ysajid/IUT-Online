from iut_online.university.models import Department, Program
from iut_online.post.models import Group

d1 = Department(name = "Civil and Environmental Engineering", code = 'CEE', budget = 10000, building = '1st')
d2 = Department(name = "Electrical and Electronics Engineering", code = 'EEE', budget = 10000, building = '1st')
d3 = Department(name = "Mechanical and Chemical Engineering", code = 'MCE', budget = 10000, building = '2nd')
d4 = Department(name = "Computer Science and Engineering", code = 'CSE', budget = 10000, building = '2nd')

d1.save()
d2.save()
d3.save()
d4.save()

p1 = Program(name = "Bachelor in Science", code="BSc Engg", year = 4)
p1.save()
p1 = Program(name = "Higher Diploma", code="HD", year = 3)
p1.save()

g = Group(name = "CSE Batch 14")
g.save()
g = Group(name = "CSE 4530")
g.save()
g = Group(name = "CSE 4503")
g.save()
g = Group(name = "CSE 4505")
g.save()