import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Supriya Pandey
##### *Resume* 
''')

image = Image.open('dp.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
A sincere individual with strong values working skilled in problem solving, looking for an opportunity to work in an interactive workplace where the aim is to achieve long term growth of the company through customer satisfaction and improved performance standards.

''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Supriya Pandey</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



st.markdown('## Contact', unsafe_allow_html=True)
with st.expander('Contact'):
  st.write('''
  '**Phone - +91 8697645363** 
  ''')
  st.write('''
  '**Mail - werock.pandey@gmail.com** 
  ''')



#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

with st.expander('Education'):
  txt('**Bachelors of Technology** (Information Technology), *Techno India Salt Lake*, Kolkata','')

#####################
st.markdown('''
## Work Experience
''')
with st.expander('Work Experience'):
  txt('**Project 1 - CITI BANK **, Automation ',
  '')
  txt('**key Technologies**, Python,Pyspark, Bigdata(Hadoop), Autosys, Lightspeed',
  '')
  st.markdown('''
  - Built User Interface, background code for functionality, and successfully deployed.
  - Automated and deployed Production Validation process to eliminate human error and reduced time from 2 hours to 2 mins per associate.
  - Created dashboard to show recon of source to destination table ingestion data
  - Created user interface and automated process of creating data catalog for each table
  - Implemented and automated data quality checks for table ingestion at source side to avoid downstream impact
  - Analyzed the various production issues, done RCA and took various steps to avoid them
  - Worked on regulatory reporting projects for multiple countries
  - Successfully migrated reports from SAP BO to Python using Pandas, Pyspark OpenPyXL and PyFPDF
  ''')

  txt('**Project 2 - RUSHMORE**, Python Developer',
  '')
  txt('**key Technologies**, Python, SQL Alchemy, Streamlit',
  '')
  st.markdown('''
  - Worked on writing scripts to extract multiple sql queries and categorizing and formatting it in different columns of excel file wrote Python logic for the sql queries, and created UI with SQL connection
  - Created UI with tabs for separate categories which in turn consisted of multiple functionalities
  - Created feature to create, upload tables with data from single and multiple files and delete records, drop table(s) single/multiple and create backup of selected table based on type of deals.
  - Created feature to create combined data file from multiple tables and run the python logics which yielded output based on the selected template and format the data which could further downloaded with the download buttons required.
  - Created functionality to create /edit logics in Database from the UI based on type and deal name. Worked on script to combine files based of input keep in a folder and split different tabs of excel in separate files.
  ''')

  txt('**Project 3 - Nationstar Morigage.LLC**, Acquisition & Risk Reporting Analyst',
  '')
  txt('**key Technologies**, SSIS, Excel, SQL, VBA',
  '')
  txt('Automation Analyst :  ',
  '')
  st.markdown('''
  - It includes receiving data from prior servicers then conversion of the received data into readable format upload it into the database and according to the mapping provided generate reports/templates using technologies such as Monarch, SQL, SSIS VBA macro, EXCEL
  - Manipulated the queries for the required output Have created VBA macros as we ll for reporting purpose and updated the VBA codes when there were any changes advised
  - Have created macro to select the file from any location for copying. purging, formatting based on conditions and creating new files and storing at desired locations.
  - Have basic knowledge of SSIS due to short duration interaction.
  ''')

  txt('Risk Reporting Analyst :  ',
  '')
  st.markdown('''
  - Developed dashboards in Excel and Power Bi tor better view of the process to senior management provided functionalities drill down to record level for business use as well.
  - Automated and- optimized the process by eliminating the repeated manual process by using SQL, SSIS packages,Excel, VBA Macros.
  - Worked on Enterprise risk Dashboard and compliance also Own Weekly. Monthly reports of the Company Portfolio performance which are sent to top management.
  - Worked on other adhoc analysis requirement from Senior Management
  - Worked on Enterprise risk Dashboard and compliance also Own Weekly. Monthly reports of the Company Portfolio performance which are sent to top management.
  - Worked on other adhoc analysis requirement from Senior Management
  ''')

  txt('**Project 4 - WM Morrisonsr**, Technology Analyst',
  '')
  txt('**Key Technologies*, [SQL, Excel, Client Application',
  '')
  st.markdown('''
  - Carrying out disaster recovery activities
  - Checking issues reported by Clients on backend (5Ol Server Management Studio).
  - Troubleshooting for any minor, or critical incident that is observed on the application.
  - Demonstrating abilities in Fast Issue Resolution, Solving Tickets and Technical Support.
  - Handling escalation issues at LI, L2 level end inclusive of attending calls and reporting to duty managers onsite /offshore.
  - Having excellent inter-personal skill with ability to work as part of team as well as independently.
  - Interacting with Clients, preparing multiple documents for clients' understanding of applications.
  - Maintaining daily, weekly reports for reviewing overall performance in terms of SLAS.
  ''')

#####################
st.markdown('''
## Skills
''')
with st.expander('Skills'):
  txt3('Programming', '`Python`, `Regex`,  `Big Data(Hadoop)`, `Pyspark`')
  txt3('Data processing', '`SQL`, `pandas`, `numpy`')
  txt3('Data visualization', '`plotly`')
  txt3('UI', '`Streamlit`')

#####################
st.markdown('''
## Social Media
''')
with st.expander('Social Connect'):
  txt2('LinkedIn', 'https://www.linkedin.com/in/supriya-pandey-8b601389?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app')

