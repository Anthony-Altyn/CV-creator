
# Text Variables
Header = '>>This resume was generated entirely in Python. For full sourcecode, view my GitHub profile.'
Name = 'ANTON ALTYNBAEV'
Title = 'for position: Junior'
Contact = 'altynbajew@gmail.com\nphone: 575 771 073\nlinkedin.com/in/anton-altynbaev\nhttps://github.com/Anthony-Altyn'
ProfessionalSummary = 'PROFESSIONAL SUMMARY'
DescrProf ='''
Until recently a multipurpose product engineer in injection molding,
thermodynamics, electronics. Worked as a contractor for different
startups and big companies. Used C++ and Python for various
tasks - generally to ease my own work, but as the creation of
programs began to take more and more time decided to shift
my focus to this activity.'''
WorkHeader = 'EXPERIENCE RELATED TO THIS POSITION'
WorkOneTitle = 'OMNIMECH Sp. z o.o. / Engineer, co-founder'
WorkOneTime = '2018-Present'
WorkOneDesc = '''
- Used various version-control software for designing purposes
- Have created for a client a program instrument for
  mass-sorting CNC-files with output HTML-reports
- Optimized a database for a client
'''
WorkTwoTitle = 'Freelance engineer / Product engineer'
WorkTwoTime = '2014-2018'
WorkTwoDesc = '''
- Created various small programs in C++ to help with engineering
  calculations in aerodynamics
- Gathered limited experience with networks
- Programmed controllers in ASM (mostly Atmel)
'''
WorkThreeTitle = 'Ufa plant Promsvyaz / Injection molding engineer'
WorkThreeTime = '2012-2014'
WorkThreeDesc ='''
- Except for using Version-control software this experience
  is mostly unrelated to programming
'''
EduHeader = 'EDUCATION'
EduOneTitle = 'Ufa State College of Radioelectronics'
EduOneTime = '2001-2006'
EduOneDesc = 'Radioelectronics and Computer systems'
EduTwoTitle = 'Ufa State Aviation Technical University'
EduTwoTime = '2006-2010'
EduTwoDesc = 'Robotics'
SkillsHeader = 'Skills'
SkillsDesc = '- Python\n- Command Line\n- Git and Version Control\n- SQL\n- Probability/Statistics math\n- HTML\n- Excel'
ExtrasTitle = 'Languages'
ExtrasDesc = '''
English - B2
Polish - B2
Russian - C1
German - A2'''
CodeTitle = 'Legal information'
CodeDesc = '''
Omnimech sp. z o.o.
ul. Młyńska 5/9
61-729, Poznań'''

# Setting style for bar graphs
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text
plt.annotate(Header, (.02,.98), weight='regular', fontsize=7, alpha=.6)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(ProfessionalSummary, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(DescrProf, (.04,.75), weight='regular', fontsize=9)
plt.annotate(WorkHeader, (.02,.56), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02,.518), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.503), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04,.425), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.4), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.385), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.307), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02,.295), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02,.28), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkThreeDesc, (.04,.235), weight='regular', fontsize=9)
plt.annotate(EduHeader, (.02,.185), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02,.155), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02,.14), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduOneDesc, (.04,.125), weight='regular', fontsize=9)
plt.annotate(EduTwoTitle, (.02,.08), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.02,.065), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduTwoDesc, (.04,.05), weight='regular', fontsize=9)
plt.annotate(SkillsHeader, (.7,.7), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.56), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (.7,.43), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ExtrasDesc, (.7,.345), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(CodeTitle, (.7,.2), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(CodeDesc, (.7,.145), weight='regular', fontsize=10, color='#ffffff')

plt.savefig('CV-Anton-Altynbaev.png', dpi=300, bbox_inches='tight')

